import requests
import json
from string import Template
import parameters as p

def request_get(url):
    """
    Realiza petición request a bdd de Aves
    ------------
    Parameter
    ------------
    url
        Type:   String
    
    Return
    ------------
    response
        Type:   JSON
        Descripción:    Respuesta completa de API Get
    """
    response = json.loads(requests.get(url).text)
    return response

def process_birds_data():
    """
    Procesa los datos obtenidos con request_get para simplificarlos
    ------------
    Parameter
    ------------
    None
    
    Return
    ------------
    birds
        Type:   Array de diccionarios
        Descripción:    diccionario contiene nombre, name e image
        Ejemplo:    ["{'nombre': 'Tenca', 'name': 'Chilean Mockingbird', 'image': 'https://aves.ninjas.cl/'},{'nombre': 'Tórtola Común', 'name': 'Eared Dove', 'image': 'https://aves.ninjas.cl'}"]
    """
    response = request_get(p.URL)
    birds = []
    for bird in response:
        new_bird={}
        new_bird["nombre"]=bird.get("name").get("spanish")
        new_bird["name"]=bird.get("name").get("english")
        new_bird["image"]=bird.get("images").get("main")
        birds.append(new_bird)
    return birds

def create_template():
    """
    Arma template de imagenes
    ------------
    Parameter
    ------------
    None
    
    Return
    ------------
    content
        Type:   String
        Descripción: Texto con contenido para escribir HTML de imagenes
    """
    bird_template = Template(p.bird_template)
    content = ''
    for bird in process_birds_data():
        content += bird_template.substitute(url = bird["image"], nombre = bird["nombre"],name = bird["name"])

    return content
if __name__ == '__main__':
    for bird in process_birds_data():
        print(bird)

    
