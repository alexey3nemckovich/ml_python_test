if __name__ == '__main__':
    import argparse
    from cvat_utils import cvat_login, create_cvat_task


    # Create a parser
    parser = argparse.ArgumentParser(description="Get some hyperparameters.")

    # Get an arg for username
    parser.add_argument("--username",
                        default="alex391",
                        type=str,
                        help="Cvat user account name")

    # Create an arg for user email
    parser.add_argument("--email",
                        default="alexey3nemckovich@gmail.com",
                        type=str,
                        help="Cvat user account email")

    # Create an arg for password
    parser.add_argument("--password",
                        default="123123123zZ",
                        type=str,
                        help="Cvat user account password")
    
    # Create an arg for project id
    parser.add_argument("--project_id",
                        default=57958,
                        type=int,
                        help="Cvat project id")

    # Create an arg for task name
    parser.add_argument("--task_name",
                        default='My Task 3',
                        type=str,
                        help="Name for new Cvat task")

    # Get our arguments from the parser
    args = parser.parse_args()

    # Setup hyperparameters
    USERNAME = args.username
    EMAIL = args.email
    PASSWORD = args.password
    PROJECT_ID = args.project_id
    TASK_NAME = args.task_name

    print(
        f"[INFO] Creating CVAT task with parameters: \r\n"
        f"\tusername={USERNAME}\r\n"
        f"\temail={EMAIL}\r\n"
        f"\tpassword={PASSWORD}\r\n"
        f"\tproject_id={PROJECT_ID}\r\n"
        f"\ttask_name={TASK_NAME}\r\n")
    
    try:
        task_id = create_cvat_task(cvat_login(USERNAME, EMAIL, PASSWORD), PROJECT_ID, TASK_NAME)
        print(f'Cvat task with id {task_id} was successfully created!')
    except ValueError as e:
        print(e)
