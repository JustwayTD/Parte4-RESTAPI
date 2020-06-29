import json
import requests
api_url_base="https://swapi.dev/api/"
planets = "https://swapi.dev/api/planets/?page="
specie = "https://swapi.dev/api/species/"
starship ="http://swapi.dev/api/starships/?page="
busqueda = {"search": "Tatooine"}
def Obt_planetas(url,clima):
    count = []
    response = []
    x = 1
    while(x<7):
        planet_page = url + str(x)
        result = requests.get(planet_page)
        pl_js = result.json()
        final = pl_js['results']
        for planet in final:
            response.append(planet)
        x+=1
    for planet in response:
        if planet['climate'] ==clima:
            count.append(planet)
    print("Son ", len(count), "los planetas de clima ", clima)
def Obt_especie(num_peli , especi):
    url_pelis = "https://swapi.dev/api/films/"
    check = requests.get(specie,params={'search':especi})
    resul = check.json()
    movie = resul['results']
    comp = 0
    for mov in movie:
        if movie['films'] == url_pelis +str(num_peli)+"/":
            comp +=1
    if comp == 0:
        print("la especie ", especi, "no aparece")
    else:
        print("la especie ", especi," aparece ", comp , "veces")
    
def beegchugus(url):
    count = []
    response = []
    x = 1
    while(x<5):
        planet_page = url + str(x)
        result = requests.get(planet_page)
        pl_js = result.json()
        final = pl_js['results']
        for starship in final:
            response.append(starship)
            if final['length'] > count['length']:
                count = final 
        x+=1
    print("La nave mas grande es:", count['name'])


if __name__ == "__main__":
    Obt_planetas(planets,"arid")
    Obt_especie(6,"Wookie")
    beegchugus(starship)