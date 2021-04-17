import zeep

wsdl = 'http://nlptools.info.uaic.ro/WebPosRo/PosTaggerRoWS?wsdl'
client = zeep.Client(wsdl=wsdl)
response = ''
response += client.service.parseSentence_XML('ana arer mere.')
print(response)