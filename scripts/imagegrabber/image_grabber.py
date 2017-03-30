import json
import urllib.request
import os

# http://stackoverflow.com/questions/1270951/python-how-to-refer-to-relative-paths-of-resources-when-working-with-code-repo
fn = os.path.join(os.path.dirname(__file__), 'states.json')

with open(fn) as json_data:
    data = json.load(json_data)
    # http://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
    if not os.path.exists("img"):
        os.makedirs('img')
        print('Making img Directory')
    else:
        print('img directory already exists')
    if not os.path.exists("img\AK_Designs.gif") and  not os.path.exists("img\WY_Designs.gif"):
        output_dir = "img"
        print('exec')
        BASE_PATH = "https://www.usmint.gov/images/mint_programs/50sq_program/states/"

        # https://www.usmint.gov/images/mint_programs/50sq_program/states/OK_Designs.gif

        # XX_Designs.gif

        for key in data:
            print(key)
            filename = "{}_Designs.gif".format(str(key))
            url = '{}{}'.format(BASE_PATH, filename)
            print(url)
            output_file = os.path.join(os.path.dirname(__file__), output_dir, filename)
            urllib.request.urlretrieve(url, output_file)
    else:
        print('Quarter image files already exist')
