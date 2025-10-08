import json

def print_persons(filename: str):

    with open("part7/" + filename) as file:

        data = file.read()

    details = json.loads(data)

    for people in details:

        print(f"{people['name']} {people['age']} years ({', '.join(people['hobbies'])})")

    
print_persons("students.json")