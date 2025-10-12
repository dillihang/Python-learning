"""
Series management program.

- Series class: represents a TV show with title, seasons, genres, and ratings.
- rate(): add a rating and update average.
- minimum_grade(): filter a list of Series by minimum average rating.
- includes_genre(): filter a list of Series by genre.

Example usage:
Create Series objects, rate them, store in a list, and use the functions to filter or display series.
"""

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.genre = genres
        self.title = title
        self.seasons = seasons
        self.ratingscount = 0
        self.ratingstotal = 0
        self.avgratings = 0


    def rate(self, rating_num: int):

        self.ratingscount+=1
        self.ratingstotal+= rating_num
        self.avgratings = self.ratingstotal/self.ratingscount

    def __str__(self): 
        genre_string= ", ".join(self.genre)
        return f"{self.title} ({self.seasons} seasons) \ngenres: {genre_string} \n{self.ratingscount} ratings, average {self.avgratings} points"

def minimum_grade(rating: float, series_list: list):
        
    minimum_list=[]

    for series in series_list:

        if series.avgratings>= rating:

            minimum_list.append(series)
            
    return minimum_list

def includes_genre(genre: str, series_list: list):

    genre_list=[]

    for series in series_list:

        if genre in series.genre:
            genre_list.append(series)

    return genre_list


if __name__=="__main__":

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]


    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)