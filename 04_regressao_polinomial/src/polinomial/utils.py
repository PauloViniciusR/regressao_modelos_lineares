"""Organização dos resultados para tabelas e gráficos."""
import pandas as pd


def organiza_resultados(resultados):
    """Cria uma linha por divisão e apresenta MAE e RMSE positivos."""
    tabelas = []
    for nome, scores in resultados.items():
        tabela = pd.DataFrame(scores).assign(model=nome)
        tabela["time_seconds"] = tabela["fit_time"] + tabela["score_time"]
        tabela["MAE"] = -tabela["test_neg_mean_absolute_error"]
        tabela["RMSE"] = -tabela["test_neg_root_mean_squared_error"]
        tabelas.append(tabela)
    return pd.concat(tabelas, ignore_index=True)
