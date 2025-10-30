class Task:
    """
    Represents a single task in a software company's task list.

    Attributes:
        description (str): A short description of the task.
        programmer (str): Name of the programmer assigned to the task.
        workload (int): Estimated hours required to complete the task.
        id (int): Unique identifier for the task, assigned sequentially.
        __is_finished (bool): Internal flag indicating if the task is finished.

    Methods:
        is_finished(): Returns True if the task is finished, False otherwise.
        mark_finished(): Marks the task as finished.
        __str__(): Returns a readable string representation of the task, including status.
    """
    id_counter=1

    def __init__(self, description: str, programmer: str, workload: int):
        self.__description = description
        self.__programmer = programmer
        self.__workload = workload
        self.__is_finished = False
        self.id = Task.id_counter
        Task.id_counter += 1
    
    @property
    def description(self):
        return self.__description
    
    @property
    def programmer(self):
        return self.__programmer
    
    @property
    def workload(self):
        return self.__workload
    
    def is_finished(self):
        return self.__is_finished
    
    def mark_finished(self):
        self.__is_finished=True

    def __str__(self):
        value = "FINISHED" if self.__is_finished else "NOT FINISHED"
            
        return f"{self.id}: {self.__description} ({self.__workload} hours), programmer {self.__programmer} {value}"
    

class OrderBook:
    """
    Manages a collection of tasks (Task objects) for a software company.

    Attributes:
        __order_list (list): Internal list storing Task objects.

    Methods:
        add_order(description, programmer, workload):
            Adds a new Task to the OrderBook.
        all_orders():
            Returns a list of all Task objects in the OrderBook.
        programmers():
            Returns a collection of unique programmer names in the OrderBook.
        mark_finished(id):
            Marks the task with the given ID as finished.
        finished_orders():
            Returns a list of all finished tasks.
        unfinished_orders():
            Returns a list of all unfinished tasks.
        status_of_programmer(programmer):
            Returns a tuple summarizing a programmer's finished and unfinished tasks,
            including counts and total workloads.
    Notes:
        List comprehensions are used internally to filter tasks and extract programmer names efficiently.
    """
    def __init__(self):
        self.__order_list = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.__order_list.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.__order_list
    
    def programmers(self):
        name_list = [task_objects.programmer for task_objects in self.__order_list]
        return set(name_list)
    
    def mark_finished(self, id: int):
        id_check = [numbs.id for numbs in self.__order_list]
        if id not in id_check:
            raise ValueError(f"{id} does not exist")

        for task_objects in self.__order_list:
            if id == task_objects.id:
                task_objects.mark_finished()
        
        # raise ValueError(f"{id} does not exist")
    
    def finished_orders(self):
        return [finished for finished in self.__order_list if finished.is_finished() == True]
    
    def unfinished_orders(self):
        return [unfinished for unfinished in self.__order_list if unfinished.is_finished() == False]
    
    def status_of_programmer(self, programmer: str):
        
        finished=[]
        unfinished=[]

        for task_object in self.__order_list:
            if task_object.programmer == programmer:
                if task_object.is_finished():
                    finished.append(task_object)
                else:
                    unfinished.append(task_object)
        
        if len(finished) == 0 and len(unfinished) == 0:

            raise ValueError(f"{programmer} does not exist")
        
        return (len(finished), len(unfinished), sum(task_object.workload for task_object in finished), sum(task_object.workload for task_object in unfinished))
        # return ([task_object.description for task_object in finished], sum(task_object.workload for task_object in finished), [task_object.description for task_object in unfinished], sum(task_object.workload for task_object in unfinished))

class OrderBookApp:
    """
    Interactive console app for managing software company tasks.

    Handles user input for adding tasks, listing finished or unfinished ones,
    marking tasks as finished, viewing programmers, and checking a programmer's status.
    Recovers gracefully from invalid input without crashing.

    Attributes:
        __orderbook (OrderBook): Stores all task data.

    Methods:
        instructions() - Displays command options.
        add_order() - Adds a new task.
        list_finished_tasks() - Shows finished tasks.
        list_unfinished_tasks() - Shows unfinished tasks.
        mark_finished() - Marks a task as finished by ID.
        get_programmers() - Lists all programmers.
        get_status() - Displays a programmer’s task summary.
        execute() - Runs the main command loop.
    """
    def __init__(self):
        self.__orderbook = OrderBook()
    
    def instructions(self):
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")


    def add_order(self):
        desc = input("description: ")
        progandeta = input("programmer and workload estimate: ")
        part = progandeta.split()
        try:
            workload = int(part[1])
            self.__orderbook.add_order(desc, part[0], workload)
            print("added!")
        except (ValueError, IndexError):
            print("erroneous input")

    def list_finished_tasks(self):
        finished = self.__orderbook.finished_orders()
        if len(finished) == 0:
            print("no finished tasks")
        else:
            for items in finished:
                print(items)
    
    def list_unfinished_tasks(self):
        unfinished = self.__orderbook.unfinished_orders()
        if len(unfinished) == 0:
            print("no unfinished tasks")
        else:
            for items in unfinished:
                print(items)

    def mark_finished(self):
        id = (input("id: "))
        try:
            self.__orderbook.mark_finished(int(id))
            print("marked as finished")
        except (ValueError):
            print("erroneous input")
        
    def get_programmers(self):
        programmers = self.__orderbook.programmers()
        for items in programmers:
            print(items)

    def get_status(self):
        person = input("programmer: ")

        try:
            status = self.__orderbook.status_of_programmer(person)
            if status is not None:
                print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
        except (ValueError):
            print("erroneous input")

    def execute(self):
        self.instructions()
    
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.get_programmers()
            elif command == "6":
                self.get_status()
            else:
                self.instructions()
        

if __name__ == "__main__":

    app = OrderBookApp()
    app.execute()
    
    


    
    