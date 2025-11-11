def search_by_name(filename: str, word:str):

    my_list=[]
    recipe_list=[]
    found_list=[]

    with open(filename) as file:

        for line in file:
            line=line.strip()
            my_list.append(line)
            if line=="":
                my_list.remove("")
                recipe_list.append(my_list)
                my_list=[]
                continue

        if my_list:
            recipe_list.append(my_list)

    for items in recipe_list:
        dishname=items[0]

        if word.lower() in dishname.lower():

            found_list.append(dishname)

    return found_list


def search_by_time(filename: str, prep_time:int):

    my_list=[]
    recipe_list=[]
    found_list=[]

    with open(filename) as file:

        for line in file:
            line=line.strip()
            my_list.append(line)
            if line=="":
                my_list.remove("")
                recipe_list.append(my_list)
                my_list=[]
                continue

        if my_list:
            recipe_list.append(my_list)

    for items in recipe_list:
        time=int(items[1])

        if time<=prep_time:

            found_list.append(f"{items[0]}, preparations {time} min")

    return found_list


def search_by_ingredient(filename: str, ingredient: str):

    my_list=[]
    recipe_list=[]
    found_list=[]

    with open(filename) as file:

        for line in file:
            line=line.strip()
            my_list.append(line)
            if line=="":
                my_list.remove("")
                recipe_list.append(my_list)
                my_list=[]
                continue

        if my_list:
            recipe_list.append(my_list)

    
    for items in recipe_list:
        if ingredient in items:

            found_list.append(f"{items[0]}, preparations {items[1]} min")

    return found_list



    

def main():

    if __name__ == "__main__":
        
        # found_recipes = search_by_name("Part 6/recipes1.txt", "cake")

        # for recipe in found_recipes:
        #     print(recipe)

        # found_recipes = search_by_time("Part 6/recipes1.txt", 20)

        # for recipe in found_recipes:
        #     print(recipe)

        found_recipes = search_by_ingredient("Part 6/recipes1.txt", "eggs")

        for recipe in found_recipes:
            print(recipe)


main()