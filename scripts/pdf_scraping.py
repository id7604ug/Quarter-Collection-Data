import sys

country = list()

with open('states.txt', 'r') as state_names:
    states = state_names.readlines()
    for state in states:
        country.append(state.strip())

with open('country.txt', 'r',
          encoding=sys.getfilesystemencoding()) as read_info:
    read_data = read_info.readlines()
    print(len(read_data))
    for line in read_data:

        if 'Statehood' in line:
            with open('process_data.txt', 'a') as write_process_data:
                write_process_data.write(line + "\n")
