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
    
if __name__ == "__main__":
    
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
    status = orders.status_of_programmer("Brandon")
    print(status)


    
    