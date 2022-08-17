import re
import argparse
import requests
from bs4 import BeautifulSoup
from urlparsing import *
from save_output import * 

Mainsubject = []
WarningDate = []
SeverityLevel = []
Warningnumber = []
targetsector = []
Description = []
Threats = []
Preventiveprocedures = []
AlertURL = []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url',metavar="https://cert.gov.sa/en/security-warnings/*",help="Alert URL")
    parser.add_argument('-l','--listurl', type=open, help="List of URL Alerts (Seperated By Line)")
    parser.add_argument('-o','--output', type=argparse.FileType('w', encoding='latin-1'), help="Output")
    parser.add_argument('-f','--format', required=True, choices=['text','json','csv'])
    args = parser.parse_args()
    urlregex = r"https://cert.gov.sa/en/security-warnings/.*"
    url = args.url
    fileformat = args.format
    if (fileformat == "json" and re.search(r".*\.json",args.output.name)) or (fileformat == "csv" and re.search(r".*\.csv",args.output.name)) or (fileformat == "text"):
        if url and re.search(urlregex,url):
            parseUrl(url,fileformat)
            if fileformat == "json" or fileformat == "csv":
                convertor(Mainsubject,WarningDate,SeverityLevel,Warningnumber,targetsector,Description,Threats,Preventiveprocedures,AlertURL,args.output.name,fileformat)
            else:
                pass
        elif args.listurl.name:
            with open(args.listurl.name) as fp:
                while True:
                    line = fp.readline()
                    if not line:
                        break
                    urlline = line.strip()
                    if re.search(urlregex,urlline):
                        parseUrl(urlline,fileformat)
                    else:
                        continue
            if fileformat == "json" or fileformat == "csv":
                convertor(Mainsubject,WarningDate,SeverityLevel,Warningnumber,targetsector,Description,Threats,Preventiveprocedures,AlertURL,args.output.name,fileformat)
            else:
                pass
    else:
        print("File Format Doesn't Match The Output File Extension")
        

def parseUrl(url,fileformat):
    session = requests.Session()
    response = session.get(url)
    parsed_html = BeautifulSoup(response.content, "html.parser")
    print(parsed_html)
    for tag in parsed_html.find_all("script"):
        tag.decompose()
    for tag in parsed_html.find_all("style"):
        tag.decompose()
    ParTagResp = parsed_html.findAll("p")
    SpanTagResp = parsed_html.findAll("span")
    h4TagResp = parsed_html.find("h4")
    main = mainSubject(h4TagResp)
    warndate = warningDate(ParTagResp)
    lvl = level(ParTagResp)
    warn = warningNumber(ParTagResp)
    trgt = targetSector(parsed_html)
    desc = description(parsed_html)
    threat = threats(parsed_html)
    prvnt = preventiveProcedures(parsed_html)
    Mainsubject.append(main)
    WarningDate.append(warndate)
    SeverityLevel.append(lvl)
    Warningnumber.append(warn)
    targetsector.append(trgt)
    Description.append(desc)
    Threats.append(threat)
    Preventiveprocedures.append(prvnt)
    AlertURL.append(url)

    if fileformat == "text":
        print("==============================")
        print("Warning Title: \n", main)
        print("Warning Date: \n", warndate)
        print("Severity Level: \n", lvl)
        print("Warning Number: \n", warn)
        print("Target Sector: \n", trgt)
        print("Description: \n", desc)
        print("Threats: \n", threat)
        print("Best practice and Recommendations: \n", prvnt)
        print("URL Reference \n", url)
        print("==============================")


if __name__ == '__main__':
    main()
