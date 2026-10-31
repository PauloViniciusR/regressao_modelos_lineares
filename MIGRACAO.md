# Registro da migração

Data: 31/10/2026.

| Origem | Destino | Commit importado |
| --- | --- | --- |
| `Modelos_regressao` | `02_modelos_regressao` | `406c127ca836044f8769631adfbf826b5ac473ab` |
| `Regularização` | `03_regularizacao` | `7a4f6b335e7c8daaa9cf9a1da885b940398ebe42` |

Repositórios de origem:

- https://github.com/PauloViniciusR/Modelos_regressao
- https://github.com/PauloViniciusR/Modelos_regularizacao

Os commits originais são ancestrais de `main` neste repositório. As importações usam merges sem squash; os caminhos antigos permanecem nos commits históricos. Para consultar o histórico antes da importação, use `git log COMMIT_IMPORTADO` com o SHA da tabela.

A pasta de trabalho foi consolidada em `regressao_modelos_lineares`, com o mesmo nome do repositório no GitHub. As pastas locais duplicadas foram retiradas após a conferência dos arquivos e preservadas em um backup externo. O destino dos repositórios remotos antigos é administrado separadamente. Os dados ignorados do módulo 02 foram copiados apenas localmente. Notebooks tiveram os caminhos de importação adaptados à nova estrutura; ambientes originais e licença do módulo 02 foram preservados.

## Organização local

Os pacotes Python foram separados em `regressao` e `regularizacao` para evitar colisões de imports. O ambiente compartilhado é definido somente no `environment.yml` da raiz.
