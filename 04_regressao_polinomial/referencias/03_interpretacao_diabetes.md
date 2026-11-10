# Diabetes: leitura detalhada dos resultados

> **Registro histórico:** estes resultados pertencem à grade anterior de 180 candidatos, sem expansão polinomial. O notebook agora testa 540 candidatos com graus 1, 2 e 3 e precisa ser reexecutado para gerar os resultados da nova configuração.

Execução completa salva em **09/11/2026**, no notebook [03_base_diabetes.ipynb](../notebooks/03_base_diabetes.ipynb). Os números abaixo descrevem essa execução; se alterar a base, a grade ou as divisões, recalcule as tabelas antes de usar esta interpretação.

## 1. O erro e a execução

O erro salvo era `NameError: name 'plt' is not defined`. O alias `plt` é criado por `import matplotlib.pyplot as plt`. Após reiniciar o kernel, as células anteriores precisam ser executadas novamente. A análise foi executada desde o início em um kernel novo do ambiente `machine_learn`, com resultados e figuras gravados no notebook.

Os imports locais usam `polinomial`. A primeira célula encontra `04_regressao_polinomial/src` e coloca essa pasta no caminho de importação do Python.

## 2. Como ler os dados

A base possui **442 observações** e **10 variáveis explicativas**, além de `target`. O alvo é uma medida quantitativa da base Diabetes; o modelo aprende a prever essa medida numérica.

- `df.head()` mostra algumas linhas; não é uma avaliação do modelo.
- `df.info()` descreve tipos e preenchimento das colunas.
- `X = df.drop(columns="target")` separa as entradas.
- `y = df["target"]` separa a resposta.
- Os gráficos de dispersão mostram uma variável de cada vez. O ajuste multivariado considera todas simultaneamente.

## 3. Os pré-processamentos

**Somente categóricas:** aplica OrdinalEncoder e OneHotEncoder e preserva a escala das variáveis numéricas.

**Simples:** codifica as categorias e padroniza as oito variáveis numéricas. Foi a estratégia escolhida pela busca inicial.

**Completo:** aplica Box-Cox, com padronização da saída, a IMC, LDL, HDL e colesterol total; usa StandardScaler nas outras quatro numéricas e codifica as categorias.

Os parâmetros de transformação são aprendidos dentro do treino de cada divisão. Assim, médias, desvios e parâmetros de Box-Cox não recebem informação da divisão usada para avaliar.

## 4. Os 180 candidatos

A grade combina 6 valores de alpha, 5 valores de l1_ratio, 3 pré-processadores e 2 opções para transformar o alvo. São **180 configurações**, cada uma avaliada em 5 divisões: **900 ajustes de validação** na busca inicial, além do reajuste do vencedor.

A avaliação aninhada faz outras cinco buscas, usando somente o treino de cada divisão externa: são mais **4.500 ajustes internos de validação**. As referências são avaliadas nas mesmas divisões externas.

## 5. A configuração escolhida na busca inicial

- **alpha = 0,01:** força de regularização pequena entre os valores testados. Foi o menor valor da grade; a busca não verificou valores abaixo dele.
- **l1_ratio = 0,9:** maior peso da penalização L1 na mistura. Isso não significa eliminar 90% das variáveis. Neste ajuste, nenhum dos dez coeficientes foi exatamente zero.
- **Pré-processamento simples:** categorias codificadas e variáveis numéricas padronizadas.
- **transformer = None:** o alvo permaneceu na escala original.

`FunctionTransformer(validate=True)` aparece em `transformer_` porque TransformedTargetRegressor usa uma identidade internamente quando nenhuma transformação foi solicitada.

O ajuste final convergiu em **385 iterações**. O limite foi aumentado para 100.000 para dar tempo aos outros candidatos da grade.

## 6. Por que o score é negativo

`best_score_ = -54,644798` usa a métrica `neg_root_mean_squared_error`. O scikit-learn escolhe o maior score; maximizar o RMSE negativo equivale a minimizar o RMSE positivo. Portanto, o erro correspondente é **54,644798 unidades do alvo**.

Esse valor não é porcentagem de erro nem o erro de toda previsão individual. RMSE agrega erros quadráticos e dá mais peso aos maiores desvios.

## 7. Comparação exploratória e avaliação externa

A comparação exploratória reproduz a lógica da aula: escolhe parâmetros usando todos os dados e avalia esse candidato nas mesmas divisões. Nela, o RMSE foi **54,6448** no ElasticNet e **54,6456** na regressão linear. A diferença de **0,0008** é muito pequena.

Esse score participou da escolha do modelo. Para avaliar a própria seleção, foi acrescentada validação cruzada aninhada: em cada divisão externa, todos os parâmetros são escolhidos novamente usando somente os dados de treino disponíveis.

**Resultados externos:**

| Modelo | R² médio | MAE médio | RMSE médio |
| --- | ---: | ---: | ---: |
| DummyRegressor | -0.0194 | 65.979 | 77.193 |
| LinearRegression | 0.4825 | 44.107 | 54.646 |
| ElasticNet_busca_aninhada | 0.4697 | 44.742 | 55.244 |

O RMSE médio do ElasticNet ficou **28.43%** abaixo do DummyRegressor. A diferença entre o RMSE médio da regressão linear e o do ElasticNet foi **-0.599**; positiva favorece ElasticNet, negativa favorece regressão linear. A tabela por divisão no notebook mostra a consistência desse resultado.

A escolha externa pode diferir da escolha feita na busca com todos os dados. Isso é esperado porque cada busca recebe uma amostra de treino diferente.

### Diferenças entre as divisões externas

| Divisão | RMSE linear | RMSE ElasticNet | Configuração interna do ElasticNet |
| --- | ---: | ---: | --- |
| 1 | 53,868 | 53,629 | alpha 0,05; l1_ratio 0,10; alvo original |
| 2 | 51,570 | 51,611 | alpha 0,01; l1_ratio 0,90; alvo original |
| 3 | 56,820 | 60,066 | alpha 0,10; l1_ratio 0,10; alvo transformado |
| 4 | 52,650 | 52,728 | alpha 0,10; l1_ratio 0,75; alvo original |
| 5 | 58,319 | 58,189 | alpha 0,01; l1_ratio 0,75; alvo original |

O ElasticNet teve RMSE menor em duas das cinco divisões e maior nas outras três. A terceira divisão apresentou a maior diferença, aproximadamente 3,245 pontos de RMSE. Foi também a divisão em que a busca interna escolheu transformar o alvo. Essa coincidência ajuda a investigar o resultado, mas não isola a transformação como causa do desempenho.

Todos os vencedores internos usaram o pré-processamento simples. Alpha e l1_ratio variaram entre as amostras. O menor valor de alpha foi escolhido em duas divisões, e o maior valor de l1_ratio em uma. Isso mostra que a escolha inicial 0,01/0,9 não foi repetida de forma uniforme.

Nesta execução, a regressão linear apresentou RMSE médio cerca de 0,599 ponto menor e exigiu menos tempo de ajuste. Essa diferença é pequena em relação à variação entre divisões; o resultado sustenta tratar regressão linear como uma referência competitiva, sem afirmar superioridade estatística.

## 8. Como interpretar cada métrica

- **R²:** compara o erro quadrático com o de prever a média no conjunto avaliado. Um R² perto de 0,48 representa uma redução aproximada de 48% nesse erro relativo, em média entre divisões; não significa acertar 48% das previsões. Pode ser negativo quando o modelo é pior que essa referência.
- **MAE:** média das magnitudes dos erros. É expresso na mesma unidade do alvo.
- **RMSE:** raiz da média dos erros quadráticos. Também está na unidade do alvo e cresce mais quando há erros grandes.
- **Desvio entre divisões:** mede variação do resultado entre amostras de avaliação. Não é intervalo de confiança nem comprovação de superioridade de um modelo.
- **Tempo:** no ElasticNet aninhado inclui a busca interna; nas referências não há essa busca.

A coluna `std_test_*` de GridSearchCV usa desvio populacional (`ddof=0`). A tabela resumida com `groupby().std()` usa desvio amostral (`ddof=1`). Por isso, as duas formas de resumir os mesmos cinco valores podem apresentar desvios diferentes.

O DummyRegressor usa a média do treino. Como essa média difere da média de cada divisão avaliada, seu R² pode ficar ligeiramente negativo.

## 9. Cada coeficiente do modelo reajustado

Coeficientes descrevem associações condicionais do modelo ajustado em todos os dados da busca inicial. Para as variáveis numéricas do pipeline simples, a unidade transformada corresponde a um desvio padrão do treino.

| Variável transformada | Coeficiente | Leitura |
| --- | ---: | --- |
| `standard_scaler__colesterol_total` | -29.817 | Um desvio padrão a mais nesta variável associa-se a uma redução da previsão, condicionada às outras entradas. A correlação com outras medidas de colesterol influencia o sinal. |
| `one_hot_encoder__sexo_2` | -22.809 | Diferença ajustada entre a categoria 2 e a categoria 1 de sexo. O código do dataset não deve ser interpretado como uma escala numérica contínua. |
| `standard_scaler__idade` | -0.583 | Efeito por um desvio padrão na idade. A magnitude é pequena neste ajuste com as demais variáveis presentes. |
| `standard_scaler__hdl` | +0.221 | Efeito por um desvio padrão em HDL. O coeficiente é pequeno, mas não foi exatamente zerado. |
| `standard_scaler__glicose` | +3.468 | Efeito por um desvio padrão na variável glicose, mantendo as demais entradas constantes. |
| `ordinal_encoder__colesterol_hdl_cat` | +8.661 | Efeito por um passo na codificação ordinal: 0 para 2-3, 1 para 4-5 e 2 para 6+. O encoder impõe passos numéricos igualmente espaçados. |
| `standard_scaler__pressao_media` | +15.148 | Efeito por um desvio padrão na pressão média. |
| `standard_scaler__ldl` | +17.489 | Efeito por um desvio padrão em LDL. Variáveis correlacionadas podem redistribuir os pesos de medidas relacionadas. |
| `standard_scaler__imc` | +24.731 | Efeito por um desvio padrão em IMC. |
| `standard_scaler__triglicerides` | +33.133 | Efeito por um desvio padrão na coluna chamada triglicerides da base fornecida. |

Os valores não são efeitos causais. As variáveis contínuas padronizadas, a categoria ordinal e o indicador de sexo têm escalas diferentes; suas magnitudes não constituem um ranking geral de importância.

O intercepto é **156,310255**: é a previsão na origem das entradas transformadas. Neste pipeline, a referência combina valores numéricos nas médias de treino, nível ordinal 0 e a categoria removida de sexo. Ele não precisa ser igual à média de `target`.

## 10. O que os atributos significam

| Atributo | Leitura |
| --- | --- |
| `best_params_` | Parâmetros selecionados pela busca |
| `best_score_` | Média do score de validação do candidato vencedor |
| `best_estimator_` | Pipeline completo reajustado depois da seleção |
| `regressor_` | Pipeline interno já ajustado |
| `regressor_["preprocessor"]` | Pré-processador ajustado e seus parâmetros de transformação |
| `regressor_["reg"]` | ElasticNet ajustado, seus coeficientes e intercepto |
| `transformer_` | Transformação ajustada do alvo; identidade quando não houve transformação |
| `get_feature_names_out()` | Ordem e nomes exatos das colunas transformadas |
| `cv_results_` | Resultados dos candidatos e de cada divisão interna |

## 11. Como ler os gráficos

No gráfico de coeficientes, o sinal define a direção da associação; a distância ao zero mostra a magnitude na escala da respectiva variável transformada.

Nos boxplots de métricas, cada modelo tem cinco resultados externos. A linha central é a mediana; a caixa cobre a região entre o primeiro e o terceiro quartis. Os bigodes seguem a regra de 1,5 intervalo interquartil, e pontos externos podem aparecer individualmente. O marcador adicional indica a média. Caixas sobrepostas e médias próximas não sustentam, por si, uma conclusão de superioridade.

## 12. Próximos experimentos

- Examinar uma faixa de alpha abaixo de 0,01, mantendo uma avaliação externa para medir a nova seleção.
- Testar uma expansão polinomial em um pipeline e comparar seu custo e sua generalização.
- Investigar resíduos e estabilidade dos coeficientes entre divisões.

A expansão polinomial ainda não foi aplicada nesta análise da base Diabetes.
