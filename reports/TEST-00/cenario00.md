## TEST-00 (Auto)
# BDD
Given que a comunicação com o provedor de IA falhou
When o sistema processa o comentário
Then o sistema deve retornar status code 502
And a resposta deve conter os campos "error_type" e "error_message"
And a mensagem de erro deve ser padronizada e clara

## Comandos:
# Utilizamos o JUnit para salvar o resultado do teste automatizado em .xml
python -m pytest -vv -s --junitxml=reports\pytest-results.xml - reports/pytest-results.xml

# Utilizamos os parâmetros -vv e -s para ver o output do teste no Power Shell
python -m pytest -vv -s | Tee-Object -FilePath reports\pytest-output-com-debug.txt
# Evidencias nas pasta e JIRA
