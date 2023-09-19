import random

def simple_list():
    persons = []
    
    for i in range(10):
        person = {
            "id": i,
            "age": random.randint(1, 100)
        }
        persons.append(person)   
    return persons

def sort_list(dicts):
    return sorted(dicts, key=lambda x: x['age'])

def sort_list():
    pass
