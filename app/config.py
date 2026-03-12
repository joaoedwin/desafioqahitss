import os

from dotenv import load_dotenv


def load_environment_variables() -> None:
    """Carrega variáveis de ambiente a partir do arquivo `.env` na raiz do projeto.

    Motivo:
    - Mantém credenciais fora do código-fonte.
    - Facilita execução local (ambiente reprodutível) sem setup manual.
    """

    # Por padrão, procura o arquivo `.env` no diretório de execução (working directory).
    load_dotenv(override=False)


def get_required_env_variable(variable_name: str) -> str:
    """Lê uma variável de ambiente obrigatória.

    Args:
        variable_name: Nome da variável esperada (ex.: `GEMINI_API_KEY`).

    Returns:
        Valor da variável.

    Raises:
        RuntimeError: Quando a variável não existe ou está vazia.
    """

    variable_value = os.getenv(variable_name)

    if variable_value is None or variable_value.strip() == "":
        raise RuntimeError(
            f"Variável de ambiente obrigatória não configurada: {variable_name}. "
            "Configure-a no arquivo .env na raiz do projeto."
        )

    return variable_value


def get_optional_env_variable(variable_name: str, default_value: str) -> str:
    """Lê uma variável de ambiente opcional, com valor padrão.

    Args:
        variable_name: Nome da variável.
        default_value: Valor usado quando a variável não estiver definida.

    Returns:
        Valor da variável ou o padrão.
    """

    variable_value = os.getenv(variable_name)

    if variable_value is None or variable_value.strip() == "":
        return default_value

    return variable_value
