import json
import urllib.request
import os

file = open('states.json').read()
data = json.loads(file)
output_dir = "img"
BASE_PATH = "https://www.usmint.gov/images/mint_programs/50sq_program/states/"

# XX_Designs.gif

for key in data:
    filename = "{}_Designs.gif".format(str(key))
    url = '{}{}'.format(BASE_PATH, filename)
    print(url)
    output_file = os.path.join(os.path.curdir, output_dir, filename)
    urllib.request.urlretrieve(url, output_file)
