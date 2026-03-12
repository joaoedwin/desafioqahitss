## TEST-02
# BDD
Given que o usuário envia um comentário com elogio
When o sistema processa o comentário
Then o sistema deve retornar a classificação do sentimento POSITIVO e score de confiança

# Comentário:
"Gostei muito do atendimento, foi rápido e eficiente."

## Comandos:
# Utilizamos o uvicorn para rodar o servidor (API)
python -m uvicorn app.main:app --reload

# Evidencias nas pasta e JIRA