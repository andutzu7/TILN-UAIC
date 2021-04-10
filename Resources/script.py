import os

stopwordz = []
with open('stopwords.txt',mode = 'r') as stopwords:
    stopwordz = stopwords.readlines()
print(stopwordz)


#with open('andy.txt',mode='r') as to_lematize: