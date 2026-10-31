"""Pipelines e avaliação com as transformações dentro da validação cruzada."""
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

RANDOM_STATE = 42


def construir_pipeline_polinomial(grau=2, regressor=None):
    """Expande as variáveis e padroniza antes de ajustar o regressor."""
    return Pipeline([
        ("polynomial_features", PolynomialFeatures(degree=grau, include_bias=False)),
        ("standard_scaler", StandardScaler()),
        ("reg", LinearRegression() if regressor is None else regressor),
    ])


def treinar_e_validar_modelo_regressao(
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
