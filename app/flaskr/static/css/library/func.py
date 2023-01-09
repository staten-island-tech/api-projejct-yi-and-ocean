import json
import requests

def getWord(Search):
    key = 'cc94a000-270c-4303-8c37-1ba4576600e6'
    data = requests.get(
         f"https://dictionaryapi.com/api/v3/references/sd4/json/{search}?key={key}").json()
    return data

def checkValidWord(word):
    if word == []:
        return '404.html'


