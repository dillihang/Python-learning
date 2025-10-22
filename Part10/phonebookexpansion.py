class PhoneBook:
    """
    Phone Book Application

    This program implements a simple text-based phone book application. It allows users
    to add new contacts, search for numbers by name, and save or load data from a file
    automatically. The application is organized into three main classes:

    - PhoneBook: handles storage and lookup of names and numbers.
    - FileHandler: manages reading and writing phone book data to a file.
    - PhoneBookApplication: provides a command-line user interface.

    Note:
    The overall structure and functionality of the code were provided as part of an exercise
    template. Only the "search by number" feature (the method `get_name_by_num()` in PhoneBook and 
    `search_by_num()` in PhoneBookApplication) were implemented by me.
    """
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            # Add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []
        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name]
    
    def get_name_by_num(self, number: str):
        for names, numbers_list in self.__persons.items():
            if number in numbers_list:
                return names
        return None
        

    def all_entries(self):
        # Return all entries (in dictionary format)
        return self.__persons


class FileHandler:
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        try:
            with open(self.__filename) as f:
                for line in f:
                    parts = line.strip().split(';')
                    name, *numbers = parts
                    names[name] = numbers
        except FileNotFoundError:
            # If file doesn’t exist yet, just return an empty dict
            pass
        return names

    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("Part10/phonebook.txt")

        # Add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers is None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def search_by_num(self):
        number = input("number: ")
        name = self.__phonebook.get_name_by_num(number)
        if name is None:
            print("unknown number")
            return
        else:
            print(name)

    def exit(self):
        # Save data back to the file before exiting
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_by_num()
            else:
                self.help()


if __name__ == "__main__":
    application = PhoneBookApplication()
    application.execute()
