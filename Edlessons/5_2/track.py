from typing import TextIO          

class Track:
    def __init__(self, name, location):
        self.name = name
        self.location = location

def read_track(file_name: TextIO) -> Track:   
    track_name = file_name.readline().strip()
    track_location = file_name.readline().strip()
    track = Track(track_name, track_location)
    return track

def print_track(track: Track) -> None:
    print("Track name:", track.name)
    print("Track location:", track.location)

def main():
    file = open("track.txt", "r")
    track = read_track(file)
    file.close()
    print_track(track)

if __name__ == "__main__":
    main()