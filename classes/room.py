class Room:

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.attendees = []
        self.song_list = []

    def check_in(self, guest): # tried to add a specific room to add to. Can't make it work
        self.attendees.append(guest)

    # def check_out(self, person, attendees):
    #     for person in attendees:
    #         if person == guest.name:
    #             self.attendees.remove(person)
        # Tried to make an if loop to find guest then remove them, cant make it work
                
    def check_out(self, guest):
        self.attendees.append(guest) # cant run without this or ValueError: list.remove(x)
        self.attendees.remove(guest)

    def add_song(self, song):
        self.song_list.append(song) # which room? cant make it work to add this
    
    def c
    #check the len of guest list
    #if > capacity 
    #pop() to take the last person off 
    # run until guest list is <= capacity