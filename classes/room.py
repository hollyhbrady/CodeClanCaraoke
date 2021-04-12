class Room:

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.attendees = []
        self.song_list = []

    def check_in(self, guest): # tried to add a specific room to add to. Can't make it work.
        # tried to add check capacity up here before check in but - TypeError: check_in() missing 1 required positional argument: 'guest' I don't know how to solve this
        if len(self.attendees) < self.capacity:
            self.attendees.append(guest)

    # def check_out(self, guest, attendees):
    #     for person in self.attendees:
    #         if person.name == guest.name:
    #             self.attendees.remove(person)
        # Tried to make an if loop to find guest then remove them, cant make it work
                
    def check_out(self, guest):
        # self.attendees.append(guest) # cant run without this or ValueError: list.remove(x)
        self.attendees.remove(guest)

    def add_song(self, song):
        self.song_list.append(song) # which room? cant make it work when I try to add this
    
    def check_capacity(self):
        if len(self.attendees) > self.capacity:
            self.attendees.pop() #will this keep running until line 26 isn't more than?
        return self.capacity
    # TypeError: '>' not supported between instances of 'int' and 'TestRoom'        

    #check the len of guest list
    #if > capacity 
    #pop() to take the last person off 
    # run until guest list is <= capacity