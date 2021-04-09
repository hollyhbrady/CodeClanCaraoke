class Room:

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.attendees = []

    def check_in(self, guest):
        self.attendees.append(guest)
