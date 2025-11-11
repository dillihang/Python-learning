def invert(dictionary: dict):

    new_dict={}

    for keys, values in dictionary.items():

        new_dict[values]=keys

    dictionary.clear()

    for k,v in new_dict.items():

        dictionary[k]=v



def main():
  
   s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
   invert(s)
   print(s)


if __name__ == "__main__":

    main()