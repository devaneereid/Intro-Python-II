# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, current_description, item=[]):
        self.name = name
        self.current_description = current_description
        self.item = item

    def __str__(self):
        return self.name 
    
    def about(self, item):
        print(f"the player can pick up the {self.item}.")

# class Item:
#     def __init__(self, item):
#         self.item = item
        # self.desc = desc


