# driver code for the libary management system
from library import Library
from book import Book

def main():
    # instantiates a library object
    library = Library() #even if the class doesnt take any arguments for the init, you always need parentheses

    while True:
        action = input("What would you like to do: (add, lend, return, search, exit) （。＾▽＾）")
        if action == "exit":
            break
        try: 
            if action == "add":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                # instantiate our book class to create a book object
                new_book = Book(title, author)
                # calls the library add_book method to add the book object to library.books -> self.books
                library.add_book(new_book)
                print(f"Added book: {title}")
            elif action == "lend":
                title = input("Which book would you like to lend? ")
                library.lend_book(title)
            
            elif action == "return":
                title = input("Enter book title to return: ")
                library.return_book(title)
            elif action == "search":
                title = input("Which would you like to search for? ")
                book = library.find_book(title)
                if book:
                    availability = "available" if book.is_available else "not available"
                    print(f"{title} by {book.author} is {availability}")
                else:
                    print(f"{title} not found")
        except Exception as e:
            print(f"An error occurred: {e}")

# main()