import statistics

def splittingscores(scoreslist: list[str]):
# Splitting and turning it into int
    splitscore_int=[]
    splitscore_str = scoreslist.split()

    for numb in splitscore_str:
       splitscore_int.append(int(numb))   

    return splitscore_int


def splitexandex(splitscore_int : list[int]) -> tuple[list[int], list[int]]:
# splitting the input from user in to examscores and exercise scores and converting them to int
    examscores = []
    exercisescores = []

    for index in range(len(splitscore_int)):

        if index%2 == 0:
            examscores.append(splitscore_int[index])
        else:
            exercisescores.append(splitscore_int[index])
    
    return examscores, exercisescores
    
 

def calcexerpoints(exercisescores : list[int]) -> list[int]:

    percentexerpoints = []

    for index in range(len(exercisescores)):

        percentexerpoints.append(int(exercisescores[index]*0.10))

    return percentexerpoints



def print_statistics(examscores, percentexerpoints : list[int]):
    
    print("Statistics: ")
    # calculating average points
    totalpoints=[]
    totalforaverage=[]

    for index in range(len(examscores)):
        
        totalforaverage.append(examscores[index] + percentexerpoints[index])
        if examscores[index] < 10:
            totalpoints.append(0)
        else: 
            totalpoints.append(examscores[index] + percentexerpoints[index])

    # print(totalpoints)
    # print(totalforaverage)

      
    print(f"Points average: {statistics.mean(totalforaverage):.1f}")

    # calculating pass percentage:

    totalcount = len(totalpoints)
    totalfailed = 0

    for numb in totalpoints:
        if numb <= 14:
            totalfailed+=1

    passpercentage = 100 - totalfailed/totalcount * 100 
    print(f"Pass percentage: {passpercentage:.1f}")


    # calculating grade distribution:


    stars = "*"
    g0=""
    g1=""
    g2=""
    g3=""
    g4=""
    g5=""
    

    for points in totalpoints:

        if points <=14:
            g0 += stars
            
        elif 15<= points <=17:
            g1 += stars
            
        elif 18<= points <=20:
            g2 +=stars
            
        elif 21<= points <=23:
            g3 +=stars
            
        elif 24<= points <=27:
            g4 +=stars
            
        elif 28<= points <=30:
            g5 +=stars
    
    

    results=[g5,g4,g3,g2,g1,g0]
    print(f"Grade distribution: ")

    t=5
    i=0
    
    while t >= 0:
        print(f" {t:>2}: {results[i]}")
        
        t-=1
        i+=1



def input_from_user():
# taking in input from users
    scoreslist= ""

    while True:
        scores = input("Exam points and exercises completed: ")
        if scores == "":
            break
        scoreslist += scores + " "
    return scoreslist


def main():
    # call input_from_user() to get the data
    scoreslist = input_from_user()

    splitscore_int = splittingscores(scoreslist)

    examscores, exercisescores = splitexandex(splitscore_int)

    percentexerpoints = calcexerpoints(exercisescores)

    print_statistics(examscores, percentexerpoints)
   
# Run the program
main()   



# Test helpers directly

# test_input = "2 67 20 6 20 90 12 67 13 53 15 33 11 48 20 62 9 98 17 60 2 100 0 72 12 79 9 7 19 36 17 4 17 5 20 55 8 58 12 26"

# splitscore_int = splittingscores(test_input)

# examscores, exercisescores = splitexandex(splitscore_int)

# percentexerpoints = calcexerpoints(exercisescores)

# print_statistics(examscores, percentexerpoints)
