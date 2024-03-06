import requests
import json
from string import Template
import template as t

def request_get(url):
    return json.loads(requests.get(url).text)

def process_birds_data():
    response = request_get('https://aves.ninjas.cl/api/birds')
    birds = []
    for bird in response:
        new_bird={}
        new_bird["nombre"]=bird.get("name").get("spanish")
        new_bird["name"]=bird.get("name").get("english")
        new_bird["image"]=bird.get("images").get("main")
        birds.append(new_bird)
    return birds

def create_template():
    bird_template = Template(t.bird_template)
    content = ''
    for bird in process_birds_data():
        content += bird_template.substitute(url = bird["image"], nombre = bird["nombre"],name = bird["name"])

    return content
if __name__ == '__main__':
    for bird in process_birds_data():
        print(bird)

    
