import input_functions 

GENRE_NAMES = {
    1: "Pop",
    2: "Classic",
    3: "Jazz",
    4: "Rock"
}


class Album:
    # Optional: you may add an __init__ method
    pass


def read_album():
    print("Enter Album")

    album_name = input_functions.read_string("Enter album name: ")
    artist_name = input_functions.read_string("Enter artist name: ")
    genre_number = input_functions.read_integer_in_range("Enter Genre between 1-4: ",1,4)

    album = Album()
    album.name = album_name
    album.artist = artist_name
    album.genre = genre_number

    return album


def print_album(album):
    print("Album information is:")
    print(album.name)
    print(album.artist)
    print('Genre is',album.genre)
    print(GENRE_NAMES[album.genre])


def main():
    album = read_album()
    print_album(album)


if __name__ == "__main__":
    main()
