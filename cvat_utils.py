import requests
import json


CVAT_API_URL = 'https://app.cvat.ai/api/'


def cvat_login(username: str, email: str, password: str):
    login_data = {
        "username": username,
        "email": email,
        "password": password
    }

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(f'{CVAT_API_URL}auth/login', headers=headers, json=login_data)

    if response.status_code == 200:
        api_token = response.json()['key']
    else:
        raise ValueError(f"Cvat login failed with error {response.status_code}: {response.text}")
    
    return api_token


def create_cvat_task(api_token, project_id: int, task_name: str):
    headers = {
        'Authorization': f'Token {api_token}',
        'Content-Type': 'application/json',
    }

    task_data = {
        'project_id': project_id,
        'name': task_name,
        'mode': 'annotation',
        'owner': '',
    }

    request_data = json.dumps(task_data, indent=4)

    response = requests.post(f'{CVAT_API_URL}tasks', headers=headers, data=request_data)

    if response.status_code == 201:
        task_id = response.json()['id']
    else:
        raise ValueError(f"Failed to create Cvat task with {response.status_code}: {response.text}")

    return task_id
