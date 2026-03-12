DESAFIO
Imagine que você faz parte do time de QA de uma aplicação que utiliza um modelo de IA para classificar automaticamente o sentimento de comentários de usuários em uma plataforma.
A funcionalidade recebe um texto enviado pelo usuário e retorna uma classificação de sentimento:
•	Positivo
•	Neutro
•	Negativo
Exemplo de entrada:
Comentário:
"Gostei muito do atendimento, foi rápido e eficiente."
Resposta esperada da API:
{
"sentimento": "positivo",
"score": 0.92
}
O QUE ESPERAMOS NA SUA SOLUÇÃO
Prepare uma pequena apresentação e demonstração abordando os seguintes pontos:
1.	Estratégia de Testes
Explique como você abordaria os testes dessa funcionalidade baseada em IA.
Considere aspectos como:
•	variação de inputs
•	consistência das respostas
•	cenários positivos e negativos
•	possíveis riscos ou limitações de um modelo de IA.
2.	Cenários de Teste
Liste alguns cenários de teste que você considera importantes para validar esse tipo de funcionalidade.
3.	Cenário Automatizado
Implemente ao menos um cenário automatizado que valide o comportamento da funcionalidade.
Pode ser, por exemplo:
•	validação de classificação de sentimento
•	verificação de resposta da API
•	validação de estrutura do retorno.
Você pode utilizar a ferramenta ou linguagem de sua preferência (por exemplo: Python, Robot Framework, Cypress, Playwright, etc.).
4.	Evidências de Teste
Apresente evidências da execução do teste automatizado, como:
•	logs
•	prints
•	relatórios de execução
•	output do teste
5.	Explicação da Solução
Durante a entrevista, você poderá explicar:
•	como estruturou o teste
•	quais decisões tomou
•	como evoluiria essa automação em um projeto real.
