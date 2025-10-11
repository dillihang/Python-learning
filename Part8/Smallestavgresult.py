def smallest_average(person1: dict, person2: dict, person3: dict):

    new_dict={}

    first_person = (person1["result1"] + person1["result2"] + person1["result3"])/3
    second_person = (person2["result1"] + person2["result2"] + person2["result3"])/3
    third_person = (person3["result1"] + person3["result2"] + person3["result3"])/3

    smallest=min(first_person,second_person,third_person)
    
    if smallest == first_person:
        new_dict=person1
    elif smallest == second_person:
        new_dict=person2
    elif smallest == third_person:
        new_dict=person3

    return new_dict
    
if __name__=="__main__":

    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}


    print(smallest_average(person1, person2, person3))
 