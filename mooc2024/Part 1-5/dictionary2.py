def factorials(n: int):

    dis={}
    facts=1

    for numb in range(1, n+1):

        facts*=numb
        dis[numb]=facts


    return dis



if __name__ == "__main__":

    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])