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
    4 : 'Update an existing Album',
    5 : 'Exit the application'
}

MENU_Opt2 = {
    1 : 'Display all albums',
    2 : 'Display all albums for a particular genre'
}

MENU_Opt4 = {
    1 : 'Change title',
    2 : 'Change genre'
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

def print_number_track(track_key, tracks, album):
    i = 0
    print()
    while i != len(tracks):
        if (i+1) == track_key:
            play_track(tracks[i], album)
        i += 1
    print()
    

def play_track(track,album):
    print(f"Playing track {track.name} from album {album.title}")
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
    i = 0
    keys = list(MAIN_MENU.keys())
    while i < (len(keys)):
        current_key = keys[i]
        current_value = MAIN_MENU[current_key]
        print(f'{current_key}.',current_value)
        i += 1
    opt = in_fnc.read_integer('\n--***--\nPlease select an option from 1-5: ')

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
                    while i <= len(MENU_Opt2):
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
            if not albums:
                print('You have not Read in any Album.\nPlease choose Option 1 to Read in an album!')
                return True
            else:
                print_option(opt,MAIN_MENU)
                print_all_albums_title(albums)
                run_1 = True
                while run_1 == True:
                    album_number = in_fnc.read_integer(f'Please enter the album number between 1 and {len(albums)}: ')
                    if 1 <= album_number <= len(albums):
                        update_album = albums[album_number - 1]
                        run = True
                        while run == True:
                            i = 1
                            while i <= len(MENU_Opt4):
                                print(f'{i}.',MENU_Opt4[i])
                                i += 1
                            update_option = in_fnc.read_integer('\n--***--\nPlease select an option from 1-2: ')
                            if update_option < 1 or update_option > 2:
                                print(f'You have chosen option {update_option}.\nYour option does not exist.\nPlease choose again!')
                                run = True
                            else:
                                menu_opt_4(update_option, update_album)
                                run = False
                        run_1 = False
                    else:
                        print('Your album number does not exist.')
                        run_1 = True
                return True
        case 5:
            menu_opt_5(opt)
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
            if not albums[i].tracks:
                print(f'Album {albums[i].title} is empty\n')
                return
            else:
                print('Album is found: ')
                print('Album number', i + 1,'-',albums[i].title)
                print_tracks(albums[album_key-1].tracks)
        i += 1
    print()   
    track_key = in_fnc.read_integer('Please enter the track number: ')
    print_number_track(track_key,albums[album_key-1].tracks,albums[album_key-1])

# --- Menu Option 2 ---
def menu_opt_4(update_option, update_album):
    match update_option:
        case 1:
            update_album.title = in_fnc.read_string('Please enter new title: ')
        case 2:
            update_album.genre = genre_select()
    print_album(update_album)
    in_fnc.read_string('Please enter to return to Main Menu: ')
    return

# --- Menu Option 5 ---
def menu_opt_5(opt):
    print_option(opt,MAIN_MENU)
    print('-----------------------')
    print('Goodbye, See you again!')
    print('-----------------------')

# --- Genre Menu Selecting ---
def genre_select():
    run = True
    while run == True:
        i = 1
        while i <= len(GENRE):
            print(f'{i}.',GENRE[i])
            i += 1
        opt = in_fnc.read_integer('\n--***--\nPlease select genre from 1-2-3-4: ')
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