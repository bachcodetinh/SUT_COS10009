import input_functions 

class Track:
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
    count = int(music_file.readline())
    tracks = []
    i = 0
    while i != count:
        track = read_track(music_file)
        tracks.append(track)
        i += 1
    return tracks

def print_tracks(tracks):
    # print all the tracks use tracks[x] to access each track
    count = len(tracks)
    i = 0
    while i != count:
        print_track(tracks[i])
        i += 1

def print_track(track):
    print(f"Track title is: {track.name}")
    print(f"Track file location is: {track.location}")

# search for track by name
# returns the index of the track or -1 if not found
def search_for_track_name(tracks, search_name):
    found_index = 0
    while found_index < len(tracks):
        if tracks[found_index].name.strip() != search_name:
            found_index +=1
        else:
            return found_index
    return -1
    
def main():
    # Open the file, read the tracks, then close the file
    music_file = open("album.txt", "r")
    tracks = read_tracks(music_file)
    music_file.close()
    print_tracks(tracks)

    search_string = input_functions.read_string("Enter the track name you wish to find: ").strip()
    index = search_for_track_name(tracks, search_string)
    if index >= 0:
        print(f"Found {tracks[index].name} at index {index}")
    else:
        print("Entry not found")

if __name__ == "__main__":
    main()