from reader import Reader
from datetime import date
from book import Book


class Library(object):
    def __init__(self,shelves,readers):
        self.shelves_list = shelves
        self.readers_list = readers

    def is_there_place_for_new_book(self):
        for shelf in self.shelves_list:
            if not shelf.is_shelf_full:
                return True

    def add_new_book(self,obj_book):
        ok = False
        library_full = 0
        for shelf_obj in self.shelves_list:
            library_full +=1 
            if not shelf_obj.is_shelf_full:
                shelf_obj.add_book(obj_book)
                ok = True
                break
            
        if library_full > 3:
            print("Error - The library is full")
        return ok

      
    def delete_book(self,book_title):
        ok = False
        for shelf in self.shelves_list:
            for book in shelf.books_list:
                if book_title == book.title:
                    shelf.books_list.remove(book)
                    ok = True
        return ok

    def change_locations(self,book_title1,book_title2):
        ok_first = False
        ok_second = False
        for shelf in self.shelves_list:
            for book_obj in shelf.books_list:
                if book_title1 in book_obj.title:
                    first = book_obj
                    ok_first = True
                if book_title2 in book_obj.title:
                    second = book_obj
                    ok_second = True
        if ok_first and ok_second:
            for shelf in self.shelves_list:
                for book_obj in shelf.books_list:
                    if book_title1 in book_obj.title:
                        first = book_obj
                        shelf1 = shelf
                    if book_title2 in book_obj.title:
                        second = book_obj
                        shelf2 = shelf
                    
            for shelf in self.shelves_list:
                if shelf == shelf1:
                    shelf.books_list.remove(first)
                    shelf.books_list.append(second)
                if shelf == shelf2:
                    shelf.books_list.remove(second)
                    shelf.books_list.append(first)
            return True
        else:
            return False
        
   
    def order_books(self):
        for shelf in self.shelves_list:
            book_dict = {}
            for book_obj in shelf.books_list:
                book_dict[book_obj.num_of_pages] = book_obj
            
            new_list = sorted(book_dict.keys())
            shelf.books_list.clear() 
            close_list = list()
            for val in new_list:
                shelf.books_list.append(book_dict[val])
                del book_dict[val]


    def register_reader(self,reader_name,id):
        reader_obj = Reader(id,reader_name,[])
        self.readers_list.append(reader_obj)
    
    def remove_reader(self,reader_name):
        for reader in self.readers_list:
            if reader.name == reader_name:
                self.readers_list.remove(reader)
                return True
        return False

    def reader_read_book(self,reader_id,book_title):
        ok = False
        for shelf in self.shelves_list:
            for book_obj in shelf.books_list:
                if book_obj.title == book_title: 
                    ok = True
                    break
        if ok:
            for reader in self.readers_list:
                if reader.id == int(reader_id):
                    reader.books.append({"book title" : book_title,
                                        "date taken": date.today().strftime("%d/%m/%Y %H:%M:%S")})
                    
        else:
            print("Error, There is no book called {} in the library ".format(book_title))
        return ok
        
    
    def search_by_auther(self,auther_name):
        ok = False
        for shelf in self.shelves_list:
            for book_obj in shelf.books_list:
                if book_obj.auther == auther_name:
                    if not ok:
                        print("The list of books for the author {} is:".format(auther_name))
                    print(book_obj.title +"\n")
                    ok = True
        return ok

    def all_library_data(self):
        full_dict = dict()
        full_list = list()
        reader_list = list()
        for shelf in self.shelves_list:
            shelf_dict = {}
            shelf_dict["is_shelf_full"] = str(shelf.is_shelf_full)
            shelf_list = []
            for book_obj in shelf.books_list:
                shelf_list.append({"auther" : book_obj.auther,
                                   "title" : book_obj.title,
                                   "num_of_pages" :  book_obj.num_of_pages})
            shelf_dict["books"] = shelf_list
            full_list.append(shelf_dict)
        full_dict["shelves"] = full_list

        for reader in self.readers_list:
            reader_list.append({"id" :reader.id,
                        "name" : reader.name,
                        "books" : reader.books })
        full_dict["readers"] = reader_list
        return full_dict
    
    def get_data_from_file(self,data):
        if self.is_there_place_for_new_book():
            for books_dict in data["shelves"]:
                for book in books_dict["books"]:
                    book_obj = Book(book['auther'],book['title'],book['num_of_pages'])
                    if self.is_there_place_for_new_book():
                        self.add_new_book(book_obj)
                    else:
                        break
        else:
            print("There is no room for a new book in the library")
        id_list = list()
        for reader in self.readers_list:
            id_list.append(int(reader.id))
        for reader_dict in data["readers"]:
            reader_obj = Reader(int(reader_dict['id']),reader_dict['name'],reader_dict['books'])
            if reader_dict['id'] not in id_list:
                self.readers_list.append(reader_obj)