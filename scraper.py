#!/usr/bin/python3

from bs4 import BeautifulSoup
from requests import get
from json import dumps

data = {}
USER = 'joaoofreitas'
URL = 'https://github.com/'
print('Parsing: ' + URL + USER)

def dictToJson(dict):
    dumpedDict = dumps(dict)
    return dumpedDict

html = get(URL + USER)

if html.status_code != 200:
    print('An error has ocurred. Please check if the website is online or correct.')


print('Success Parsing the Profile\nPretiffying it...\n\n')
scrape = BeautifulSoup(html.text, 'html.parser')
pinnedRepos = scrape.findAll('div',{'class':'pinned-item-list-item-content'})

numberOfRepos = 0
for repos in pinnedRepos:
    names = repos.findAll('span', {'class': 'repo'})
    routeURLs = repos.findAll('a', href=True)
    repoDescriptions = repos.findAll('p', {'class':'pinned-item-desc'})

    for name in names:
        print(name.text)
    for routeURL in routeURLs:
        print(URL + USER + routeURL['href'])
    for repoDescription in repoDescriptions:
        print(repoDescription.text)
   
    numberOfRepos += 1
    data['Repo' + str(numberOfRepos)] = (name.text, URL + USER + routeURL['href'], repoDescription.text)
 
