from datetime import date

class Reader:
    def __init__(self,id,name,books_list):
        self.id = id
        self.name = name
        self.books = books_list
    
    def read_book(self,book_title):
        self.books.append({"title" : book_title,
                            "date":date.today()})