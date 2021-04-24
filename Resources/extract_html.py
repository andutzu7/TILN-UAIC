from bs4 import BeautifulSoup
import requests
import re
def extract_article(link):
    resp = requests.get(link)
    html_doc = resp.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    response = soup.find_all('p')[:-1]
    regex = re.compile('<p.*>(.*)</p>')
    result = ''
    for item in response:
        clean = regex.match(str(item))
        result += clean.group(1)
    return result

if __name__ == '__main__':
    link = 'https://www.digi24.ro/stiri/actualitate/restrictii-prelungite-in-capitala-prefect-vor-fi-relaxari-cand-incidenta-coboara-sub-3-ce-exceptii-exista-in-perioada-pastelui-1507361'
    print(extract_article(link))
