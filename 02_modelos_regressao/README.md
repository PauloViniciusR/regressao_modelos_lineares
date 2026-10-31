# Modelos de regressão

Experimentos com o dataset Diabetes do scikit-learn: análise exploratória, regressão linear, pipelines e validação cruzada.

## Ordem de estudo

| Notebook | Tema |
| --- | --- |
| [01 EDA](notebooks/01_EDA.ipynb) | Explorar o dataset Diabetes, organizar as variáveis e gerar a base tratada para os próximos notebooks. |
| [02 regressao linear](notebooks/02_regressao_linear.ipynb) | Treinar uma regressão linear e examinar métricas, resíduos e coeficientes como referência inicial. |
| [03 curva aprendizado](notebooks/03_curva_aprendizado.ipynb) | Analisar como o desempenho de treino e validação muda conforme aumenta o volume de dados de treinamento. |
| [04 introducao a pipelines](notebooks/04_introducao_a_pipelines.ipynb) | Organizar pré-processamento e regressão linear em um pipeline para aplicar as etapas de forma consistente. |
| [05 one hot](notebooks/05_one_hot.ipynb) | Incluir a variável categórica sexo no pipeline com OneHotEncoder e ColumnTransformer. |
| [06 outras transformacoes](notebooks/06_outras_transformacoes.ipynb) | Combinar transformações numéricas e categóricas e gerar a base categorizada usada nos experimentos seguintes. |
| [07 target transformer](notebooks/07_target_transformer.ipynb) | Explorar a transformação do alvo com TransformedTargetRegressor e sua integração ao pipeline. |
| [08 validacao cruzada](notebooks/08_validacao_cruzada.ipynb) | Avaliar o modelo em diferentes divisões dos dados com KFold e cross_validate. |
| [09 dummy regressor](notebooks/09_dummy_regressor.ipynb) | Usar DummyRegressor como referência para verificar o ganho dos modelos de regressão. |
| [10. analise complexidade](notebooks/10.%20analise_complexidade.ipynb) | Comparar estratégias de pré-processamento e observar seus efeitos nas métricas de regressão. |
| [11 outros modelos](notebooks/11_outros_modelos.ipynb) | Comparar regressão linear, Ridge, Lasso e ElasticNet com diferentes configurações de pré-processamento. |

## Execução e dados

Use o ambiente `machine_learn` descrito no [README principal](../README.md). Execute os notebooks em ordem, com um kernel próprio para este módulo.

A pasta `dados/` não é versionada. O notebook 01 cria essa pasta e gera `diabetes_tratados.parquet`; o notebook 06 gera `diabetes_categorizado.parquet`.

As funções reutilizáveis ficam em `src/regressao/`. A análise compara R², MAE e RMSE e inclui DummyRegressor como referência.

[Análise técnica](referencias/analise_tecnica.md) · [Licença MIT deste módulo](LICENSE) · [Próximo módulo: Regularização](../03_regularizacao/)
