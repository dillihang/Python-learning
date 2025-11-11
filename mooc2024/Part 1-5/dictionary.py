def times_ten(start_index: int, end_index: int):

    dis={}


    for numbs in range(start_index, end_index+1):
        
        dis[numbs]=numbs*10


    return(dis)








if __name__ == "__main__":

    d = times_ten(3, 6)
    print(d)