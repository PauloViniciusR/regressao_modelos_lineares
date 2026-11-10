# Arquivos originais da aula 1

Códigos recebidos na pasta de downloads “Instruções para o bloco - aula 1”, copiados sem alterações para consulta durante as aulas.

| Original | Versão utilizada nos notebooks |
| --- | --- |
| [config.py](config.py) | [polinomial/config.py](../../src/polinomial/config.py), com caminhos do módulo |
| [modelos.py](modelos.py) | [polinomial/modelos.py](../../src/polinomial/modelos.py), com pipelines, validação cruzada e GridSearchCV |
| [graficos.py](graficos.py) | [polinomial/graficos.py](../../src/polinomial/graficos.py), com métricas, coeficientes e resíduos |
| [auxiliares.py](auxiliares.py) | [polinomial/auxiliares.py](../../src/polinomial/auxiliares.py), com a tabela de coeficientes |

As três bases fornecidas estão em `../../dados/`. Os originais desta pasta são referências; os notebooks devem importar o pacote `polinomial` de `src/`.

As adaptações mantêm as interfaces da aula. Na versão utilizada, os erros aparecem positivos nos gráficos e as tabelas preservam colunas numéricas. O exemplo sintético inicial tem sua função própria, `treinar_e_validar_modelo_polinomial`.
