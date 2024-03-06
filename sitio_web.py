
import json
from string import Template
from process_data import create_template 
import template as t

html_template = Template(t.html_template)

html = html_template.substitute(main = create_template())

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html)






