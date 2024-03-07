import json
from string import Template
from process_data import create_template 
import parameters as p
#Se utiliza template.py para especificar la estructura y así que código quede mas limpio

html = Template(p.html_template).substitute(main = create_template())

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html)






