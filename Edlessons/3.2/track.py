import input_functions as input_functions


class Track:
    def __init__(self, name, location):
        self.name = name
        self.location = location


def read_track():
    # TODO: prompt for and read the track name
    track_name = input_functions.read_string("Enter track name: ")
    # TODO: prompt for and read the track location
    track_location = input_functions.read_string("Enter track location: ")
    # TODO: create and return a Track object
    track = Track(track_name, track_location)
    return track


def print_track(track):
    # TODO: print the track name
    print("Track name:", track.name)
    # TODO: print the track location
    print("Track location:", track.location)
    


def main():
    # TODO: call read_track() and print_track()
    track = read_track()
    print_track(track)
    


# leave this line
if __name__ == "__main__":
    main()
