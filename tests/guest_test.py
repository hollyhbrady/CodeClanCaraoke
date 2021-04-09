import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Colin", "Rocket Man")

    def test_guest_has_name(self):
        self.assertEqual("Colin", self.guest.name)
