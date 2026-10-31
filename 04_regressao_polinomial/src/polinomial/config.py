from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parents[2]
PASTA_DADOS = PASTA_PROJETO / "dados"
PASTA_MODELOS = PASTA_PROJETO / "modelos"
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
# Bases fornecidas na aula.
DADOS_EXEMPLO_POLINOMIAL = PASTA_DADOS / "dados_polinomial.csv"
DADOS_DIABETES_TRATADOS = PASTA_DADOS / "diabetes.parquet"
DADOS_DIABETES_CATEGORIZADOS = PASTA_DADOS / "diabetes_categorizado.parquet"

# Saída opcional do exemplo sintético, separada dos dados da aula.
DADOS_EXEMPLO_SINTETICO = PASTA_DADOS / "exemplo_polinomial.csv"
