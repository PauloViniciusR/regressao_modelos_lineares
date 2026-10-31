# Regressão com modelos lineares

Estudos e experimentos de regressão com Python e scikit-learn. O repositório reúne fundamentos de Machine Learning, preparação de dados, pipelines, validação cruzada e comparação de modelos lineares regularizados.

## Conteúdo

| Módulo | Temas | Status |
| --- | --- | --- |
| [01 · Fundamentos](01_fundamentos/) | Tipos de aprendizado e etapas de um projeto de Machine Learning | Disponível |
| [02 · Modelos de regressão](02_modelos_regressao/) | Análise exploratória, regressão linear, transformações e validação cruzada | Disponível |
| [03 · Regularização](03_regularizacao/) | Ridge, Lasso, ElasticNet e otimização com GridSearchCV | Disponível |
| [04 · Regressão polinomial](04_regressao_polinomial/) | Expansão de variáveis, comparação de graus e validação cruzada | Exemplo inicial |
| [05 · Projeto de regressão](05_projeto_regressao/) | Aplicação do fluxo de modelagem em um projeto | Planejado |

Os experimentos de regressão e GridSearchCV utilizam o dataset Diabetes do scikit-learn. A avaliação considera R², MAE e RMSE, com modelos de referência e pipelines de pré-processamento.

## Regularização e GridSearchCV

Os três modelos seguem a mesma lógica de busca e apresentação dos resultados. A comparação final usa validação cruzada aninhada para avaliar a seleção dos hiperparâmetros.

| Notebook | Objetivo |
| --- | --- |
| [Comparação dos modelos](03_regularizacao/notebooks/02_GridSearchCV.ipynb) | Comparar Ridge, Lasso e ElasticNet com regressão linear e DummyRegressor |
| [Ridge](03_regularizacao/notebooks/02a_GridSearchCV_Ridge.ipynb) | Explorar a penalização L2 e ajustar `alpha` |
| [Lasso](03_regularizacao/notebooks/02b_GridSearchCV_Lasso.ipynb) | Explorar a penalização L1 e analisar coeficientes nulos |
| [ElasticNet](03_regularizacao/notebooks/02c_GridSearchCV_ElasticNet.ipynb) | Combinar L1 e L2, ajustando `alpha` e `l1_ratio` |

## Ambiente e execução

Requisitos: Conda e um editor com suporte a notebooks Jupyter.

```bash
git clone https://github.com/PauloViniciusR/regressao_modelos_lineares.git
cd regressao_modelos_lineares
conda env create -f environment.yml
conda activate machine_learn
```

Abra o [workspace](regressao_modelos_lineares.code-workspace), selecione o kernel **machine_learn** e execute as células do notebook em ordem. Se o ambiente já estiver instalado, basta selecioná-lo. Use o `environment.yml` da raiz como referência do ambiente compartilhado.

Os módulos usam pacotes distintos: `regressao`, `regularizacao` e `polinomial`, dentro de suas pastas `src/`. Os notebooks localizam esses pacotes ao executar da raiz, do módulo ou da pasta `notebooks/`.

### Dados

- **Módulo 02:** as bases são geradas pelos notebooks e ficam fora do Git. Execute primeiro [01_EDA.ipynb](02_modelos_regressao/notebooks/01_EDA.ipynb), seguido de [06_outras_transformacoes.ipynb](02_modelos_regressao/notebooks/06_outras_transformacoes.ipynb).
- **Módulo 03:** as bases utilizadas estão incluídas em `03_regularizacao/dados/`.

## Verificação das importações

Com o ambiente `machine_learn` ativo, execute na raiz:

```bash
python -m unittest discover -s tests -v
```

A verificação cobre os imports dos notebooks em diferentes diretórios e o uso dos três módulos na mesma sessão Python.

## Organização

Nos módulos de modelagem, `notebooks/` reúne os experimentos e `src/` concentra as funções de configuração, treinamento e visualização. Dados, modelos treinados e relatórios ficam nas pastas correspondentes de cada módulo.

[Padrão de commits](CONTRIBUTING.md) · [Histórico da migração](MIGRACAO.md) · [Licença do módulo 02](02_modelos_regressao/LICENSE)
