# ------------------------------
# Import Modules
# ------------------------------
import input_functions as in_fnc
import time

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
        self.date = date
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
    i = 0
    while i != len(tracks):
        print('\nTrack number',i+1)
        print_track(tracks[i])
        i += 1

def print_number_track(track_key, tracks):
    i = 0
    print()
    while i != len(tracks):
        if (i+1) == track_key:
            print_track(tracks[i])
        i += 1
    print()
    time.sleep(3)

# --- Albums Reading ---
def read_albums(albums_file, albums):
    count = int(albums_file.readline().strip())
    i = 0
    while i < count:
        album = read_album(albums_file)
        albums.append(album)
        i += 1

def read_album(album):
    artist = album.readline().strip()
    title = album.readline().strip()
    date = album.readline().strip()
    genre= int(album.readline().strip())
    tracks = read_tracks(album)
    return Album(title, artist, date, genre, tracks)

# --- Albums Printing ---
def print_all_albums_title(albums):
    i = 0
    print()
    while i != len(albums):
        print('ALbum key:', i + 1,' ',albums[i].title)
        i += 1
    print()

def print_genre_albums(genre, albums):
    i = 0
    print()
    while i != len(albums):
        if albums[i].genre == genre:
            print('Album number', i + 1,'-',albums[i].title)
        i += 1
    print()

def print_album(album):
    print(f"Album title is {album.title}")
    print(f"Album artist is {album.artist}")
    print(f"The album release date is {album.date}")
    print(f"Genre is {album.genre} - {GENRE[album.genre]}")
    print_tracks(album.tracks)

# ------------------------------
# Menus
# ------------------------------
# --- Main Menu ---
def main_menu():
    print('----------------------')
    print('Music Player Main Menu')
    print('----------------------\n')
    i = 1
    while i <= (count := len(MAIN_MENU)):
        print(f'{i}.',MAIN_MENU[i])
        i += 1
    opt = in_fnc.read_integer('\n--***--\nPlease select an option from 1-4: ')

    return opt

# --- Menu Selecting ---
def select_menu(opt, albums):
    match opt:
        case 1:  
            print_option(opt,MAIN_MENU)
            name = in_fnc.read_string("Please enter the album's file name: ")
            with open(name, 'r') as outfile_album:
                read_albums(outfile_album, albums)
            return True
        case 2:
            if not albums:
                print('You have not Read in any Album.\nPlease choose Option 1 to Read in an album!')
                return True
            else:
                run = True
                while run == True:
                    i = 1
                    while i <= (count := len(MENU_Opt2)):
                        print(f'{i}.',MENU_Opt2[i])
                        i += 1
                    opt = in_fnc.read_integer('\n--***--\nPlease select an option from 1-2: ')
                    if opt < 1 or opt > 2:
                        print(f'You have chosen option {opt}.\nYour option does not exist.\nPlease choose again!')
                        run = True
                    else:
                        menu_opt_2(opt,albums)
                        run = False
                        return True
            return True
        case 3:
            if not albums:
                print('You have not Read in any Album.\nPlease choose Option 1 to Read in an album!')
                return True
            else:
                run = True
                while run == True:
                    album_key = in_fnc.read_integer('Please enter the album number: ')
                    if 1 <= album_key <= len(albums):
                        menu_opt_3(album_key,albums)
                        run = False
                    else:
                        print('Your album number does not exist.')
                        run = True
                return True
        case 4:
            menu_opt_4(opt)
            return False
        case _:
            print(f'You have chosen option {opt}.\nYour option does not exist.\nPlease choose again!')
            return True    
    
# --- Menu Option 2 ---
def menu_opt_2(opt,albums):
    print_option(opt,MENU_Opt2)
    match opt:
        case 1:
            print_all_albums_title(albums)
        case 2:
            genre = genre_select()
            print_genre_albums(genre,albums)

# --- Menu Option 3 ---
def menu_opt_3(album_key,albums):
    i = 0
    print()
    while i != len(albums):
        if (i+1) == album_key:
            print('Album is found: ')
            print('Album number', i + 1,'-',albums[i].title)
            print_tracks(albums[album_key-1].tracks)
        i += 1
    print()   
    track_key = in_fnc.read_integer('Please enter the track number: ')
    print_number_track(track_key,albums[album_key-1].tracks)

# --- Menu Option 4 ---
def menu_opt_4(opt):
    print_option(opt,MAIN_MENU)
    print('-----------------------')
    print('Goodbye, See you again!')
    print('-----------------------')

# --- Genre Menu Selecting ---
def genre_select():
    run = True
    while run == True:
        i = 1
        while i <= (count := len(GENRE)):
            print(f'{i}.',GENRE[i])
            i += 1
        opt = in_fnc.read_integer('\n--***--\nPlease select genre from 1-4: ')
        if opt < 1 or opt > 4:
            print(f'You have chosen genre {opt}.\nYour genre does not exist.\nPlease choose again!')
            run = True
        else:
            print_option(opt,GENRE)
            run = False
    return opt

# ------------------------------
# Utilities
# ------------------------------      
# --- Print Option ---
def print_option(opt,opt_name):
    print(f'\nYou have chosen option {opt} -',{opt_name[opt]},'\n')

# --- Main Function ---
def main():
    run = True
    albums = []
    while run == True:
        opt = main_menu()
        run = select_menu(opt, albums)
    
# ------------------------------
# Running the main function
# ------------------------------
if __name__ == "__main__":
    main()