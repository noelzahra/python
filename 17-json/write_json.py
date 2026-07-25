'''
    Writing JSON data to a file using Python's built-in json module.
'''

import json

data = {
    'John Doe': {
        'name': 'John Doe',
        'gender': 'Male',
    },
    'Jane Smith': {
        'name': 'Jane Smith',
        'gender': 'Female',
    }
}

if __name__ == "__main__":
    with open('json_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print(f"Saving to a json file: {type(json_file)} for data variable \n Data dict is : {data}\n")

    with open('json_data.json', 'r') as json_file:
        json_object_literals = json_file.read()
        print(f"JSON key value pairs  in json_data.json: {json_object_literals}")