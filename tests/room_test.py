import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("One", 10)
        self.guest = Guest("Colin", "Rocket Man")

    def test_room_has_number(self):
        self.assertEqual("One", self.room.number)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room.capacity)

    def test_check_in(self):
        self.room.check_in(self.guest)
        self.assertEqual("Colin", self.room.attendees[0].name)

    # def test_check_out(self):
    #     self.assertEqual([], )

    


