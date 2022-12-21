import argparse
from pathlib import Path

from config.constants import sonarqube_url


def create_parser():
    parser = argparse.ArgumentParser(description='SonarQube API adapter')
    parser.add_argument('-u', '--url', type=str, default=sonarqube_url,
                        help=f'SonarQube link. Default is {sonarqube_url}')
    parser.add_argument('-l', '--login', type=str, default=None,
                        help='SonarQube login')
    parser.add_argument('-p', '--password', type=str, default=None,
                        help='SonarQube password')
    parser.add_argument('-t', '--token', type=str, default=None,
                        help='SonarQube token')
    parser.add_argument('-n', '--project', type=str, default=None,
                        help='Target SonarQube project. If not selected - tool will generate new.')
    parser.add_argument('-s', '--scan', type=str, default=Path(__file__).parents[1],
                        help='Scan folder for analyzing. Default is this script folder')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='Output file for data')
    parser.add_argument('-j', '--json', default=False, action='store_true',
                        help='Data as json')
    parser.add_argument('-d', '--delete', default=False, action='store_true',
                        help='Remove project in the end')
    parser.add_argument('-r', '--remove-old', default=False, action='store_true',
                        help='Remove other generated projects before run')
    parser.add_argument('-dt', '--delete-time', type=int, default=30,
                        help='Days that other generated project will be kept. Default 30')
    return parser.parse_args()


arguments = create_parser()
