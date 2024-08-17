import json
import requests
import os

def update_pokemon():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
    pokemon_file = __file__.replace("pokemon-database-site", "assets")
    pokemon_file = __file__.replace("update_pokemon.py", "pokemon.json")
    data = json.loads(response.text)
    results = data["results"]
    for result in results:
        result["unformatted_name"] = result["name"]
        result["name"] = result["name"].title().replace("-", " ")
        id = result["url"].replace("https://pokeapi.co/api/v2/pokemon/", "")
        id = id.replace("/", "")
        print(id)
        img = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
        result["img"] = img
        result["id"] = id
        species = requests.get("https://pokeapi.co/api/v2/pokemon-species/" + id)
        species = species.text
        try:
            species = json.loads(species)
        except:
            break
        index = 0
        while index < 50:
            if species["flavor_text_entries"][index]["language"]["name"] == "en":
                result["desc"] = species["flavor_text_entries"][index]["flavor_text"]
                break
            else:
                index+=1
        print(result["desc"])
    f = open(pokemon_file, "w")
    print(results)
    f.write(json.dumps(results, indent= 4))
    f.close()


update_pokemon()