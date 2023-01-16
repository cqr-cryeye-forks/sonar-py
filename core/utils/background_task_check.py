import json
from time import sleep

import requests


def wait_until_all_background_tasks_finish(project: dict, token: str, sonar_url: str) -> list[str]:
    errors = []
    _is_no_background_tasks = False
    print('Check if all background tasks finished')
    while not _is_no_background_tasks:
        session = requests.Session()
        session.auth = (token, '')
        link_data = session.get(url=f"{sonar_url}/api/ce/component?component={project['key']}")
        if link_data.status_code == 200:
            results = json.loads(link_data.content.decode())
            tasks = results.get("queue", [])
            for task in tasks:
                if task.get("componentKey", "") == project['key']:
                    status = task.get("status", "Unknown")
                    print(f'Background task exist. '
                          f'Id: {task.get("id", "N/A")} '
                          f'Type: {task.get("type", "N/A")} '
                          f'Status: {status} '
                          f'Submitted at: {task.get("submittedAt", "N/A")}'
                          )
                    if status == "FAILED":
                        errors.append(
                            f"{task.get('errorType', 'Message')}: {task.get('errorMessage', 'Unknown error')}")
                        print('Background task finished. Exiting')
                        _is_no_background_tasks = True
                    # if status in ["SUCCESS", "FAILED"]:
                    #     print('Background task finished. Exiting')
                    #     errors = task.get("errorMessage", None)
                    #     _is_no_background_tasks = True
            if not tasks:
                print('No background tasks. Go to getting results')
                _is_no_background_tasks = True
        else:
            message = f"Error getting data. Status code: {link_data.status_code}. Background tasks check failed"
            print(message)
            errors.append(message)
            _is_no_background_tasks = True
        if not _is_no_background_tasks:
            # print('Sleep for 30 sec')
            sleep(30)
    return errors
