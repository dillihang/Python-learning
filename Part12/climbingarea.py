class ClimbingRoute:
    """
    Exercise template for ClimbingArea and ClimbingRoute classes.

    This module provides the classes and helper functions for managing climbing areas
    and their routes. The template originally includes the ClimbingRoute and ClimbingArea
    class structures. The functions below were added to perform sorting and retrieval tasks:

        - by_length(item: ClimbingRoute): Returns the length of a climbing route.
        - by_difficulty(item: ClimbingRoute): Returns a tuple (grade, length) for difficulty comparison.
        - sort_by_length(routes: list): Returns a new list of ClimbingRoute objects sorted by length (longest first).
        - sort_by_difficulty(routes: list): Returns a new list of ClimbingRoute objects sorted by difficulty (hardest first).
        - sort_by_number_of_routes(areas: list): Returns a new list of ClimbingArea objects sorted by the number of routes (ascending).
        - sort_by_most_difficult(areas: list): Returns a new list of ClimbingArea objects sorted by the most difficult route (descending).

    Notes:
        - The ClimbingArea class encapsulates its routes in a private list (__route_list).
        - Sorting by difficulty uses alphabetical order for grades, with longer routes considered harder
        if grades are the same.
    """
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} meters, grade {self.grade}"
    
class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__route_list = []

    def add_route(self, route: ClimbingRoute):
         self.__route_list.append(route)
    
    def routes(self):
        return len(self.__route_list)
        
    def hardest_route(self):
        return max(self.__route_list, key=by_difficulty)

    def __str__(self):
        return f"{self.name}, {len(self.__route_list)}, hardest {self.hardest_route().grade}"
        
def by_length(item: "ClimbingRoute"):
        return item.length

def by_difficulty(item: "ClimbingRoute"):
        return (item.grade, item.length)

def sort_by_length(routes: list):
    return sorted(routes, key=by_length, reverse=True)

def sort_by_difficulty(routes: list):
    return sorted(routes, key=by_difficulty, reverse=True)

def sort_by_number_of_routes(areas: list):
    def sort_by_len_object(area_list: ClimbingArea):
        return area_list.routes()
    return sorted(areas, key=sort_by_len_object)

def sort_by_most_difficult(areas: list):
    def sort_by_hardest_route(area_list: ClimbingArea):
        hardest_route = area_list.hardest_route()
        return by_difficulty(hardest_route)
    return sorted(areas, key=sort_by_hardest_route, reverse = True)
     

if __name__ == "__main__":

    ca1 = ClimbingArea("Olhava")
    ca1.add_route(ClimbingRoute("Edge", 38, "6A+"))
    ca1.add_route(ClimbingRoute("Great cut", 36, "6B"))
    ca1.add_route(ClimbingRoute("Swedish route", 42, "5+"))

    ca2 = ClimbingArea("Nummi")
    ca2.add_route(ClimbingRoute("Synchro", 14, "8C+"))

    ca3 = ClimbingArea("Nalkkila slab")
    ca3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
    ca3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
    ca3.add_route(ClimbingRoute("Piggy not likey", 12 , "6B+"))
    ca3.add_route(ClimbingRoute("Orchard", 8, "6A"))

    print(ca1)
    print(ca3.name, ca3.routes())
    print(ca3.hardest_route())

    print()
    print()
    print()

    areas = [ca1, ca2, ca3]
    for area in sort_by_number_of_routes(areas):
        print(area)

    print()
    print()
    print()

    areas = [ca1, ca2, ca3]
    for area in sort_by_most_difficult(areas):
        print(area)