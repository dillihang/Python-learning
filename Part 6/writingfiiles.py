name=input("Whom should i sighn this to: ")
where=input("Where shall i save it: ")


with open("Part 6/" + where, "w") as my_file:
    my_file.write(f"Hi {name}, ")
    my_file.write("we hope you enjoy learning Python with us! ")
    my_file.write("Best, ")
    my_file.write("Mooc.fi Team")