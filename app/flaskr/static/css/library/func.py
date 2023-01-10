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
    else:
        try:
            if word[0]['shortdef']:
                return 'word.html'
        except:
            return '404.html'

def randomWord():
    done == False
    while done == False: 
        randomWord = requests.get('https://random-word-api.herokuapp.com/word?number=1').json()
        defOfWord: getWord(randomWord)
        if defOfWord == []:
            pass
        else:
            done = True
            return defOfWord[0]

