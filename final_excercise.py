from library import Library
from book import Book
# Further expand you character class
# Create a class to manage your characters
# give that class the option to add a character
# and display each character

# Create a new attribute on your character to manage a collection of inventory objects
library = Library()
book = Book("LOTR", "Author")
library.add_book(book)

# example for displaying all books
for book in library.books:
    print(book.title)


class Character:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name
        # manage instances of an Item class
        self.inventory = []

    def add_item(self):
        item_name = input("What are you adding to your inventory? ")
        damage = input("How powerful is that item? ")
        item = Item(item_name, damage)
        self.inventory.append(item)

class Item:
    
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        

class CharacterManager:
    def __init__(self):
        self.characters = []

    # method to add character object to self.characters

    # method to display information about character objects in the list