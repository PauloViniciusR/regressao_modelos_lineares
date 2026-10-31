"""Integração dos imports reais dos notebooks e dos caminhos dos módulos."""
import contextlib
import io
import json
import os
from pathlib import Path
import unittest

os.environ.setdefault("MPLBACKEND", "Agg")
ROOT = Path(__file__).resolve().parents[1]
MODULOS = {
    "02_modelos_regressao": "regressao",
    "03_regularizacao": "regularizacao",
}


def primeira_celula_imports(notebook):
    conteudo = json.loads(notebook.read_text())
    return next(
        "".join(celula["source"])
        for celula in conteudo["cells"]
        if celula["cell_type"] == "code"
        and "PASTA_SRC" in "".join(celula["source"])
    )


@contextlib.contextmanager
def diretorio(pasta):
    anterior = Path.cwd()
    os.chdir(pasta)
    try:
        yield
    finally:
        os.chdir(anterior)


class ImportacoesNotebooks(unittest.TestCase):
    def executar_imports(self, notebook, cwd):
        contexto = {}
        with diretorio(cwd), contextlib.redirect_stdout(io.StringIO()):
            exec(compile(primeira_celula_imports(notebook), str(notebook), "exec"), contexto)
        return contexto

    def test_imports_em_diferentes_diretorios(self):
        for modulo, pacote in MODULOS.items():
            pasta = ROOT / modulo
            for notebook in sorted((pasta / "notebooks").glob("*.ipynb")):
                for cwd in (ROOT.parent, ROOT, pasta, pasta / "notebooks"):
                    with self.subTest(notebook=notebook.name, cwd=str(cwd)):
                        contexto = self.executar_imports(notebook, cwd)
                        self.assertEqual(contexto["PASTA_PROJETO"], pasta)
                        self.assertEqual(contexto["PASTA_SRC"], pasta / "src")
                        for valor in contexto.values():
                            origem = getattr(valor, "__module__", "")
                            self.assertFalse(origem.startswith("src."))

    def test_modulos_coexistem_na_mesma_sessao(self):
        # Alternar a ordem reproduz a troca de notebooks sem reiniciar o kernel.
        for modulo in ("02_modelos_regressao", "03_regularizacao", "02_modelos_regressao"):
            notebook = sorted((ROOT / modulo / "notebooks").glob("*.ipynb"))[0]
            self.executar_imports(notebook, ROOT)

        import regressao.config as config_regressao
        import regularizacao.config as config_regularizacao
        from regressao.modelos import treinar_e_validar_modelo_regressao as treino_regressao
        from regularizacao.modelos import treinar_e_validar_modelo_regressao as treino_regularizacao

        self.assertIsNot(treino_regressao, treino_regularizacao)
        self.assertEqual(config_regressao.PASTA_PROJETO, ROOT / "02_modelos_regressao")
        self.assertEqual(config_regularizacao.PASTA_PROJETO, ROOT / "03_regularizacao")
        self.assertNotEqual(config_regressao.PASTA_DADOS, config_regularizacao.PASTA_DADOS)


if __name__ == "__main__":
    unittest.main()
