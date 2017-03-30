import sys
import json
import urllib.request

states = {}

with open('states.json') as json_data:
    data = json.load(json_data)
    states = data

# Get state coin info
with open('country.txt', 'r', encoding=sys.getfilesystemencoding()) as read_info:
    read_data = read_info.readlines()
    print(len(read_data))
    x = 0
    while x < len(read_data):
        line = read_data[x]
        if 'Statehood' in line:
            with open('process_data.txt', 'a') as write_process_data:
                state_name = read_data[x - 1].replace('\n', '')
                if state_name.lower() in states.items()
                write_process_data.write('State: ' + state_name + ' ' + line + "\n")
        x += 1
