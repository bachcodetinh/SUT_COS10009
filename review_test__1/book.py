import input_functions as in_fnc

class Book:
    def __init__(self, book_id, author, title, shelf_number):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.shelf_number = shelf_number

def read_a_book():
    book_id = in_fnc.read_integer('Enter book id: ')
    author = in_fnc.read_string('Enter book author: ')
    title = in_fnc.read_string('Enter book title: ')
    shelf_number = in_fnc.read_integer('Enter book shelf number: ')
    book = Book(book_id, author, title, shelf_number)
    return book

def read_books():
    book_array = []
    num_book = in_fnc.read_integer('How many books are you entering: ')
    i = 0
    for i in range(num_book):
        book = read_a_book()
        book_array.append(book)
    return book_array

def print_a_book(book):
    print('Id',book.book_id)
    print('Author',book.author)
    print('Title',book.title)
    print('Shelf Number',book.shelf_number)

def print_books(book_array):
    for i in range(len(book_array)):
        print_a_book(book_array[i])

def main():
    book_list = read_books()
    print_books(book_list)

if __name__ == '__main__':
    main()