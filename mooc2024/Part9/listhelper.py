from collections import Counter

class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        highest=0
        for number in my_list:
           count=my_list.count(number)
           if count>highest:
               highest=count
               most_common=number
        
        return most_common
        
    @classmethod
    def doubles(cls, my_list: list):
        duplicate_list=[]
        counts = Counter(my_list)

        for key,value in counts.items():
            if value>1:
                duplicate_list.append(key)

        return len(duplicate_list)

        
if __name__=="__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

