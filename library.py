# responsible for managing several instances of Book
# how can we manage the books?
# how do we find books within our library attributes
# what kind of attributes within my library

# import from book.py and get the book class
# importing entire module
import random
#            useing the module and naming the method we want to use
random_num = random.choice([1,2,3,4,5,6,7,8,9,10])
print(random_num)

# naming module methods we want to use
from random import randint
print(randint(1,10))

# the same rules will apply with custom modules
# when we import from other python files we've created
# we can explicitly state which classes, functions, variables, etc.. we want to use
# or we can import the whole file
import book

# creating an instance of the book class
# book - python file Book - class of Book
my_book = book.Book("LOTR", "Tolkien")
print(my_book.title)
print(my_book.author)
# referencing the publisher variable
print(book.publisher)
# only importing the Book class
# from python file import class
from book import Book

another_book = Book("The Magicians", "Some guy")
print(another_book.title)
print(another_book.author)

# alias our imports 
# from location import something as something_else
# from book import Book as b

# another_book = b("1984", "George")
# print(another_book.title)
# print(another_book.author)


class Library:
    
    def __init__(self):
        # collection of book objects - object composition
        # object composition - when instances of a class make up the attributes of another class
        self.books = []
    
    def add_book(self, book):
        # add a book object to our list of books
        # we gather book information through driver code
        self.books.append(book)

    def find_book(self, title):
        # loop through our list of book objects and match a title to a title attribute
        # for each book object in self.books check if the title passed into our method
        # matches the title attribute of a book object
        for book in self.books:
            if book.title == title:
                # returns a whole book object
                return book
        return None # returns None if we cant find the book in our list
    # will be used in the lend_book method below
    
    def lend_book(self, title):
        book = self.find_book(title)
        # if we get a book object back and we're able to check the book out
        # meaning the is_available attribute is currently true
        if book and book.check_out():
            print(f"Book {book.title} has been lent out")
        else:
            print(f"{title} is not available")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
            # book.is_available = True
            print(f"Book {title} has been returned!")
        else:
            print(f"Book {title} is not in our library")


    
   