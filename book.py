# Modularization - separating functionality into separate files
# separates concerns and organize our code into "categories" 

# managing individual instances of a book
# what are some attributes a book could have
# what are some methods i may need for a book
# how are those methods going to interact with my book attributes
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # managing if the book is available to check out
        self.is_available = True #setting a default attribute
    
    # method for checking out a book
    # check if is_available is equal to True
    def check_out(self):
        # check if is_available is True
        if self.is_available:
            # if it is, we set it to False
            # because we can consider this book checked out
            self.is_available = False
            # return True because we will use this function to see if we can succesfully check out a book object
            return True
        return False
    
    def return_book(self):
        # returns our book so we set self.is_available back to True
        self.is_available = True

# this is for the import example but not a necessary part of the library example  
publisher = "Penguin Books"