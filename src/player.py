# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def moving(self, direction_command, current_room):
        attributes = f"{direction_command} + '_to'"
        if getattr(self.current_room, attributes):
            self.current_room = getattr(self.current_room, attributes)
            print(self.current_room)
        else: 
            print("Error! You can't move that direction.")




        