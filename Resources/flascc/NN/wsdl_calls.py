import zeep 
import pandas as pd

def request_lemmatized(text):
    response = ''
    response += client.service.parseSentence_XML(text)
    response += '🤩'
    return response

def read_tsv(path):
    df = pd.read_csv(path, sep='\t')
    return df

if __name__=='__main__':    
    wsdl = 'http://nlptools.info.uaic.ro/WebPosRo/PosTaggerRoWS?wsdl'
    client = zeep.Client(wsdl=wsdl)
    df = read_tsv('./balancing_dataset.tsv.tsv')
    text=[]
    outfile_path = './wdsl.txt'
    for row in df.itertuples(index=True, name='Pandas'):
        text.append(row._1)
    
    with open(outfile_path,'a+') as f:
        for article in text:
            f.write(request_lemmatized(article))