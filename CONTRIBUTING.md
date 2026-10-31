# Padrão de commits

Use mensagens curtas em português, identificando o módulo ou notebook e a alteração:

```text
escopo: ação objetiva
```

| Alteração | Exemplo |
| --- | --- |
| README principal | `readme: atualiza apresentação` |
| Fundamentos | `fundamentos: revisa aprendizado supervisionado` |
| Validação cruzada | `regressao/08: ajusta validação cruzada` |
| Comparação com GridSearchCV | `regularizacao/02: compara modelos` |
| Notebook Ridge | `regularizacao/02a: ajusta grade Ridge` |
| Notebook Lasso | `regularizacao/02b: comenta coeficientes` |
| Notebook ElasticNet | `regularizacao/02c: ajusta l1_ratio` |
| Código compartilhado | `regularizacao/src: corrige métricas` |
| Regressão polinomial | `polinomial: adiciona experimento` |
| Projeto aplicado | `projeto: prepara dados` |
| Configuração do repositório | `repo: ajusta ambiente` |

Cada commit deve reunir uma mudança coerente. Separe alterações independentes em módulos ou notebooks diferentes. Quando a mudança for compartilhada, use o escopo do módulo ou `repo` e descreva o efeito comum.

Antes de commitar, confira os arquivos com `git status` e o conteúdo com `git diff`. Adicione somente os arquivos relacionados à mudança. Evite mensagens genéricas como “atualizações” e “alterações”.

O padrão vale para novos commits. Os históricos importados mantêm as mensagens originais.
