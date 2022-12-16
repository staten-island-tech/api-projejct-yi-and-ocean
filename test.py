import json
import pip._vendor.requests as requests


input = input('enter word here omg')
key = 'a1aafee4-36ef-4329-bc85-e87ff1b83aa2'
r = requests.get(f"https://dictionaryapi.com/api/v3/references/collegiate/json/{input}?key={key}").json()
print(r)
