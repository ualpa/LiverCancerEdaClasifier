import matplotlib.pyplot as plt
import pandas as pd

def boxplot(data: pd.DataFrame):
    figure, axes = plt.subplots(4, 1, figsize = (8, 10))
    figure.suptitle("Variables boxplots", fontsize = 16)
    for ax, col in zip(axes, data.columns):
        ax.boxplot(data[col], vert = False)
        ax.set_ylabel(col)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
