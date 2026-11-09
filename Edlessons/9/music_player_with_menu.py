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
    def __init__(self, title, artist, genre, tracks):
        self.title = title
        self.artist = artist
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
    return Track(name,location)

def read_tracks(music_file):
    tracks = []
    i = 0
    while i != (count := int(music_file.readline().strip())):
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
def read_album(music_file):
    artist = music_file.readline().strip()
    title = music_file.readline().strip()
    genre= int(music_file.readline().strip())
    tracks = read_tracks(music_file)
    return Album(title, artist, genre, tracks)

# --- Albums Printing ---
def print_album(album):
    print(f"Album title is {album.title}")
    print(f"Album artist is {album.artist}")
    print(f"Genre is {album.genre}")
    print(f"{GENRE[album.genre]}")
    print_tracks(album.tracks)

# --- Menu Selecting ---
def main_menu():
    i = 1
    print('----------------------')
    print('Music Player With Menu')
    print('----------------------')
    while i != (count := len(MAIN_MENU)):
        print(f'{i}.',MAIN_MENU[i])
        i += 1

    opt = in_fnc.read_integer('--***--\nPlease select an option from 1-4: ')
    print(f'You have chosen option {opt} -',MAIN_MENU[opt])

    return opt
    
# --- Main Function ---
def main():
    main_menu()

# ------------------------------
# Running the main function
# ------------------------------
if __name__ == "__main__":
    main()