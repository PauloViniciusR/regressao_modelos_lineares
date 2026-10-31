# Regressão polinomial

Comparação de modelos com expansão polinomial, pipelines e validação cruzada.

## Estrutura

```text
04_regressao_polinomial/
├── dados/
├── modelos/
├── notebooks/
│   └── 01_regressao_polinomial.ipynb
├── referencias/
├── relatorios/
│   └── imagens/
└── src/
    └── polinomial/
        ├── config.py
        ├── modelos.py
        ├── graficos.py
        └── utils.py
```

## Notebook inicial

[01 · Regressão polinomial](notebooks/01_regressao_polinomial.ipynb) compara os graus 1, 2, 3 e 5 em dados sintéticos. Inclui avaliação por R², MAE e RMSE, tabelas e gráficos das curvas ajustadas.

Selecione o kernel **machine_learn** e execute as células em ordem. O notebook funciona a partir da raiz, do módulo ou da pasta de notebooks e usa o pacote exclusivo `polinomial`.

O ambiente é o [environment.yml da raiz](../environment.yml). Dados e artefatos gerados ficam fora do Git por padrão; o exemplo inicial gera os dados em memória.

## Próximos estudos

- Diagnóstico de subajuste e sobreajuste.
- Curvas de aprendizado e seleção do grau.
- Regularização dos termos polinomiais.

## Commits neste módulo

Use o mesmo repositório da trilha. A partir da raiz, adicione somente as alterações relacionadas ao módulo:

```bash
git status
git add 04_regressao_polinomial/
git commit -m "polinomial: organiza experimentos"
git push
```

Para uma alteração específica, use o número do notebook, como `polinomial/01: compara graus`.

[Voltar à trilha](../README.md)
