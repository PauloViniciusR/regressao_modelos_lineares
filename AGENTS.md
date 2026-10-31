# Instruções do repositório

- Escreva documentação e comentários em português, com linguagem direta.
- Use mensagens de commit curtas no formato `escopo: ação objetiva`, conforme CONTRIBUTING.md.
- Identifique o módulo e o número do notebook quando a alteração for específica, por exemplo: `regularizacao/02b: ajusta grade Lasso`.
- Separe mudanças independentes por módulo ou notebook. Use um único commit quando os arquivos fizerem parte da mesma alteração.
- Preserve os históricos importados. Não reescreva commits antigos sem solicitação explícita do usuário.
- Use o environment.yml da raiz para o ambiente compartilhado. Os pacotes são `02_modelos_regressao/src/regressao`, `03_regularizacao/src/regularizacao` e `04_regressao_polinomial/src/polinomial`; mantenha os imports distintos.
