class SongInfo:
    def __init__(self, artist, track, link):
        self.artist = artist
        self.track = track
        self.link = link

    def to_string(self):
        return ('Here\'s what I found! \n\nArtist: {0} \nSong: {1} \nLink: {2} \n'
                .format(self.artist, self.track, self.link))
