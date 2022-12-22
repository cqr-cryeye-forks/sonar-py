import json

import requests


def get_results(project: dict, token: str, sonar_url: str) -> (dict, list):
    session = requests.Session()
    session.auth = (token, '')
    results = {}
    data_link = f"{sonar_url}/api/issues/search?componentKeys={project['key']}&ps=1"
    
    # data_link = f"{sonar_url}/api/issues/search?resolved=false&id={project['key']}"
    link_data = session.get(url=data_link)
    errors = []
    if link_data.status_code == 200:
        results = json.loads(link_data.content.decode())
    else:
        print(f"Error getting data. Status code: {link_data.status_code}")
        errors.append(f"Error getting data. Status code: {link_data.status_code}")
    return results, errors
