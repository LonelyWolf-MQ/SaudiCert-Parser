# Saudi CERT Parser
A tool that parse security alerts notified by ![SaudiCERT](https://cert.gov.sa/) and converts them into multi formats (JSON, CSV, TXT).

## To run the project what you need is:
- Having python3.
- Install the requirements ```pip3 install -r requirements.txt```.
- Run: ```python3 main.py -h```

### CSV:
- URL: ```python3 main.py -u https://cert.gov.sa/en/security-warnings/*  -f csv -o example.csv```
- List of URL: ```python3 main.py -l urls_example.txt -f csv -o example.csv```

### JSON:
- URL: ```python3 main.py -u https://cert.gov.sa/en/security-warnings/*  -f json -o example.json```
- List of URL: ```python3 main.py -l urls_example.txt -f json -o example.json```
 
### TEXT:
- URL: ```python3 main.py -u https://cert.gov.sa/en/security-warnings/*  -f text```
- List of URL: ```python3 main.py -l urls_example.txt -f text```

## Future work
- Add more extensions/formats.
- Add some functionalities for automation tasks that could be used by Cybersecurity/IT departments.

## NOTE:
You may face problems in some alerts because of the html tags of the website.

if you noticed any mistake or have any suggestion reached me at my Twitter/LinkedIn account:
- [![Twitter](https://img.shields.io/twitter/follow/MHMDQi?style=social)](https://twitter.com/intent/follow?screen_name=MHMDQi)
- [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mhmdqi/)
