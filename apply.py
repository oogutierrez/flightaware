# This is for my application for Software Engineer - Big Data in FlightAware 

import requests
import json

url = 'https://flightaware.com/about/careers/apply?data='
headers = {'Content-type': 'application/json'}
urls = [ 
         "https://www.linkedin.com/in/orlando-gutierrez-09995a2/",
         "https://github.com/oogutierrez/flightaware"
       ]
       
data = {'name': 'Orlando Gutierrez',
        'email': 'oogutierrez@yahoo.com',
        'position': 'Software Engineer - Big Data',
        'urls': [ urls ],
        'comment': 'Please call me at 8323788532 or 4046617285'}

r = requests.post(url + json.dumps(data), headers=headers)
print(r.status_code, r.text)
