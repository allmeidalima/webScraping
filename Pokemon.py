from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

html = urlopen("https://www.pokemon.com/br/pokedex/")
bs = BeautifulSoup(html, 'html.parser')
#print(bs)
#linhas = bs.find_all('tr', {'class':'even'})
pokemon = bs.find_all('li')

pokemons = []

for item in pokemon:
    for i in range(899):
        if str(i) in item.text:
            if item.text not in pokemons:
                pokemons.append(item.text) 
                #print(item.text)

#pokemons = [i for item in pokemon for i in range(899) if str(i) in item.text and print(item.text)]
#print(pokemons)

with open("meusPokemons.json", 'w', encoding='utf8') as data:
    json.dump(pokemons, data, ensure_ascii=False, indent=2)
#with open('./db.json', 'w', encoding='utf8') as f:
        #json.dump(data, f, ensure_ascii=False, indent=2)