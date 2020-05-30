#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

USER = 'joaoofreitas'
URL = 'https://github.com/'
print('Parsing: ' + URL + USER)

html = requests.get(URL + USER)

if html.status_code != 200:
    print('An error has ocurred. Please check if the website is online or correct.')


print('Success Parsing the Profile\nPretiffying it...\n\n')
scrape = BeautifulSoup(html.text, 'html.parser')
pinnedRepos = scrape.findAll('div',{'class':'pinned-item-list-item-content'})

records = {}
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
    records[numberOfRepos] = (name.text, URL + USER + routeURL['href'], repoDescription.text)

print(records)
