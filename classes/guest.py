class Guest:

    def __init__(self, name, fav_song):
        self.name = name
        self.fav_song = fav_song

    def add_song(self, room):
        room.song_list.append(self.fav_song)
    