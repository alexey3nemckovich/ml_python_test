import os
import seaborn as sns
from plot_drawer import PlotDrawer
import pandas as pd
from imblearn.under_sampling import RandomUnderSampler


def save_figures(folder_path, figures_info):
    filepaths = []

    for i, figure_info in enumerate(figures_info):
        filepaths.append(f'{folder_path}/{figure_info[1]}')
        figure_info[0].savefig(filepaths[i])
    
    return filepaths


def draw_plots(filepath, save_folder_path):
    if not os.path.exists(save_folder_path):
        try:
            os.makedirs(save_folder_path)
        except OSError as e:
            print('Failed to create dir for plots!')
            return
    
    plot_drawer = PlotDrawer()
    
    data = pd.read_json(filepath)

    missings_fig = plot_drawer.draw_missings(
        data, 
        figsize=(10,5), 
        title="Dataset missings");
    
    corners_counts_confusion_matrix_fig = plot_drawer.draw_confusion_matrix(
        data.gt_corners, 
        data.rb_corners, 
        title="Corners counts confusion matrix");
    
    deviations_histplots_fig = plot_drawer.draw_plots_table(
        rows=2, 
        cols=3, 
        figsize=(15, 7),
        plot_fn=sns.histplot,
        data_list=[data['floor_min'], data['floor_mean'], data['floor_max'], data['ceiling_min'], data['ceiling_mean'], data['ceiling_max']],
        labels=['Floor min deviations', 'Floor mean deviations', 'Floor max deviations', 'Ceiling min deviations', 'Ceiling mean deviations', 'Ceiling max deviations'],
        title='Histograms for floor/ceiling deviations for different counts of corners');
    
    deviations_boxplots_fig = plot_drawer.draw_plots_table(
        rows=1, 
        cols=3, 
        figsize=(12, 4),
        plot_fn=sns.boxplot,
        data_list=[data[['floor_min', 'ceiling_min']], data[['floor_mean', 'ceiling_mean']], data[['floor_max', 'ceiling_max']]],
        xticklabels=['floor', 'ceiling'],
        labels=['Min deviations', 'Mean deviations', 'Max deviations'],
        title='Boxplots for floor/ceiling deviations');

    corners_deviations_boxplots_fig = plot_drawer.draw_plots_table(
        rows=2, 
        cols=3, 
        figsize=(15, 7),
        plot_fn=sns.boxplot,
        x_data=data['gt_corners'], 
        y_list=[data['floor_min'], data['floor_mean'], data['floor_max'], data['ceiling_min'], data['ceiling_mean'], data['ceiling_max']], 
        data_list=[data, data, data, data, data, data],
        labels=['Floor min deviations', 'Floor mean deviations', 'Floor max deviations', 'Ceiling min deviations', 'Ceiling mean deviations', 'Ceiling max deviations'],
        title='Boxplots for floor/ceiling deviations for different counts of corners');
    
    X = data[data['gt_corners'] != 10].drop(['name', 'gt_corners', 'rb_corners'], axis=1)
    y = data[data['gt_corners'] != 10]['gt_corners']

    undersampler = RandomUnderSampler(random_state=42)

    X_resampled, y_resampled = undersampler.fit_resample(X, y)

    undersampled_corners_deviations_boxplots_fig = plot_drawer.draw_plots_table(
        rows=2, 
        cols=3, 
        figsize=(15, 7),
        plot_fn=sns.boxplot,
        x_data=y_resampled, 
        y_list=[X_resampled['floor_min'], X_resampled['floor_mean'], X_resampled['floor_max'], X_resampled['ceiling_min'], X_resampled['ceiling_mean'], X_resampled['ceiling_max']], 
        data_list=[X_resampled, X_resampled, X_resampled, X_resampled, X_resampled, X_resampled],
        labels=['Floor min deviations', 'Floor mean deviations', 'Floor max deviations', 'Ceiling min deviations', 'Ceiling mean deviations', 'Ceiling max deviations'],
        title='Boxplots for floor/ceiling deviations for different counts of corners after undersampling');
    
    mean_deviation_boxplot_fig = plot_drawer.draw_boxplot(
        x=data.gt_corners, 
        y=data['mean'], 
        data=data, 
        title="Mean deviation by count of corners");

    floor_ceiling_mean_deviation_trends_fig = plot_drawer.draw_plots(
        [data.groupby(by=data.gt_corners)['ceiling_mean'].median(), data.groupby(by=data.gt_corners)['floor_mean'].median()], 
        figsize=(7, 5), 
        labels=['Ceiling mean', 'Floor mean'],
        title="Mean deviation trend with corners count");

    figures_data = [
        (missings_fig, 'data_missings.jpg'),
        (corners_counts_confusion_matrix_fig, 'corners_counts_confusion_matrix.jpg'),
        (deviations_histplots_fig, 'deviations_histplots.jpg'),
        (deviations_boxplots_fig, 'deviations_boxplots.jpg'),
        (corners_deviations_boxplots_fig, 'corners_deviations_boxplots.jpg'),
        (undersampled_corners_deviations_boxplots_fig, 'undersampled_corners_deviations_boxplots.jpg'),
        (mean_deviation_boxplot_fig, 'mean_deviation_boxplot.jpg'),
        (floor_ceiling_mean_deviation_trends_fig, 'floor_ceiling_mean_deviation_trends.jpg'),
    ]

    return save_figures(save_folder_path, figures_data);
