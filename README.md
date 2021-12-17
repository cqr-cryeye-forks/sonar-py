# sonar-py
Small adapter for <a href="https://github.com/shijl0925/python-sonarqube-api">shijl0925/python-sonarqube-api</a> for using library as script

## How it works
Script has this logic:  
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
                        Target SonarQube project
  -s SCAN, --scan SCAN  Scan folder for analyzing. Default is this script
                        folder
  -o OUTPUT, --output OUTPUT
                        Output file for data
  -j, --json            Data as json
  -d, --delete          Remove project in the end
```