
# ML python test project

We have dataset of 1347 corners deviations for different rooms. This project helps to estimate model quality based on data provided.

## Installing dependencies:

To install dependencies for this project you can use command line **pip install -e .**

## Generating plots:

To get generate plots you can use script **'./generate_plots.py'**

### Example of execution:
````
  (venv) alex@alex-pc:~/projects/ml/ml_python_test$ python ./generate_plots.py
````
Generating plots...
Plots were successfully saved to the folder './plots'.
File paths:
['./plots/data_missings.jpg', './plots/corners_counts_confusion_matrix.jpg', './plots/deviations_histplots.jpg', './plots/deviations_boxplots.jpg', './plots/corners_deviations_boxplots.jpg', './plots/undersampled_corners_deviations_boxplots.jpg', './plots/mean_deviation_boxplot.jpg', './plots/floor_ceiling_mean_deviation_trends.jpg']

## Creating Cvat.ai task:

To create Cvat.ai task you can use script **'./create_cvat_task.py'**

### Example of execution:
````
  (venv) alex@alex-pc:~/projects/ml/ml_python_test$ python ./create_cvat_task.py
````
[INFO] Creating CVAT task with parameters: 
        username=alex391
        email=alexey3nemckovich@gmail.com
        password=123123123zZ
        project_id=57958
        task_name=My Task 3

Cvat task with id 302577 was successfully created!

## Scripts usage information:
#### create_cvat_task.py

usage: create_cvat_task.py [-h] [--username USERNAME] [--email EMAIL] [--password PASSWORD] [--project_id PROJECT_ID] [--task_name TASK_NAME]

Get some hyperparameters.

options:
  -h, --help            show this help message and exit<br>
  --username USERNAME   Cvat user account name<br>
  --email EMAIL         Cvat user account email<br>
  --password PASSWORD   Cvat user account password<br>
  --project_id PROJECT_ID Cvat project id<br>
  --task_name TASK_NAME Name for new Cvat task

