import pandas as pd

def output2json(df,file):
        with open(file, 'w') as f:
            f.write(df.to_json(orient='records', lines=True))

def output2csv(df,file):
    df.to_csv(file, index=False, encoding='utf-8')

def convertor(main,warndate,lvl,warn,trgt,desc,threat,prvnt,url,fileoutput,fileformat):
    df = pd.DataFrame()
    df['Main Subject'] = main
    df['Warning Date'] = warndate
    df['Severity Level'] = lvl
    df['Warning Number'] = warn
    df['Target Sector'] = trgt
    df['Description'] = desc
    df['Threats'] = threat
    df['Best practice and Recommendations:'] = prvnt
    df['URL Reference:'] = url

    if fileformat == 'json':
        output2json(df,fileoutput)
    elif fileformat == 'csv':
        output2csv(df,fileoutput)