   # Task 8.1 T - use the code from the previous tasks to complete this:

GENRE = {
    1 : "Pop",
    2 : "Classic",
    3 : "Jazz",
    4 : "Rock"
}

class Album():
    # NB: you will need to add tracks to the following and finish the initialiser

    # complete the missing code:
    def __init__(self, title, artist, genre, tracks):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.tracks = tracks

class Track():
    def __init__(self, name, location):
        self.name = name
        self.location = location

# Reads in and returns a single track from the given file
def read_track(music_file):
    name = music_file.readline().strip()
    location = music_file.readline().strip()
    return Track(name,location)

# Returns an array of tracks read from the given file
def read_tracks(music_file):
    count = int(music_file.readline().strip())
    tracks = []
    i = 0
    while i != count:
        track = read_track(music_file)
        tracks.append(track)
        i += 1
    return tracks

# Takes an array of tracks and prints them to the terminal
def print_tracks(tracks):
    count = len(tracks)
    i = 0
    while i != count:
        print_track(tracks[i])
        i += 1

# Reads in and returns a single album from the given file, with all its tracks
def read_album(music_file):
    artist = music_file.readline().strip()
    title = music_file.readline().strip()
    genre= int(music_file.readline().strip())
    tracks = read_tracks(music_file)
    return Album(title, artist, genre, tracks)

# Takes a single album and prints it to the terminal along with all its tracks
def print_album(album):
    print(f"Album title is {album.title}")
    print(f"Album artist is {album.artist}")
    print(f"Genre is {album.genre}")
    print(f"{GENRE[album.genre]}")
    print_tracks(album.tracks)
    # print out the tracks

# Takes a single track and prints it to the terminal
def print_track(track):
    print(f"Track title is: {track.name}")
    print(f"Track file location is: {track.location}")

# Reads in an album from a file and then print the album to the terminal
def main():
    file_name = "album.txt"
    music_file = open(file_name, "r")
    album = read_album(music_file)
    music_file.close()
    print_album(album)

if __name__ == "__main__":
    main()