import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 10)

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)



