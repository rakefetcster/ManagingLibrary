# managing_library
#***********************************
To start work run python with main.py
#***********************************

This program is only server - python program for managing a library
it show good practice with classes in python.
The program start with a menu - in python


The Program
The program manages ONLY 1 Library object.
The program starts with pre-defined 2 Books object on EACH shelf. These books
are pulled from a proper collection in a MongoDB data base (The collection
stores 6 Books records – for 3 Shelves)
This library management system is accessible only to registered library
employees. To start working with system, the employee must login with his
username and email login details. These details will be verified against the REST
API at https://jsonplaceholder.typicode.com/users

If there’s an employee with that username and email he will be logged in and will get the
following menu ( in infinite loop) :
• - “For adding a book - Press 1”.
• - “For deleting a book - Press 2”.
• - “For changing books locations - Press 3”.
• - “For registering a new reader - Press 4”.
• - “For removing a reader - Press 5”.
• - “For searching books by author – Press 6.”
• - “For reading a book by a reader – Press 7.”
• - “For ordering all books – Press 8.”
• - “For saving all data – Press 9”.
• - “For loading data – Press 10”.
• - “For exit – Press 11”.
