import json

from core import arguments


def export_issues(issues: list[dict]):
    if arguments.output:
        with open(arguments.output, 'w') as file:
            if arguments.json:
                json.dump(issues, file, indent=2)
            else:
                file.write(str(issues))
        file.close()
        print(f'Issues saved to {arguments.output}')
    elif arguments.json:
        print(json.dumps(issues))
    else:
        print(issues)
