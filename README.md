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
