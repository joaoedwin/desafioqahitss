from pydantic import BaseModel, Field


class SentimentRequest(BaseModel):
    """Schema de entrada do endpoint de classificação de sentimento."""

    # Mantemos o nome `comentario` para refletir a linguagem do domínio (PT-BR).
    comentario: str = Field(
        ..., min_length=1, description="Texto enviado pelo usuário para análise de sentimento."
    )


class SentimentResponse(BaseModel):
    """Schema de saída retornado pelo endpoint de classificação de sentimento."""

    # O valor é validado no teste de contrato para permanecer dentro do esperado.
    sentimento: str = Field(
        ..., description="Classificação do sentimento: positivo, neutro ou negativo."
    )

    # Score representa a confiança do modelo para o rótulo retornado.
    score: float = Field(
        ..., ge=0.0, le=1.0, description="Confiança do modelo para a classificação."
    )
