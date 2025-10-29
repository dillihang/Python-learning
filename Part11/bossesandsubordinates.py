class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(employee: "Employee"):
    """
    Recursively counts the total number of subordinates under the given employee.

    This includes both direct subordinates and all indirect subordinates 
    (subordinates of subordinates, and so on).

    Args:
        employee (Employee): The employee whose subordinates are to be counted.

    Returns:
        int: The total number of subordinates under the given employee.
    """
    print(f"ENTER {employee.name}")
    total = len(employee.subordinates)
    for person_object in employee.subordinates:
        total += count_subordinates(person_object)
    print(f"EXIT  {employee.name} -> {total}")
    return total


if __name__ == "__main__":
    
    t1 = Employee("Sally")
    t2 = Employee("Eric")
    t3 = Employee("Matthew")
    t4 = Employee("Emily")
    t5 = Employee("Adele")
    t6 = Employee("Claire")
    t1.add_subordinate(t4)
    t1.add_subordinate(t6)
    t4.add_subordinate(t2)
    t4.add_subordinate(t3)
    t4.add_subordinate(t5)
    print(count_subordinates(t1))
    print(count_subordinates(t4))
    print(count_subordinates(t5))
   
    