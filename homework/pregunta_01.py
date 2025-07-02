"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    os.makedirs("files/plots", exist_ok=True)
    
    df = pd.read_csv("files/input/news.csv", index_col=0)
    
    plt.figure(figsize=(12, 8))
    
    for column in df.columns:
        plt.plot(df.index, df[column], marker='o', linewidth=2, label=column)
    
    plt.title("News Consumption by Media Type Over Time", fontsize=16, fontweight='bold')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Consumption (%)", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    
    plt.ylim(0, None)
    
    plt.xticks(df.index[::2])
    
    plt.tight_layout()
    
    plt.savefig("files/plots/news.png", dpi=300, bbox_inches='tight')
    plt.close()


