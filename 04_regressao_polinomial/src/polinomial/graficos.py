"""Visualizações dos resultados da validação cruzada."""
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import PredictionErrorDisplay


def plot_comparar_metricas_modelos(df_resultados):
    # Aceita tanto resultados organizados quanto os nomes de scoring usados na aula.
    df_resultados = df_resultados.copy()
    for erro, coluna in [
        ("MAE", "test_neg_mean_absolute_error"),
        ("RMSE", "test_neg_root_mean_squared_error"),
    ]:
        if erro not in df_resultados:
            df_resultados[erro] = -df_resultados[coluna]
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    metricas = [
        ("test_r2", "R²"), ("MAE", "MAE"),
        ("RMSE", "RMSE"), ("time_seconds", "Tempo (s)"),
    ]
    for ax, (metrica, titulo) in zip(axs.flat, metricas):
        sns.boxplot(data=df_resultados, x="model", y=metrica, showmeans=True, ax=ax)
        ax.set(title=titulo, xlabel="Modelo", ylabel=titulo)
        ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    plt.show()


def plot_coeficientes(df_coefs, tituto="Coeficientes"):
    """Mantém o nome do argumento da aula para aceitar as mesmas chamadas."""
    ax = df_coefs.plot.barh()
    ax.set(title=tituto, xlabel="Coeficientes")
    ax.axvline(x=0, color=".5")
    if ax.get_legend() is not None:
        ax.get_legend().remove()
    plt.tight_layout()
    plt.show()


def plot_residuos(y_true, y_pred):
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    sns.histplot(y_true - y_pred, kde=True, ax=axs[0])
    PredictionErrorDisplay.from_predictions(
        y_true=y_true, y_pred=y_pred, kind="residual_vs_predicted", ax=axs[1],
    )
    PredictionErrorDisplay.from_predictions(
        y_true=y_true, y_pred=y_pred, kind="actual_vs_predicted", ax=axs[2],
    )
    fig.tight_layout()
    plt.show()
