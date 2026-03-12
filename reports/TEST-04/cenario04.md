## TEST-04
# BDD
Given que o usuário envia um comentário com reclamação
When o sistema processa o comentário
Then o sistema deve retornar a classificação do sentimento NEGATIVO e score de confiança

# Comentário:
"O atendimento foi muito ruim, não recomendo."

## Comandos:
# Utilizamos o uvicorn para rodar o servidor (API)
python -m uvicorn app.main:app --reload

# Evidencias nas pasta e JIRA