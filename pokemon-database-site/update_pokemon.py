import json
import requests
import os

def update_pokemon():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
    pokemon_file = __file__.replace("pokemon-database-site", "assets")
    pokemon_file = __file__.replace("update_pokemon.py", "pokemon.json")
    data = json.loads(response.text)
    results = data["results"]
    f = open(pokemon_file, "w")
    f.write(json.dumps(results, indent= 4))
    f.close()


update_pokemon()