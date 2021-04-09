import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 10)
        self.guest = Guest("Colin", "Rocket Man")

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room.capacity)

    def test_check_in(self):
        self.assertEqual("Colin", check_in(self.guest))




