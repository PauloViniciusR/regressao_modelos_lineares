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
    "04_regressao_polinomial": "polinomial",
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
        import importlib

        # Alternar a ordem reproduz a troca de notebooks sem reiniciar o kernel.
        for modulo in (*MODULOS, *reversed(MODULOS)):
            notebook = sorted((ROOT / modulo / "notebooks").glob("*.ipynb"))[0]
            self.executar_imports(notebook, ROOT)

        funcoes = []
        pastas_dados = []
        for modulo, pacote in MODULOS.items():
            config = importlib.import_module(f"{pacote}.config")
            modelos = importlib.import_module(f"{pacote}.modelos")
            self.assertEqual(config.PASTA_PROJETO, ROOT / modulo)
            self.assertEqual(config.PASTA_DADOS, ROOT / modulo / "dados")
            funcoes.append(modelos.treinar_e_validar_modelo_regressao)
            pastas_dados.append(config.PASTA_DADOS)

        self.assertEqual(len(set(funcoes)), len(MODULOS))
        self.assertEqual(len(set(pastas_dados)), len(MODULOS))


if __name__ == "__main__":
    unittest.main()
