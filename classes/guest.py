class Guest:

    def __init__(self, name, fav_song):
        self.name = name
        self.fav_song = fav_song

    def add_song(self, room, guest):
        room.song_list.append(self.guest.fav_song)
    