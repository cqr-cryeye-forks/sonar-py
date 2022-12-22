import json

from core import arguments


def export_issues(issues: list[dict], errors: list[str], scan_data: dict):
    data = {
        'issues': issues,
        'errors': errors,
        'scan_data': scan_data,
    }
    if arguments.output:
        with open(arguments.output, 'w') as file:
            if arguments.json:
                json.dump(data, file, indent=2)
            else:
                file.write(str(data))
        file.close()
        print(f'Issues saved to {arguments.output}')
    elif arguments.json:
        print(json.dumps(data))
    else:
        print(data)
