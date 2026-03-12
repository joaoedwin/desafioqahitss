from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from app.ai_client import classify_sentiment_with_gemini
from app.config import load_environment_variables
from app.schemas import SentimentRequest, SentimentResponse


def create_application() -> FastAPI:
    """Factory da aplicação.

    Motivo:
    - Facilita importação no teste sem efeitos colaterais.
    - Mantém o entrypoint organizado (padrão comum em projetos Python).
    """

    load_environment_variables()

    application = FastAPI(title="Sentiment AI QA - POC")

    @application.post("/sentiment", response_model=SentimentResponse)
    def classify_sentiment_endpoint(payload: SentimentRequest) -> SentimentResponse:
        """Classifica o sentimento a partir do comentário do usuário."""

        try:
            model_result = classify_sentiment_with_gemini(payload.comentario)
        except Exception as exc:
            # Para POC: tratamento simples, porém explícito. O upstream (IA) falhou.
            return JSONResponse(
                status_code=502,
                content={
                    "error_type": exc.__class__.__name__,
                    "error_message": str(exc),
                },
            )

        # Validamos o payload retornado mapeando para o schema de resposta.
        # Se o retorno não respeitar o contrato (ex.: score fora do range), o Pydantic
        # vai levantar exceção. Em produção, isso deveria ser tratado e convertido
        # em um erro de upstream mais amigável.
        return SentimentResponse(**model_result)

    return application


app = create_application()
