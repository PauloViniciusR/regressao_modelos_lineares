"""Integração entre as bases da aula e as funções usadas nos notebooks."""
import json
import os
from pathlib import Path
import sys
import unittest

os.environ.setdefault("MPLBACKEND", "Agg")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "04_regressao_polinomial" / "src"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from polinomial.config import (
    DADOS_EXEMPLO_POLINOMIAL,
    DADOS_EXEMPLO_SINTETICO,
    DADOS_DIABETES_TRATADOS,
    DADOS_DIABETES_CATEGORIZADOS,
)
from polinomial.graficos import plot_comparar_metricas_modelos
from polinomial.modelos import (
    grid_search_cv_regressor,
    organiza_resultados,
    treinar_e_validar_modelo_regressao,
)


class MateriaisPolinomial(unittest.TestCase):
    def test_bases_disponiveis_e_exemplo_separado(self):
        df = pd.read_csv(DADOS_EXEMPLO_POLINOMIAL)
        self.assertEqual(list(df.columns), ["X", "y"])
        self.assertFalse(df.isna().any().any())
        self.assertNotEqual(DADOS_EXEMPLO_SINTETICO, DADOS_EXEMPLO_POLINOMIAL)
        for caminho in (DADOS_DIABETES_TRATADOS, DADOS_DIABETES_CATEGORIZADOS):
            self.assertIn("target", pd.read_parquet(caminho).columns)

    def test_api_da_aula_com_transformacao_do_alvo(self):
        df = pd.read_csv(DADOS_EXEMPLO_POLINOMIAL)
        X, y = df[["X"]], df["y"]
        scores = treinar_e_validar_modelo_regressao(
            X, y, LinearRegression(), preprocessor=PolynomialFeatures(2),
            target_transformer=StandardScaler(), n_splits=2,
        )
        tabela = organiza_resultados({"Polinomial": scores})
        self.assertTrue(np.isfinite(tabela["RMSE"]).all())
        self.assertTrue((tabela["MAE"] >= 0).all())
        busca = grid_search_cv_regressor(
            LinearRegression(),
            {"regressor__preprocessor__degree": [1, 2]},
            preprocessor=PolynomialFeatures(include_bias=False),
            target_transformer=StandardScaler(), n_splits=2,
        ).set_params(n_jobs=1)
        busca.fit(X, y)
        self.assertTrue(np.isfinite(busca.predict(X)).all())
        self.assertIn(busca.best_params_["regressor__preprocessor__degree"], (1, 2))

    def test_resumo_preserva_modelos_de_graus_diferentes(self):
        notebook = ROOT / "04_regressao_polinomial/notebooks/01_regressão_polinomial_resumo.ipynb"
        contexto = {}
        anterior = Path.cwd()
        mostrar = plt.show
        try:
            os.chdir(notebook.parent)
            plt.show = lambda: plt.close("all")
            for i, celula in enumerate(json.loads(notebook.read_text())["cells"]):
                if celula["cell_type"] == "code":
                    exec(compile("".join(celula["source"]), f"{notebook}:{i}", "exec"), contexto)
            regressores = []
            for grau in (1, 3, 8):
                modelo = contexto["parametros_modelos"][f"Grau {grau}"]["modelo"]
                regressores.append(modelo["reg"])
                self.assertEqual(modelo["reg"].n_features_in_, grau)
                predicoes = modelo.predict(contexto["df_xfit"])
                self.assertEqual(len(predicoes), len(contexto["df_xfit"]))
                self.assertTrue(np.isfinite(predicoes).all())
            self.assertEqual(len(set(map(id, regressores))), 3)
        finally:
            os.chdir(anterior)
            plt.show = mostrar
            plt.close("all")

    def test_notebook_sintetico_continua_executavel(self):
        notebook = ROOT / "04_regressao_polinomial/notebooks/02_regressao_polinomial.ipynb"
        contexto = {}
        anterior = Path.cwd()
        mostrar = plt.show
        try:
            os.chdir(ROOT)
            plt.show = lambda: plt.close("all")
            for i, celula in enumerate(json.loads(notebook.read_text())["cells"]):
                if celula["cell_type"] == "code":
                    exec(compile("".join(celula["source"]), f"{notebook}:{i}", "exec"), contexto)
            self.assertEqual(len(contexto["df_resultados"]), 20)
            self.assertEqual(set(contexto["modelos_ajustados"]), {1, 2, 3, 5})
            # Os gráficos também aceitam as colunas de scoring da aula, sem MAE/RMSE extras.
            bruto = contexto["df_resultados"].drop(columns=["MAE", "RMSE"])
            plot_comparar_metricas_modelos(bruto)
        finally:
            os.chdir(anterior)
            plt.show = mostrar
            plt.close("all")


if __name__ == "__main__":
    unittest.main()
