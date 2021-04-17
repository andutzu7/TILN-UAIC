import zeep 
import re

def request_lemmatized(text):

    wsdl = 'http://nlptools.info.uaic.ro/WebPosRo/PosTaggerRoWS?wsdl'
    client = zeep.Client(wsdl=wsdl)
    response = ''
    response += client.service.parseSentence_XML(text)
    response += '🤩'
    return response


if __name__ == '__main__':
# Adding the stopwords to the list
    stopwerdz = []
    count = 0
    with open('stopwords.txt',mode = 'r') as stopwerds:
        while 1:
            werd = stopwerds.readline()
            werd = werd.strip('\n')
            stopwerdz.append(werd)
            count = count + 1
            if count > 433:
                break
            
    text = request_lemmatized('azi am mers la magazinul colturos')
    arr = text.split('\n')
    for line in arr:
        found = re.search('.*(LEMMA="[A-Za-zăâîșț1-9]*").*',line)
        if found:
            res = found.group(1)
            print(res)