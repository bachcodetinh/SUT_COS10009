class Track:
    def __init__(self, name, location):
        self.name = name
        self.location = location

def read_tracks(music_file):
    count = int(music_file.readline().strip())
    tracks = []
    i = 0
    while i != count:
        track = read_track(music_file)
        tracks.append(track)
        i += 1
    return tracks
def read_track(music_file):
    name = music_file.readline().strip()
    location = music_file.readline().strip()
    return Track(name,location)

def print_tracks(tracks):
    count = len(tracks)
    i = 0
    while i != count:
        print_track(tracks[i])
        i += 1
def print_track(track):
    print(f"Track Name: {track.name}")
    print(f"Track Location: {track.location}")

def main():
    music_file = open("input.txt", "r") 
    tracks = read_tracks(music_file)
    print_tracks(tracks)
    music_file.close()

if __name__ == '__main__':
    main()