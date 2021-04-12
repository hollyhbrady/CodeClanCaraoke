import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_one = Room("One", 10)
        self.room_two = Room("Two", 2)
        self.colin = Guest("Colin", "Rocket Man")
        self.hannah = Guest("Hannah", "The Greatest")
        self.roosa = Guest("Roosa", "Vibes")
        self.bemorekind = Song("Be More Kind", "Frank Turner")

    def test_room_has_number(self):
        self.assertEqual("One", self.room_one.number)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room_one.capacity)

    def test_check_in(self):  # this test broke when I adjusted check in function to test capacity
        self.room_one.check_in(self.colin)
        self.assertEqual("Colin", self.room_one.attendees[0].name)

    def test_check_out(self):
        self.room_one.check_in(self.colin)
        self.room_one.check_out(self.colin)
        self.assertEqual(0, len(self.room_one.attendees))

    def test_add_song_to_room(self):
        self.room_one.add_song(self.bemorekind)
        self.assertEqual(1, len(self.room_one.song_list))
    
    def test_capacity_of_room(self):
        self.room_two.check_in(self.hannah)
        self.room_two.check_in(self.roosa)
        self.room_two.check_in(self.colin)
        result = self.room_two.check_capacity()
        self.assertEqual(2, result)

