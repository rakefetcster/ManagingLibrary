from book import Book
from shelf import Shelf
from library import Library
import requests
import os
import sys
import json
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(port=27017)
db = client["books"]
books_collection = db["booksDb"]
books_data = books_collection.find({})
obj_shelf1 = Shelf()
obj_shelf2 = Shelf()
obj_shelf3 = Shelf()
book_list = list()
for this_book in books_data:
    book_list.append(Book(this_book["auther"],this_book["title"],int(this_book["num_of_pages"])))
book_list1 = book_list[0:2]
book_list2 = book_list[2:4]
book_list3 = book_list[4:6]
all_shelf = list()
for this_book in book_list1:
    obj_shelf1.add_book(this_book)
for this_book in book_list2:
    obj_shelf2.add_book(this_book)
for this_book in book_list3:
    obj_shelf3.add_book(this_book) 
all_shelf.append(obj_shelf1)
all_shelf.append(obj_shelf2)
all_shelf.append(obj_shelf3)
obj_library=Library(all_shelf,[])
reader_id = 0

user_name = input("Please write your username \n")
email = input("Please write your email address \n")
try:
    resp = requests.get("https://jsonplaceholder.typicode.com/users?username="+user_name+"&email="+email)
except requests.exceptions.RequestException as e:  
    raise SystemExit(e)
user = resp.json()
if len(user) > 0:
    ans=True

    while ans:
        print ("""
        1.For adding a book - Press 1.
        2.For deleting a book - Press 2.
        3.For changing books locations - Press 3.
        4.For registering a new reader - Press 4.
        5.For removing a reader - Press 5.
        6.For searching books by auther - Press 6.
        7.For reading a book by a reader - Press 7.
        8.For ordering all books - Press 8.
        9.For saving all data - Press 9.
        10.For loading data - Press 10.
        11.For exit - Press 11.
        """)
        ans=input("What would you like to do? ") 
        if ans=="1": 
            ok = False
            auther = input("Please write the author's name \n")
            title = input("Please write the name of the book \n")
            num_of_pages = input("Please write the number of pages of the book - must be a natural number \n")
            try:
                num = int(num_of_pages)
                obj_book = Book(auther,title,num)
                ok = obj_library.add_new_book(obj_book)
            except ValueError:
                print("Error - The number of pages in the book does not include a natural number")
            if ok:
                print("The book {} has been added to the library\n".format(title))

        elif ans=="2":
            book_title = input("please write the book title you want to remove \n")
            ok = obj_library.delete_book(book_title)
            if ok:
                print("The book was successfully removed\n")
            else:
                print("The book was not found in the library and therefore was not removed either\n")

        elif ans=="3":
            ok = False
            first_book = input("Please write the name of the first book for which you want to change location \n")
            second_book = input("Please write the name of the second book for which you want to change location \n")
            ok = obj_library.change_locations(first_book,second_book)
            if ok:
                print("The place between the books has been changed\n")
            else:
                print("Error - One of the books was not found")
        elif ans=="4":
            reader_name = input("please write the reader name \n")
            reader_id +=1
            obj_library.register_reader(reader_name,reader_id)
            print("Reader name successfully added\n ") 
        elif ans=="5":
            reader_name = input("Please write the name of the caller to remove \n")
            ok = obj_library.remove_reader(reader_name)
            if ok:
                print("Reader name {} successfully removed \n ".format(reader_name))  
            else:
                print("The reader is not in the list of readers, so the operation was not performed\n")
        elif ans=="6":
            auther_name = input("Please write the author's name\n")
            ok = obj_library.search_by_auther(auther_name)
            if not ok:
                print("No books were found in the library for the author {}\n".format(auther_name)) 
        elif ans=="7":
            reader_id = input("Please write the id of the reader \n")
            book_title = input("Please write the name of the book he wants to read \n")
            ok = obj_library.reader_read_book(reader_id,book_title)
            if ok:
                print("The book has been successfully added\n ") 
        elif ans=="8":
            obj_library.order_books()
            print("The books were reorganized on each shelf according to the number of pages in each book\n ") 
        elif ans=="9":
            file_name = input("Please write the file name to save the data \n")
            shelf_dict = obj_library.all_library_data()
            if file_name.endswith(".json"):
                json_file = file_name
            else:
                json_file = file_name + ".json"
            try:
                with open(os.path.join(sys.path[0],json_file),'w') as f: 
                    f.write(json.dumps(shelf_dict))
            except FileNotFoundError:
                print('The file {} does not exist'.format(json_file))
            print("The file was created successfully\n") 
        elif ans=="10":
            file_name = input("Please write the name of the file from which the data will be read\n")
            if file_name.endswith(".json"):
                json_file = file_name
            else:
                json_file = file_name + ".json" 
            try:
                with open(os.path.join(sys.path[0],json_file),'r') as f: 
                    data = json.load(f)
                    obj_library.get_data_from_file(data)
            except IOError:
                print("Could not read file:", json_file)
                
            print("The data was read successfully\n") 
        elif ans=="11":
            ans = False
            print("Goodbye\n ") 
        elif ans !="":
            print(" This is not valid choice, please try again\n") 
else:
    ("Error - The user does not exist")