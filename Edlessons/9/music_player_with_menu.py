# ------------------------------
# Import Modules
# ------------------------------
import input_functions as in_fnc

# ------------------------------
# Dictionaries
# ------------------------------
MAIN_MENU = {
    1 : 'Read in Albums',
    2 : 'Display Albums',
    3 : 'Select an Album to play',
    4 : 'Exit the application'
}

MENU_Opt2 = {
    1 : 'Display all albums',
    2 : 'Display all albums for a particular genre'
}

GENRE = {
    1 : "Pop",
    2 : "Classic",
    3 : "Jazz",
    4 : "Rock"
}

# ------------------------------
# Objects
# ------------------------------
class Album():
    def __init__(self, title, artist, date, genre, tracks):
        self.title = title
        self.artist = artist
        self.year = date
        self.genre = genre
        self.tracks = tracks

class Track():
    def __init__(self, name, location):
        self.name = name
        self.location = location

# ------------------------------
# Functions
# ------------------------------
# --- Tracks reading ---
def read_track(music_file):
    name = music_file.readline().strip()
    location = music_file.readline().strip()
    # print(name)
    # print(location)
    return Track(name,location)

def read_tracks(music_file):
    tracks = []
    i = 0
    count = int(music_file.readline().strip())
    while i != count:
        track = read_track(music_file)
        tracks.append(track)
        i += 1
    return tracks

# --- Tracks printing ---
def print_track(track):
    print(f"Track title is: {track.name}")
    print(f"Track file location is: {track.location}")

def print_tracks(tracks):
    count = len(tracks)
    i = 0
    while i != count:
        print_track(tracks[i])
        i += 1

# --- Albums Reading ---
def read_albums(albums_file):
    albums = []
    count = int(albums_file.readline().strip())
    i = 0
    while i < count:
        album = read_album(albums_file)
        albums.append(album)
        i += 1
    return albums

def read_album(album):
    artist = album.readline().strip()
    
    title = album.readline().strip()
    
    date = album.readline().strip()
    
    genre= int(album.readline().strip())
    # print(title)
    # print(artist)
    # print(date)
    # print(genre)
    tracks = read_tracks(album)
    return Album(title, artist, date, genre, tracks)

# --- Albums Printing ---
def print_album(album):
    print(f"Album title is {album.title}")
    print(f"Album artist is {album.artist}")
    print(f"The album release date is {album.date}")
    print(f"Genre is {album.genre}")
    print(f"{GENRE[album.genre]}")
    print_tracks(album.tracks)

# ------------------------------
# Menus
# ------------------------------
# --- Main Menu ---
def main_menu():
    print('----------------------')
    print('Music Player With Menu')
    print('----------------------')
    i = 1
    while i <= (count := len(MAIN_MENU)):
        print(f'{i}.',MAIN_MENU[i])
        i += 1
    opt = in_fnc.read_integer('--***--\nPlease select an option from 1-4: ')

    return opt

# --- Menu Selecting ---
def select_menu(opt):
    match opt:
        case 1:  
            print(f'You have chosen option {opt} -',MAIN_MENU[opt])
            name = in_fnc.read_string("Please enter the album's file name: ")
            with open(name, 'r') as outfile_album:
                albums = read_albums(outfile_album)
            return True, albums
        case 2:
            menu_opt_2(opt)
            return True
        case 3:
            menu_opt_3(opt)
            return True
        case 4:
            menu_opt_4(opt)
            return False
        case _:
            print(f'You have chosen option {opt}.\nYour option does not exist.\nPlease choose again!')
            return True
    
# --- Menu Option 1 ---
# def menu_opt_1():
    
    
# --- Menu Option 2 ---
def menu_opt_2(opt):
    print(f'You have chosen option {opt} -',MAIN_MENU[opt])

# --- Menu Option 3 ---
def menu_opt_3(opt):
    print(f'You have chosen option {opt} -',MAIN_MENU[opt])

# --- Menu Option 4 ---
def menu_opt_4(opt):
    print(f'You have chosen option {opt} -',MAIN_MENU[opt])

    print('-----------------------')
    print('Goodbye, See you again!')
    print('-----------------------')

# --- Main Function ---
def main():
    run = True
    while run == True:
        opt = main_menu()
        run, album = select_menu(opt)
        print(album)
        
# ------------------------------
# Running the main function
# ------------------------------
if __name__ == "__main__":
    main()