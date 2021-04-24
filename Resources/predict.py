import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from extract_html import extract_article
from pipeline import pipeline

new_model = tf.keras.models.load_model('model92.h5')

df=pd.read_csv('./corpus_complet.tsv',delimiter='\t')
df = df.dropna()

labels = df.authenticity
convert = lambda x : 0 if x == 'FAKE' else 1
labels = [convert(label) for label in labels ]
count=0
for label in labels:
    if label == 1:
        count = count + 1
        
X_train, _ , y_train, _ = train_test_split(df['preprocessed body'] ,labels, test_size = 0.2, random_state=6)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)

#test_data = ['om sine trece câine dietă vegană transforma pericol public umbla stradă legumă vedere dimineață câine vegan scăpat lesă sine înfige colț castravete bărbat an bărbat rămâne tzatziki salată asortat murătură castravete amenința proprietar animal vrea judecată groaznic veni piață procura castravete fabio centimetru scop consuma odată ajuns acasă explica jean victimă atac intra bloc vedea fiară rupe lesă goni sine înfige colț castravete rămâne decât codiță cădea picior turti roșu cetățean plăcea sine plimba parc fleică mânzat borsetă spune conveni trend câine vegani spera fiță trecător','lider PNL USR UDMR semna marți seară coaliție guvernare criză politic izbucnite demitere premier florin cîțu PNL ministru sănătate vlad voiculescu USR anunța vrea propune ministru sănătate','Regina elisabeta nevoit sta singur funeralii restricție impus pandemie coronavirus cameră filmare putea capta expresie chip regină sta cap plecat membru casă regal apărea imagine față întristat prinț edward mic copil regină prinț philip văzut pune sine mână frunte cor intona imn religios văzut fixa distanță sicriu tată membru casă regal special invitat purta haină doliu culoare închis mască sanitar negru păstra distanță celălalt așezare scaun interior capelă George respecta restricție impus pandemie coronavirus']
#link = 'https://www.digi24.ro/stiri/actualitate/restrictii-prelungite-in-capitala-prefect-vor-fi-relaxari-cand-incidenta-coboara-sub-3-ce-exceptii-exista-in-perioada-pastelui-1507361'
#link = 'https://www.timesnewroman.ro/life-death/tiriac-depasit-in-topul-forbes-de-daniel-dines-si-3000-de-vamesi-din-nadlac/'
#link = 'https://www.timesnewroman.ro/politic/klaus-iohannis-grav-afectat-de-rugina-dupa-ce-a-mers-cu-bicicleta-prin-ploaie/'
#link = 'https://www.digi24.ro/stiri/actualitate/justitie/seful-de-la-drumuri-din-craiova-a-fost-retinut-dupa-ce-si-a-falsificat-diploma-si-incasat-idemnizatii-de-peste-1-milion-de-lei-1507303'
#link = 'https://www.digi24.ro/stiri/actualitate/grafic-doar-doua-judete-si-capitala-raman-in-scenariul-rosu-1507455'
link = 'https://neurococi.ro/posts/Yabba-dabba-doo-Dacia-lanseaza-loganul-h'
text = extract_article(link)

test_data = pipeline(text)
# Because of a weird  behaviour of the predict method, I have to have at least 2 elements in the array
test_data.append('bug fix')
X_test = pd.DataFrame(np.array(test_data))


text_series = X_test.squeeze()

X_test = pad_sequences(tokenizer.texts_to_sequences(text_series))
X_test = np.array(X_test)

predictions = new_model.predict(X_test)[:-1]

CATEGORIES = ['TRUE','FAKE']

for index,prediction in enumerate(predictions):

    answer = lambda x : 'TRUE' if int(round(x))==1 else 'FALSE' 
    print(f'{answer(prediction[0])}, percentage = {prediction[0]}')