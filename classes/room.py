class Room:

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.attendees = []

    # function to check in guests to room
    # take a guest by name
    # put in room by number
    # assign to room list