from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parents[2]
PASTA_DADOS = PASTA_PROJETO / "dados"
PASTA_MODELOS = PASTA_PROJETO / "modelos"
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
DADOS_EXEMPLO_POLINOMIAL = PASTA_DADOS / "exemplo_polinomial.csv"
