# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, current_description):
        self.name = name
        self.current_description = current_description

    def __str__(self):
        # print(self.name)
        return self.name




