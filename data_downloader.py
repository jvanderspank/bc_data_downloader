## Jeff Vanderspank
## Jan. 29th, 2021
## The purpose of this code is to extract DEMs from : pub.data.gov.bc.ca



from bs4 import BeautifulSoup as bs
import requests

DOMAIN = ('https://pub.data.gov.bc.ca/datasets/')
URL = ('https://pub.data.gov.bc.ca/datasets/175624/')
FILETYPE = '.dem.zip'

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

folders = []

for link in get_soup(URL).find_all('a', href=True):
    file_link = link.get('href')
    folderUrl = URL + file_link
    demPage = get_soup(folderUrl)
    for dem in demPage.find_all('a', href=True):
        demLink = dem.get('href')
        if demLink.endswith(FILETYPE):
            folders.append(URL + demLink)
          
for link in folders:
    file_name = link.rpartition('/')
    file_name = file_name[2]
    with open(file_name, 'wb') as file:
        response = requests.get(link)
        file.write(response.content)

