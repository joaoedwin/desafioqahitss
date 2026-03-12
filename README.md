# Sentiment AI QA

POC para validação de uma API de análise de sentimento baseada em IA. A API recebe um comentário e retorna um JSON com `sentimento` e `score`.

## Requisitos

Python 3.14+

## Configuração

1. Criar um arquivo `.env` na raiz do projeto (use `.env.example` como referência).
2. Instalar dependências.

```powershell
python -m pip install -r requirements.txt
```

## Executar a API

```powershell
python -m uvicorn app.main:app --reload
```

Endpoint:

`POST http://127.0.0.1:8000/sentiment`

Body (JSON):

```json
{
  "comentario": "Gostei muito do atendimento, foi rápido e eficiente."
}
```

## Testes automatizados

A suíte automatizada valida:

- Contrato do retorno (campos `sentimento` e `score`, enum e range)
- Validação de request inválida (comentário vazio)
- Padronização do erro upstream (falha do provedor de IA)

Executar testes:

```powershell
python -m pytest -vv
```

Para ver o payload e o retorno no console:

```powershell
$env:SHOW_AI_OUTPUT="1"
python -m pytest -vv -s
```

## Evidências

Gerar relatório JUnit XML:

```powershell
python -m pytest -vv --junitxml=reports\pytest-results.xml
```

Salvar o output do console em arquivo:

```powershell
$env:SHOW_AI_OUTPUT="1"
python -m pytest -vv -s | Tee-Object -FilePath reports\pytest-output-com-debug.txt
```

## Cenários

Os cenários estão em `reports/cenarios.md` e em arquivos por teste em `reports/TEST-*/`.
