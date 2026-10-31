# Regressão com Machine Learning

Trilha de estudos com Python e scikit-learn: fundamentos, regressão linear, regularização, regressão polinomial e um projeto aplicado.

## Módulos

| Pasta | Conteúdo | Situação |
| --- | --- | --- |
| [01_fundamentos](01_fundamentos/) | Introdução, tipos de aprendizado e etapas de um projeto | Material disponível |
| [02_modelos_regressao](02_modelos_regressao/) | EDA, regressão linear, pipelines, transformações e validação cruzada | Material disponível |
| [03_regularizacao](03_regularizacao/) | Ridge, Lasso, ElasticNet e GridSearchCV | Material disponível |
| [04_regressao_polinomial](04_regressao_polinomial/) | Expansão polinomial e complexidade dos modelos | Pasta reservada |
| [05_projeto_regressao](05_projeto_regressao/) | Projeto aplicado de regressão | Pasta reservada |

Os módulos 02 e 03 mantêm suas próprias pastas `notebooks`, `src`, `dados`, `modelos` e `relatorios`. Os históricos dos dois repositórios originais foram incorporados sem squash nem reescrita dos commits.

## Executar os notebooks

1. Abra esta pasta no VS Code, ou abra o arquivo `regressao-machine-learning.code-workspace`.
2. Selecione o kernel **machine_learn** em cada notebook. Reinicie o kernel ao trocar de módulo: os módulos 02 e 03 têm pacotes diferentes chamados `src`.
3. Execute as células em ordem. Os caminhos dos notebooks foram ajustados para a nova estrutura.

Para criar o ambiente em outra máquina, a partir da raiz:

```bash
conda env create -f environment.yml
conda activate machine_learn
```

Se esse ambiente já existir, basta selecioná-lo no notebook. A migração não exige recriá-lo. Os arquivos `environment.yml` dentro dos módulos foram mantidos como registros dos projetos originais; use o da raiz para o ambiente compartilhado.

### Dados

Os dados de regularização estão versionados em `03_regularizacao/dados`. No módulo 02, `dados/` continua ignorado pelo Git, como no projeto original. As bases locais foram copiadas para permitir continuar trabalhando nesta máquina. Em um clone novo, crie primeiro a pasta `02_modelos_regressao/dados` (por exemplo, com `mkdir -p 02_modelos_regressao/dados` no terminal). Depois execute `02_modelos_regressao/notebooks/01_EDA.ipynb` e depois `06_outras_transformacoes.ipynb` para gerar as bases antes dos notebooks que as utilizam.

### GridSearchCV

- [Comparação dos três modelos](03_regularizacao/notebooks/02_GridSearchCV.ipynb)
- [Ridge](03_regularizacao/notebooks/02a_GridSearchCV_Ridge.ipynb)
- [Lasso](03_regularizacao/notebooks/02b_GridSearchCV_Lasso.ipynb)
- [ElasticNet](03_regularizacao/notebooks/02c_GridSearchCV_ElasticNet.ipynb)

## Git no dia a dia

Execute os comandos nesta pasta, que é a raiz do novo repositório:

```bash
git status
git add .
git commit -m "Descreve as alterações"
git push
```

## Origem dos materiais

Consulte [MIGRACAO.md](MIGRACAO.md) para os repositórios e commits importados. A licença MIT do módulo 02 permanece em `02_modelos_regressao/LICENSE`; sua presença não altera automaticamente a licença dos demais materiais.
