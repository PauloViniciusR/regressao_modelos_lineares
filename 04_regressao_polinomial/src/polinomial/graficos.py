"""Visualizações dos resultados da validação cruzada."""
import matplotlib.pyplot as plt
import seaborn as sns


def plot_comparar_metricas_modelos(df_resultados):
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
