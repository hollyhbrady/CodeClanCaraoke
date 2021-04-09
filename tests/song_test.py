import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Be More Kind", "Frank Turner")

    def test_song_has_name(self):
        self.assertEqual("Be More Kind", self.song.name)
