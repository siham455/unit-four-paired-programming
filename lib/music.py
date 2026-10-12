class Music:

    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        if len(track) == 0:
            raise Exception("Please add a track")
        self.tracks.append(track)

    def list_tracks(self):
        if len(self.tracks) == 0:
            raise Exception("No tracks in the library")
        return self.tracks