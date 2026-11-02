# Regressão polinomial

Comparação de modelos com expansão polinomial, pipelines e validação cruzada.

## Estrutura

```text
04_regressao_polinomial/
├── dados/
├── modelos/
├── notebooks/
│   ├── 01_regressão_polinomial_resumo.ipynb
│   └── 02_regressao_polinomial.ipynb
├── referencias/
├── relatorios/
│   └── imagens/
└── src/
    └── polinomial/
        ├── config.py
        ├── modelos.py
        ├── graficos.py
        ├── auxiliares.py
        └── utils.py
```

## Notebooks

[01 · Resumo da aula](notebooks/01_regressão_polinomial_resumo.ipynb) apresenta os conceitos e compara os graus 1, 3 e 8 com a base fornecida na aula.

### Exemplo sintético

[02 · Regressão polinomial](notebooks/02_regressao_polinomial.ipynb) compara os graus 1, 2, 3 e 5 em dados sintéticos. Inclui avaliação por R², MAE e RMSE, tabelas e gráficos das curvas ajustadas.

Selecione o kernel **machine_learn** e execute as células em ordem. O notebook funciona a partir da raiz, do módulo ou da pasta de notebooks e usa o pacote exclusivo `polinomial`.

O ambiente é o [environment.yml da raiz](../environment.yml). As três bases da aula estão versionadas. Outros dados e artefatos gerados ficam fora do Git por padrão; o exemplo inicial gera seus próprios dados em memória.

## Materiais da aula 1

Os [códigos originais](referencias/aula_01/) estão disponíveis para consulta. As versões adaptadas ao projeto ficam em `src/polinomial/`.

| Base | Configuração | Uso |
| --- | --- | --- |
| `dados_polinomial.csv` | `DADOS_EXEMPLO_POLINOMIAL` | Exemplo da aula, com colunas `X` e `y` |
| `diabetes.parquet` | `DADOS_DIABETES_TRATADOS` | Base Diabetes tratada |
| `diabetes_categorizado.parquet` | `DADOS_DIABETES_CATEGORIZADOS` | Base Diabetes com variável categorizada |

Depois de executar a célula de importações do notebook, os arquivos podem ser carregados assim:

```python
import pandas as pd
from polinomial.config import DADOS_EXEMPLO_POLINOMIAL
from polinomial.auxiliares import dataframe_coeficientes
from polinomial.modelos import (
    construir_pipeline_modelo_regressao,
    treinar_e_validar_modelo_regressao,
    grid_search_cv_regressor,
    organiza_resultados,
)

df = pd.read_csv(DADOS_EXEMPLO_POLINOMIAL)
X = df[["X"]]
y = df["y"]
```

Nas instruções da aula, adapte imports como `from src.modelos` para `from polinomial.modelos`. Os caminhos são relativos ao módulo e não dependem da pasta Downloads.

O notebook `02_regressao_polinomial.ipynb` continua como exemplo sintético. Seu arquivo de saída opcional é `exemplo_polinomial.csv`, separado de `dados_polinomial.csv`.

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
