# Importing the required libraries
import json

# Function to print hello world
def hello():
    data={'message':'Hello World!!'}
    return data

# Function to read the data from the json file and return it (original recepie)
def read_data():
    with open('data\ex5.json','r') as f:
        data=json.load(f)
    json.close()
    return data

# Function to read the modified data from the json file and return it (modified recepie)
def mod():
    write_data()
    with open('data\ex5_out.json','r') as f:
        data=json.load(f)
    return data

# Function to modify the data and save it to the another json file (modified recepie)
def write_data():
    with open('data\ex5.json','r') as file:
        ex5=json.load(file)

    for x in ex5:
        if x['type'] == "donut" and x['name'] == 'Old Fashioned':
            z=x['batters']['batter']
            z.append({'id': '1003', 'type': 'Coffee'})

    with open('data\ex5_out.json','w') as file:
        json.dump(ex5,file,indent=4)
    
