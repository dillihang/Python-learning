def add_movie(database: list, name: str, director: str, year: int, runtime: int):

    dis={}

    dis["name"]=name
    dis["director"]=director
    dis["year"]=year
    dis["runtime"]=runtime

    database.append(dis)

 
def find_movies(database: list, search_term: str):


    my_movies=[]


    search_term = search_term.lower()

    for movies in database:
        if search_term in movies["name"].lower():
                my_movies.append(movies)




    return my_movies


def main():
  
   database = []
   add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
   add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
   add_movie(database, "Dawn of the dead", "M. Night Python", 2011, 101)
#    print(database)

   my_movies = find_movies(database, "python")
   print(my_movies)


if __name__ == "__main__":

    main()
