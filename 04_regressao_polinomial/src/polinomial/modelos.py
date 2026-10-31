"""Pipelines e avaliação com as transformações dentro da validação cruzada."""
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, KFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from .utils import organiza_resultados

RANDOM_STATE = 42


def construir_pipeline_polinomial(grau=2, regressor=None):
    """Expande as variáveis e padroniza antes de ajustar o regressor."""
    return Pipeline([
        ("polynomial_features", PolynomialFeatures(degree=grau, include_bias=False)),
        ("standard_scaler", StandardScaler()),
        ("reg", LinearRegression() if regressor is None else regressor),
    ])


def treinar_e_validar_modelo_polinomial(
    X, y, grau=2, regressor=None, n_splits=5, random_state=RANDOM_STATE,
):
    """Retorna R² e erros negativos no formato padrão do cross_validate."""
    modelo = construir_pipeline_polinomial(grau=grau, regressor=regressor)
    cv = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    return cross_validate(
        modelo, X, y, cv=cv,
        scoring=["r2", "neg_mean_absolute_error", "neg_root_mean_squared_error"],
        error_score="raise",
    )


def construir_pipeline_modelo_regressao(
    regressor, preprocessor=None, target_transformer=None,
):
    """Interface da aula para combinar pré-processamento, regressor e alvo."""
    etapas = [] if preprocessor is None else [("preprocessor", preprocessor)]
    pipeline = Pipeline([*etapas, ("reg", regressor)])
    if target_transformer is not None:
        return TransformedTargetRegressor(
            regressor=pipeline, transformer=target_transformer,
        )
    return pipeline


def treinar_e_validar_modelo_regressao(
    X, y, regressor, preprocessor=None, target_transformer=None,
    n_splits=5, random_state=RANDOM_STATE,
):
    """Avaliação genérica com os mesmos argumentos usados nos materiais da aula."""
    modelo = construir_pipeline_modelo_regressao(
        regressor, preprocessor, target_transformer,
    )
    cv = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    return cross_validate(
        modelo, X, y, cv=cv,
        scoring=["r2", "neg_mean_absolute_error", "neg_root_mean_squared_error"],
        error_score="raise",
    )


def grid_search_cv_regressor(
    regressor, param_grid, preprocessor=None, target_transformer=None,
    n_splits=5, random_state=RANDOM_STATE, return_train_score=False,
):
    """Busca da aula: seleciona a configuração com menor RMSE médio."""
    modelo = construir_pipeline_modelo_regressao(
        regressor, preprocessor, target_transformer,
    )
    cv = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    return GridSearchCV(
        modelo, param_grid=param_grid, cv=cv,
        scoring=["r2", "neg_mean_absolute_error", "neg_root_mean_squared_error"],
        refit="neg_root_mean_squared_error", n_jobs=-1,
        return_train_score=return_train_score, verbose=1, error_score="raise",
    )
