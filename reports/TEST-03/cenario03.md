## TEST-03
# BDD
Given que o usuário envia um comentário com crítica construtiva
When o sistema processa o comentário
Then o sistema deve retornar a classificação do sentimento NEUTRO e score de confiança

# Comentário:
"O atendimento foi bom, mas poderia ser mais rápido."

## Comandos:
# Utilizamos o uvicorn para rodar o servidor (API)
python -m uvicorn app.main:app --reload

# Evidencias nas pasta e JIRA