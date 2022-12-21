# sonar-py
This tool allows you to automate tasks with SonarQube or add it to your pipeline. It will connect with SonarQube API and use local sonar-client app for scanning selected folder.

For connecting with SonarQube tool uses <a href="https://github.com/shijl0925/python-sonarqube-api">shijl0925/python-sonarqube-api</a>.

## How it works
Script logic is:  
1) get existing project or create new if not found
2) Generate configuration file if needed
3) Run local program (sonar-scaner) for starting analyzing
4) Get founded issues from API
5) Print or save founded data
6) Delete project if needed

## Usage
```angular2html
usage: sonar.py [-h] [-u URL] [-l LOGIN] [-p PASSWORD] [-t TOKEN] [-n PROJECT]
                [-s SCAN] [-o OUTPUT] [-j] [-d]

SonarQube API adapter

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     SonarQube link. Default is http://localhost:9000
  -l LOGIN, --login LOGIN
                        SonarQube login
  -p PASSWORD, --password PASSWORD
                        SonarQube password
  -t TOKEN, --token TOKEN
                        SonarQube token
  -n PROJECT, --project PROJECT
                        Target SonarQube project. If not selected - tool will generate new.
  -s SCAN, --scan SCAN  Scan folder for analyzing. Default is this script
                        folder
  -o OUTPUT, --output OUTPUT
                        Output file for data
  -j, --json            Data as json
  -d, --delete          Remove project in the end
  -r, --remove_old      Remove other generated projects before run
  -dt DELETE_TIME, --delete-time DELETE_TIME
                        Days that other generated project will be kept.
                        Default 30
```