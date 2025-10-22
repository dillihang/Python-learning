class Person:
    """
    PhoneBook Application - Version 2

    This version of the phone book expands upon the previous version by adding support
    for addresses. Each person is represented by a Person object, which stores multiple 
    phone numbers and a single address. The PhoneBook class manages Person objects in a 
    dictionary keyed by name, ensuring that numbers and addresses are associated correctly.

    Key changes in Version 2:
    - Added the Person class to encapsulate a person's name, numbers, and address.
    - PhoneBook now stores Person objects instead of simple lists.
    - Added methods to add and retrieve addresses.
    - Updated the user interface to support:
        - Adding phone numbers
        - Adding addresses
        - Searching by name
        - Searching by phone number
    - Removed functionality for saving and loading data to/from a file, simplifying the 
    program to operate in-memory only.
    """
    def __init__(self, name: str):
        self.__name = name
        self.__number_list = []
        self.__address = None

    def add_number(self, number: str):
        self.__number_list.append(number)
        
    def add_address(self, address: str):
        self.__address = address

    def name(self):
        return self.__name
    
    def numbers(self):
        return self.__number_list
    
    def address(self):
        return self.__address
    
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            new_person_object = Person(name)
            new_person_object.add_number(number)
            self.__persons[name] = new_person_object
        else:
            existing_person_object = self.__persons[name]
            existing_person_object.add_number(number)

    # def get_entry(self, name):
    #     if name in self.__persons:
    #         new_object = self.__persons[name]
    #         return new_object.numbers()

    def add_address(self, name: str, address: str):
        if name in self.__persons:
            new_object = self.__persons[name]
            new_object.add_address(address)
    
    def get_address(self, name: str):
        if name in self.__persons:
            new_object = self.__persons[name]
            return new_object.address()

    def get_numbers_by_name(self, name: str):
        if name in self.__persons:
            new_object = self.__persons[name]
            return new_object.numbers()
    
    def get_name_by_number(self, number: str):
        for name, person_object in self.__persons.items():
            if number in person_object.numbers():
                return name
        return None

    def all_entries(self):
        # Return all entries (in dictionary format)
        return self.__persons


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add number")
        print("2 search by name")
        print("3 search by number")
        print("4 add address")

    def add_number_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search_by_name(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers_by_name(name)
        address = self.__phonebook.get_address(name)
        if numbers is None:
            print("number unknown")
        else:
            for number in numbers:
                print(number)
        if address is None:
            print("unknown address")
            return
        
        print(address)

    def search_by_number(self):
        number = input("number: ")
        name = self.__phonebook.get_name_by_number(number)
        if name is None:
            print("unknown number")
            return
        print(name)

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number_entry()
            elif command == "2":
                self.search_by_name()
            elif command == "3":
                self.search_by_number()
            elif command == "4":
                self.add_address()
            else:
                self.help()


if __name__ == "__main__":
    
    app = PhoneBookApplication()
    app.execute()