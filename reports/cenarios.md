# Core (Automatizado)
Given que o usuário envia um comentário para análise de sentimento
When o sistema processa o comentário
Then o sistema deve retornar a classificação do sentimento e o score de confiança

# Cenário 0 - TEST-00 (Automatizado)
Given que a comunicação com o provedor de IA falhou
When o sistema processa o comentário
Then o sistema deve retornar status code 502
And a resposta deve conter os campos "error_type" e "error_message"
And a mensagem de erro deve ser padronizada e clara

# Cenário 1 - TEST-01 (Automatizado)
Given que o usuário envia um comentário vazio
When o sistema processa o comentário
Then o sistema deve retornar um erro

# Cenário 2 - TEST-02 (Manual)
Given que o usuário envia um comentário com elogio
When o sistema processa o comentário
Then o sistema deve retornar a classificação do sentimento POSITIVO e score de confiança

# Cenário 3 - TEST-03 (Manual)
Given que o usuário envia um comentário com crítica construtiva
When o sistema processa o comentário
Then o sistema deve retornar a classificação do sentimento NEUTRO e score de confiança

# Cenário 4 - TEST-04 (Manual)
Given que o usuário envia um comentário com crítica severa
When o sistema processa o comentário
Then o sistema deve retornar a classificação do sentimento NEGATIVO e score de confiança

======================================================================================

## CENÁRIOS CANDIDATOS (Não especificados como requisito, mas considerados relevantes)

# Cenário 1 (CENÁRIO CANDIDATO)
Given que o usuário envia um comentário com menos de 3 caracteres
When o sistema processa o comentário
Then o sistema deve retornar um erro

# Cenário 2 (CENÁRIO CANDIDATO)
Given que o usuário envia um comentário com mais de 500 caracteres
When o sistema processa o comentário
Then o sistema deve retornar um erro

# Cenário 3 (CENÁRIO CANDIDATO)
Given que o usuário envia um comentário com caracteres especiais
When o sistema processa o comentário
Then o sistema deve retornar a classificação do sentimento e o score de confiança

# Cenário 4 (CENÁRIO CANDIDATO)
Given que o usuário envia um comentário com emojis
When o sistema processa o comentário
Then o sistema deve retornar a classificação do sentimento e o score de confiança