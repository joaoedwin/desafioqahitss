import os

from fastapi.testclient import TestClient

from app.main import create_application


def _criar_client() -> TestClient:
    """Cria um cliente de teste para a API.

    Mantemos isso como helper para evitar repetição e deixar a suíte mais legível.
    """

    application = create_application()
    return TestClient(application)


def _validar_contrato_de_resposta(response_json: dict) -> None:
    """Valida o contrato mínimo esperado da resposta de sentimento."""

    assert "sentimento" in response_json
    assert "score" in response_json

    sentimento = response_json["sentimento"]
    score = response_json["score"]

    assert sentimento in {"positivo", "neutro", "negativo"}
    assert isinstance(score, (int, float))
    assert 0.0 <= float(score) <= 1.0


def test_sentiment_endpoint_retorna_200_e_contrato_valido_para_payload_valido() -> None:
    """Teste de contrato (payload válido).

    Objetivo:
    - garantir HTTP 200
    - garantir estrutura do retorno e invariantes (enum e range)
    """

    client = _criar_client()

    request_payload = {"comentario": "Não gostei. Foi péssimo o atendimento!"}
    response = client.post("/sentiment", json=request_payload)

    if response.status_code != 200:
        try:
            response_body_for_debugging = response.json()
        except Exception:
            response_body_for_debugging = response.text

        raise AssertionError(
            "Esperado HTTP 200 no endpoint /sentiment, mas retornou "
            f"{response.status_code}. Corpo da resposta: {response_body_for_debugging}"
        )

    response_json = response.json()

    if os.getenv("SHOW_AI_OUTPUT") == "1":
        print("\n--- Saída de debug do teste de contrato ---")
        print(f"Payload enviado: {request_payload}")
        print(f"Corpo da resposta: {response_json}")

    _validar_contrato_de_resposta(response_json)


def test_sentiment_endpoint_retorna_422_para_comentario_vazio() -> None:
    """Teste negativo (validação de request).

    Como o schema exige `comentario` com tamanho mínimo, esperamos 422.
    """

    client = _criar_client()

    request_payload = {"comentario": ""}
    response = client.post("/sentiment", json=request_payload)

    if os.getenv("SHOW_AI_OUTPUT") == "1":
        print("\n--- Saída de debug do teste 422 (payload inválido) ---")
        print(f"Payload enviado: {request_payload}")
        print(f"Status code: {response.status_code}")
        try:
            print(f"Corpo da resposta: {response.json()}")
        except Exception:
            print(f"Corpo da resposta (texto): {response.text}")

    assert response.status_code == 422


def test_sentiment_endpoint_retorna_502_com_erro_padronizado_quando_upstream_falha(
    monkeypatch,
) -> None:
    """Teste de resiliência (falha do provedor upstream).

    Simulamos uma exceção na chamada ao provedor de IA e validamos que a API:
    - retorna 502
    - devolve um corpo padronizado com `error_type` e `error_message`
    """

    import app.main

    def _falhar_chamada_ia(_comentario: str):
        raise RuntimeError("Falha simulada no provedor de IA")

    monkeypatch.setattr(app.main, "classify_sentiment_with_gemini", _falhar_chamada_ia)

    client = _criar_client()

    request_payload = {"comentario": "Teste de falha upstream"}
    response = client.post("/sentiment", json=request_payload)

    if os.getenv("SHOW_AI_OUTPUT") == "1":
        print("\n--- Saída de debug do teste 502 (falha upstream) ---")
        print(f"Payload enviado: {request_payload}")
        print(f"Status code: {response.status_code}")
        try:
            print(f"Corpo da resposta: {response.json()}")
        except Exception:
            print(f"Corpo da resposta (texto): {response.text}")

    assert response.status_code == 502

    response_json = response.json()
    assert response_json.get("error_type") == "RuntimeError"
    assert "Falha simulada no provedor de IA" in str(response_json.get("error_message"))
