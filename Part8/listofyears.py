import datetime

def list_years(dates: list):
    # return [d.year for d in dates]
    year_list=[]

    for fulldates in dates:

        year_list.append(fulldates.year)


    return year_list

if __name__=="__main__":

    date1 = datetime.date(2019, 2, 3)
    date2 = datetime.date(2006, 10, 10)
    date3 = datetime.date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)