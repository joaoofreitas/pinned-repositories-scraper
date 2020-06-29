#!/usr/bin/python3

from bs4 import BeautifulSoup
from requests import get
from json import dumps, dump
from sys import argv

data = {}
URL = 'https://github.com/'

try:
    USER = str(argv[1])
except IndexError:
    USER = input('Enter your github username: ')
    str(USER)

print('Parsing: ' + URL + USER)

def dictToJSON(dict):
    dumpedDict = dumps(dict)
    return dumpedDict

html = get(URL + USER)

if html.status_code != 200:
    print('An error has ocurred. Please check if the website is online or your username correct.')
else:
    print('Success Parsing the Profile!\n')
    print('Scrapping it...\n\n')
    print('=====================================================================================') 
    scrape = BeautifulSoup(html.text, 'html.parser')
    pinnedRepos = scrape.findAll('div',{'class':'pinned-item-list-item-content'})

    numberOfRepos = 0
    for repos in pinnedRepos:
        names = repos.findAll('span', {'class': 'repo'})
        routeURLs = repos.findAll('a', href=True)
        repoDescriptions = repos.findAll('p', {'class':'pinned-item-desc'})
        languages = repos.findAll('span', {'class': 'd-inline-block mr-3'})
        languageColors = repos.findAll('span',{'class': 'repo-language-color'})


        for name in names:
            parsedName = name.text 
            print(parsedName)
 
        for routeURL in routeURLs:
            print(URL + USER + routeURL['href'])
        
        for repoDescription in repoDescriptions:
            description = repoDescription.text
            description = description.replace('\n', '') 
            print(description)
        
        for language in languages:
            preParsedLanguage = language.text
            parsedLanguage = preParsedLanguage.replace('\n', '')
            print(parsedLanguage)
        
        for languageColor in languageColors:
            color = str(languageColor)
            print(color[59:66])   #Temporary Solution
            
        
        numberOfRepos += 1
        data['Repo' + str(numberOfRepos)] = parsedName, URL + USER + routeURL['href'], description, parsedLanguage, color[59:66]

        with open('fetchedData.json', 'w+') as fetchedData:
            dump(dictToJSON(data), fetchedData, ensure_ascii=False, indent=4)


