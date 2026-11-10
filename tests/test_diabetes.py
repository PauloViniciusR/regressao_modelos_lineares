"""Integração das células de configuração do notebook Diabetes."""
import contextlib
import io
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

os.environ.setdefault("MPLBACKEND", "Agg")
ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "04_regressao_polinomial/notebooks/03_base_diabetes.ipynb"


class ConfiguracaoDiabetes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import matplotlib.pyplot as plt

        cls.contexto = {}
        anterior = Path.cwd()
        try:
            os.chdir(NOTEBOOK.parent)
            with patch.object(plt, "show", lambda: plt.close("all")), contextlib.redirect_stdout(io.StringIO()):
                for i, celula in enumerate(json.loads(NOTEBOOK.read_text())["cells"]):
                    if celula["cell_type"] != "code":
                        continue
                    fonte = "".join(celula["source"])
                    if "grid_search.fit(" in fonte:
                        break
                    exec(compile(fonte, f"{NOTEBOOK}:{i}", "exec"), cls.contexto)
        finally:
            os.chdir(anterior)
            plt.close("all")

    def test_configuracao_completa_e_parametros(self):
        from sklearn.model_selection import ParameterGrid

        busca = self.contexto["grid_search"]
        self.assertEqual(len(ParameterGrid(busca.param_grid)), 540)
        self.assertEqual(busca.cv.n_splits, 5)
        parametros_validos = busca.estimator.get_params(deep=True)
        for nome in busca.param_grid:
            self.assertIn(nome, parametros_validos)

    def test_expansao_por_grupos_com_nomes_corretos(self):
        import numpy as np
        from sklearn.base import clone

        pre = clone(self.contexto["preprocessamento_completo"]).set_params(
            power_transform_poly__poly__degree=3,
            standard_scaler_poly__poly__degree=2,
        )
        transformado = pre.fit_transform(self.contexto["X"])
        nomes = pre.get_feature_names_out()
        # Quatro entradas: grau 3 gera 34 termos; grau 2 gera 14.
        # A categoria ordinal e o indicador de sexo acrescentam dois termos.
        self.assertEqual(transformado.shape, (442, 50))
        self.assertEqual(len(nomes), transformado.shape[1])
        self.assertTrue(np.isfinite(transformado).all())


if __name__ == "__main__":
    unittest.main()
