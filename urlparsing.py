import re
import html2text

def mainSubject(h4TagResp):
    name = re.findall(r"[A-Za-z].*?(?=\s(?:updates?|alert))", str(h4TagResp), re.IGNORECASE)
    return name[0]

def warningDate(ParTagResp):
    warn_date = re.findall(r"\d{1,2}\s.*?,\s+\d{4}", str(ParTagResp))
    return warn_date[0]

def level(ParTagResp):
    lvl = re.findall(r"●\s(High|Low|Medium|Critical)", str(ParTagResp))
    return lvl[0]

def warningNumber(ParTagResp):
    warn_num = re.findall(r"20[0-9]{2}-[0-9]{3,4}", str(ParTagResp))
    return warn_num[0]

def targetSector(parsed_html):
    target = re.findall(r"(?<=[0-9]<\/p>\n<p>).*?(?=<\/p>)", str(parsed_html),re.DOTALL)
    return html2text.html2text(target[0])

def description(parsed_html):
    Description = re.findall(r"(?:Description:|Description</b>:|Description</strong>:).*?(?=(?:<b>Threats:|<strong>Threats:))", str(parsed_html),re.DOTALL)
    Descriptions1 = re.sub(r"(?:Description:</b></p><p>|Description</b>:</p><p>|Description:</strong>.*?</p><p>)", "", str(Description[0]),0,re.DOTALL)
    return html2text.html2text(Descriptions1)

def threats(parsed_html):
    threats = re.findall(r"(?:Threats:|Threats:</strong>:|</p>An attacker|</p>Attacker|</p>Remote).*?(?=(?:<strong>Best|<p><b>Best))", str(parsed_html),re.DOTALL)
    thr = re.sub("Threats:</b></p>|Threats:</strong>", "", threats[0])
    return html2text.html2text(thr)

def preventiveProcedures(parsed_html):
    for tag in parsed_html.find_all("span"):
        tag.decompose()
    prevent = re.findall(r"The CERT team.*?(?=(?:</div></p>|\n</div>))", str(parsed_html))
    prev = html2text.html2text(prevent[0])
    pre = re.sub(r"\[(?:[^\]|]*\|)?([^\]|]*)\]", "", prev)
    return pre
