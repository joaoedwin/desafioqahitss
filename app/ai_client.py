import json
import re
from typing import Any, Dict

from google import genai

from app.config import get_optional_env_variable, get_required_env_variable


def build_gemini_client() -> genai.Client:
    """Cria o client do Gemini a partir das variáveis de ambiente.

    Centralizar a criação do client facilita:
    - reutilização do mesmo ponto de configuração
    - substituição por mock/stub futuramente (testes)
    """

    gemini_api_key = get_required_env_variable("GEMINI_API_KEY")

    # A SDK autentica via API Key.
    return genai.Client(api_key=gemini_api_key)


def build_sentiment_prompt(user_comment: str) -> str:
    """Monta um prompt restritivo, exigindo resposta em JSON.

    Motivo:
    - Em automação, previsibilidade é essencial.
    - Quanto mais restrito o prompt, menor a chance de o modelo adicionar texto extra.

    Contrato esperado na resposta do modelo:
    - Deve conter as chaves: `sentimento` e `score`
    - `sentimento` deve ser: positivo | neutro | negativo
    - `score` deve ser um número entre 0 e 1
    """

    return (
        "Você é um classificador de sentimento. "
        "Retorne APENAS um JSON válido (sem markdown, sem texto extra). "
        "Formato esperado: {\"sentimento\": \"positivo|neutro|negativo\", \"score\": 0.0}. "
        "\n\n"
        "Regras:\n"
        "- 'sentimento' deve ser um dos valores: positivo, neutro, negativo\n"
        "- 'score' deve ser um número entre 0 e 1\n"
        "- Responda somente com JSON\n"
        "\n\n"
        f"Comentário do usuário: {user_comment}"
    )


def classify_sentiment_with_gemini(user_comment: str) -> Dict[str, Any]:
    """Chama o Gemini e converte a resposta em um dicionário Python.

    Args:
        user_comment: Comentário bruto do usuário a ser classificado.

    Returns:
        Um dicionário com as chaves `sentimento` e `score`.

    Raises:
        ValueError: Quando o texto retornado não pode ser interpretado como JSON.
    """

    gemini_model = get_optional_env_variable("GEMINI_MODEL", "gemini-2.5-flash-lite")

    client = build_gemini_client()
    prompt = build_sentiment_prompt(user_comment)

    response = client.models.generate_content(model=gemini_model, contents=prompt)

    # A SDK retorna um objeto estruturado; `text` contém o conteúdo gerado.
    raw_text_output = (response.text or "").strip()

    # O modelo pode devolver o JSON dentro de um "code fence" (markdown), por exemplo:
    # ```json
    # {"sentimento": "positivo", "score": 0.9}
    # ```
    # Para manter o contrato estável, extraímos o primeiro objeto JSON do texto.
    json_candidate_match = re.search(r"\{.*\}", raw_text_output, flags=re.DOTALL)
    json_candidate_text = (
        json_candidate_match.group(0).strip() if json_candidate_match else raw_text_output
    )

    try:
        return json.loads(json_candidate_text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            "O Gemini não retornou uma resposta JSON válida. "
            f"Saída bruta: {raw_text_output}"
        ) from exc
