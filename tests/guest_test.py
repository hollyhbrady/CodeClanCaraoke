import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Colin", "Rocket Man")
        self.room_one = Room("One", 10)

    def test_guest_has_name(self):
        self.assertEqual("Colin", self.guest.name)

    def test_guest_has_fav_song(self):
        self.assertEqual("Rocket Man", self.guest.fav_song)    

    def test_guest_can_add_song_to_room(self):
        self.assertEqual("Rocket Man", self.room_one.song_list)
