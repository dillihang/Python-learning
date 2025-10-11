from book import Book

def older_book(book1: Book, book2: Book):

    if book1.year==book2.year:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")
    elif book1.year<book2.year:
        print(f"{book1.name} is older, it was published in {book1.year}")
    else:
        print(f"{book2.name} is older, it was published in {book2.year}")


def books_of_genre(books: list, genre: str):

    my_list=[]
    
    for items in books:
        if items.genre==genre:
            my_list.append(items)

    return my_list

if __name__=="__main__":

    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    # older_book(python, everest)
    # older_book(python, norma)

    books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

    print("Books in the crime genre:")
    for book in books_of_genre(books, "crime"):
        print(f"{book.author}: {book.name}")

