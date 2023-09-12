import seaborn as sns
import matplotlib.pyplot as plt
from typing import *
import missingno as msno
import pandas as pd
from sklearn.metrics import confusion_matrix


class PlotDrawer():
    def __init__(self):
        pass
    
    def draw_missings(self, data: pd.DataFrame, figsize=Tuple[int, int], title=None)->plt.Figure:
        ax = msno.matrix(data, figsize=figsize)

        fig = ax.get_figure()

        if not title is None:
            fig.suptitle(title)
        
        plt.show()
        return fig
    
    def draw_plots(self, series: List[pd.Series], labels: List[str], figsize=(12, 8), title:str=None)->plt.Figure:
        fig, ax = plt.subplots(figsize=figsize)

        for i, data in enumerate(series):
            ax.plot(data, label=labels[i])
        
        if not title is None:
            fig.suptitle(title)
        
        ax.legend()

        plt.show()
        return fig
    
    def draw_boxplot(self, x: pd.Series, y: pd.Series, data: pd.DataFrame, title:str=None)->plt.Figure:
        ax = sns.boxplot(x=x, y=y, data=data)

        fig = ax.get_figure()
        if not title is None:
            fig.suptitle(title)
        
        plt.show()
        return fig

    def draw_confusion_matrix(self, true_labels: pd.Series, predicted_labels: pd.Series, title:str=None)->plt.Figure:
        unique_values = true_labels.unique()
        ax = sns.heatmap(data=confusion_matrix(true_labels, predicted_labels), annot=True, fmt="d", cbar=False, xticklabels=unique_values, yticklabels=unique_values)

        if not title is None:
            plt.title(title)

        fig = ax.get_figure()
        plt.show()
        return fig
    
    def draw_plots_table(self, rows: int, cols: int, figsize: Tuple[int, int], data_list: List[pd.DataFrame], plot_fn: Callable,
                         x_data: pd.Series=None,
                         y_list: List[pd.Series]=None, 
                         xticklabels=None, 
                         labels=None,
                         title=None):
        fig, axes = plt.subplots(rows, cols, figsize=figsize)

        axes = axes.flatten()
        
        for i in range(rows * cols):
            if x_data is None:
                plot_fn(data=data_list[i], ax=axes[i])
            else:
                plot_fn(x=x_data, y=y_list[i], data=data_list[i], ax=axes[i])
            
            if not xticklabels is None:
                axes[i].set_xticklabels(xticklabels)

            if not labels is None:
                axes[i].set_xlabel(labels[i])
        
        if not title is None:
            fig.suptitle(title)

        plt.tight_layout()
        plt.show()
        return fig
