import math

def get_station_data(filename: str):

    stations={}

    with open(filename) as file:

        for line in file:
            line=line.strip()
            part=line.split(";")

            if part[0]=="Longitude":
                continue            

            stations[part[3]]= (float(part[0]),float(part[1]))


    return stations


def distance(stations: dict, station1: str, station2: str):

    # longitude1=stations[station1][0]
    # longitude2=stations[station2][0]
    # latitude1=stations[station1][1]
    # latitude2=stations[station2][1]

    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km=(longitude1-longitude2)*55.26
    y_km=(latitude1-latitude2)*111.2

    distance_km=math.sqrt(x_km**2+y_km**2)

    return distance_km


def greatest_distance(stations: dict):

    my_list={}
    final=""


    for locations in stations:
        for other_locations in stations:
            if locations==other_locations:
                continue
            d = distance(stations, locations , other_locations)
            my_list[locations, other_locations]=d
            

    
    greatest=0
    greatest_tup=()
    for numbs in my_list:
        if my_list[numbs]>greatest:
            greatest=my_list[numbs]
            greatest_tup=numbs
    

    return(greatest_tup[0]), (greatest_tup[1]), (greatest)



def main():

    if __name__ == "__main__":
        
        stations = get_station_data('Part 6/stations1.csv')
        # d = distance(stations, "Laivasillankatu", "Kapteeninpuistikko")
        # print(d)
        # d = distance(stations, "Laivasillankatu", "Kaivopuisto")
        # print(d)

        station1, station2, greatest = greatest_distance(stations)
        print(station1, station2, greatest)

main()