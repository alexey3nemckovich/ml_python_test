if __name__ == '__main__':
    from plot_utils import draw_plots
    import warnings

    warnings.simplefilter(action='ignore', category=FutureWarning)
    warnings.simplefilter(action='ignore', category=UserWarning)

    FOLDER_PATH = './plots'
    DATASET_FILEPATH = './deviation.json'

    print("Generating plots...")

    filepaths = draw_plots(DATASET_FILEPATH, FOLDER_PATH)

    print(
        f"Plots were successfully saved to the folder '{FOLDER_PATH}'.\r\n"
        f'File paths:\r\n'
        f'{filepaths}')
