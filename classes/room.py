class Room:

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.attendees = []

    def check_in(self, guest): # tried to add a specific room to add to. Can't make it work
        self.attendees.append(guest)

    def check_out(self, guest):
        self.attendees.append(guest) # cant run without this or ValueError: list.remove(x)
        # if guest in list: Tried to make an if loop to find guest then remove them, cant make it work
        self.attendees.remove(guest)


 