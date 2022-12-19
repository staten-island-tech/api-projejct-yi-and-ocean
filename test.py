import json
import pip._vendor.requests as requests

input = 'god'
# input = input('enter word here omg')
key = 'a1aafee4-36ef-4329-bc85-e87ff1b83aa2'

def getWord(search, key):
    r = requests.get(f"https://dictionaryapi.com/api/v3/references/collegiate/json/{search}?key={key}").json()
    return r

print(getWord(input, key))

for index in getWord(input, key):
    print(index)