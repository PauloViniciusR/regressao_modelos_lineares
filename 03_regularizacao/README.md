# Regularização

Estudo das penalizações L1 e L2 com Ridge, Lasso e ElasticNet. Os experimentos analisam hiperparâmetros, coeficientes e desempenho em regressão.

## Notebooks

| Notebook | Objetivo |
| --- | --- |
| [01 · Regularização](notebooks/01_regularizacao.ipynb) | Explorar o efeito da intensidade da penalização |
| [02 · Comparação](notebooks/02_GridSearchCV.ipynb) | Comparar os três modelos com validação cruzada aninhada |
| [02a · Ridge](notebooks/02a_GridSearchCV_Ridge.ipynb) | Ajustar alpha e analisar a penalização L2 |
| [02b · Lasso](notebooks/02b_GridSearchCV_Lasso.ipynb) | Ajustar alpha e analisar a penalização L1 |
| [02c · ElasticNet](notebooks/02c_GridSearchCV_ElasticNet.ipynb) | Ajustar alpha e l1_ratio |

## Comparação dos modelos

Os três modelos testam as mesmas opções de pré-processamento, transformação do alvo e valores de alpha. ElasticNet testa também l1_ratio. A busca seleciona o menor RMSE médio.

A comparação final usa validação cruzada aninhada e inclui regressão linear e DummyRegressor como referências. As tabelas exibem MAE e RMSE positivos; menores valores indicam erros menores.

## Execução

Selecione o kernel `machine_learn` e execute as células em ordem. Cada notebook de Ridge, Lasso e ElasticNet funciona de forma independente. A configuração do ambiente está no [README principal](../README.md).

As bases estão em `dados/` e as funções compartilhadas em `src/`. Os artefatos gerados em `modelos/` e `relatorios/` ficam fora do Git por padrão.
