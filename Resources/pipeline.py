import re
import os
import json
import zeep
import nltk
from nltk.corpus import stopwords


def request_lemmatized(text):

    wsdl = 'http://nlptools.info.uaic.ro/WebPosRo/PosTaggerRoWS?wsdl'
    client = zeep.Client(wsdl=wsdl)
    response = ''
    response += client.service.parseSentence_XML(text)
    response += '🤩'
    return response


def format_text(text):
    text = request_lemmatized(text)
    arr = text.split('\n')
    arr_lemmas = []
    final_tokenized = []
    index = 0
    for line in arr:
        found = re.search('.*(LEMMA="[A-Za-zăâîșț1-9]*").*', line)
        if found:
            res = found.group(1)
            arr_lemmas.append(res)
        found = re.search('🤩', line)
        if found:
            arr_lemmas.append('🤩')
    for lemma in arr_lemmas:
        found = re.search('LEMMA="([A-Za-zăâîșț1-9]*)".*', lemma)
        if found:
            res = found.group(1)
            final_tokenized.append(res)
            index = index + 1
        if index == len(arr_lemmas)-1:
            found = re.search('🤩', line)
            if found:
                final_tokenized.append('🤩')
            break
    return final_tokenized[:-1]


def filter_stopwords(article,stopwerdz):

    with open('stopwords.txt', mode='r') as stopwerds:
        count = 0
        while 1:
            werd = stopwerds.readline()
            werd = werd.strip('\n')
            stopwerdz.append(werd)
            count = count + 1
            if count > 433:
                break
        stw = stopwords.words('romanian')
        stw.extend(stopwerdz)
        filtered_article = []
        for word in article:
            filtered_word =''
            for letter in word:
                if (letter.isalpha()):
                    filtered_word += letter
                else:
                    if(letter == '~'):
                        filtered_word += ' '
            if (filtered_word not in stw and filtered_word != '' and len(filtered_word) >= 2):
                filtered_article.append(filtered_word)
        return filtered_article

def convert_to_string(words):
    return ' '.join(words)

def pipeline(text):
    stopwerdz = []

    sentences = format_text(text)
    filtered_article = filter_stopwords(sentences,stopwerdz)
    filtered_article_string = convert_to_string(filtered_article)

    print(filtered_article_string)

    # return?

if __name__ == '__main__':

    text = "Regina Elisabeta a II-a a Marii Britanii a fost nevoită să stea singură în timpul funeraliilor, din cauza restricţiilor impuse de pandemia de coronavirus. Camerele de filmare nu au putut capta expresia chipului său, regina a stat mai mult cu capul plecat.Alţi membri ai casei regale care au apărut în imagini aveau feţele întristate. Prinţul Edward, cel mai mic dintre copiii reginei şi ai prinţului Philip, a fost văzut punându-şi mâna pe frunte în timp ce corul intona imnuri religioase. El a fost văzut apoi fixând de la distanţă sicriul tatălui său.Fiecare membru al casei regale - mai ales cei special invitaţi - au purtat haine de doliu de culoare închisă şi măşti sanitare negre.Ei au păstrat distanţa unii de ceilalți și în așezarea pe scaunele din interiorul capelei St.George, pentru a respecta restricţiile impuse de pandemia de coronavirus."
    pipeline(text)