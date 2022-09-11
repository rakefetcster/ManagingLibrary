class Shelf:
    def __init__(self):
        self.books_list = list()
        self.is_shelf_full = False

    def add_book(self,book_obj):
        if not self.is_shelf_full and len(self.books_list) < 5:
            self.books_list.append(book_obj)
            if len(self.books_list) == 5:
                self.is_shelf_full = True
            
        
        

    def replace_books(self,num1,num2):
        if 1 <= num1 and num1 <=5 and 1 <= num2 and num2 <=5:
            is_ok_to_replace = True
            books_dict = dict()
            for count,item in enumerate(self.books_list):   
                books_dict[count] = item
            if books_dict[num1-1]: 
                item1 = books_dict[num1-1]
            else:
                print("There is no value in place {} in the books list".format(num1))
                is_ok_to_replace = False
                
            if books_dict[num2-1]: 
                item2 = books_dict[num2-1]
            else:
                print("There is no value in place {} in the books list".format(num2))
                is_ok_to_replace = False
            if is_ok_to_replace:
                books_dict[num1-1] = item2
                books_dict[num2-1] = item1
                self.books_list = books_dict.values()
        



    