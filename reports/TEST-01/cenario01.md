## TEST-01 (Auto)
# BDD
Given que usuário envia um comentário vazio
When o sistema processa o comentário
Then o sistema deve retornar um erro

## Comandos:
# Utilizamos o uvicorn para rodar o servidor (API)
python -m uvicorn app.main:app --reload

# Evidencias nas pasta e JIRA
