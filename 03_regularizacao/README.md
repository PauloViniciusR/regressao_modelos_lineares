# Modelos de Regularizacao

Projeto de estudo e comparacao de modelos de regressao com tecnicas de regularizacao.

## Estrutura

- `dados/`: datasets usados nos experimentos.
- `notebooks/`: analises exploratorias e experimentos.
- `src/`: funcoes reutilizaveis para configuracao, modelagem, metricas e graficos.
- `modelos/`: artefatos de modelos treinados, mantidos fora do Git por padrao.
- `relatorios/`: saidas e imagens geradas, mantidas fora do Git por padrao.

## Fluxo do projeto

1. Analise exploratoria dos dados no notebook.
2. Tratamento e preparacao das features.
3. Treinamento com validacao cruzada para reduzir risco de overfitting.
4. Comparacao dos modelos com R2, MAE e RMSE.
5. Visualizacao de coeficientes, residuos e desempenho.
