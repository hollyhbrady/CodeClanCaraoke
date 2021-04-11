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

    # def test_guest_can_add_song_to_room(self):
    #     self.guest.add_song(self.room_one)
    #     self.assertEqual("Rocket Man", self.room_one.song_list[0].name)

        
    # def test_check_in(self):
    #     self.room_one.check_in(self.guest)
    #     self.assertEqual("Colin", self.room_one.attendees[0].name)
    # def test_add_song_to_room(self):
    #     self.room_one.add_song(self.bemorekind)
    #     self.assertEqual(1, len(self.room_one.song_list))
