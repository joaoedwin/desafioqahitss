## Core
# BDD
Given que usuário envia comentário
When o sistema processa o comentário
Then o sistema deve retornar a classificação do sentimento e o score de confiança

## Comandos:
# Utilizamos o JUnit para salvar o resultado do teste automatizado em .xml
python -m pytest -vv -s --junitxml=reports\pytest-results.xml - reports/pytest-results.xml

# Utilizamos os parâmetros -vv e -s para ver o output do teste no Power Shell
python -m pytest -vv -s | Tee-Object -FilePath reports\pytest-output-com-debug.txt
# Evidencias nas pasta e JIRA