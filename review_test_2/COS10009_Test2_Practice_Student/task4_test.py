from task4_book import Book


def main():
    # Create a Book, assign its attributes, and print them.
    book = Book()
    book.id = 25
    book.title = 'Python Basics'
    book.price = 19.5222
    print(f'id: {book.id}')
    print(f'title: {book.title}')
    print(f'price: {book.price:.1f}')
    pass


if __name__ == "__main__":
    main()
