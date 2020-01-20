class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"{self.name}"

    def addItem(self, item):
        # player picks item adds to their inventory and Item method is fired
        self.inventory.append(item)
        item.on_take()

    def removeItem(self, item):
        self.inventory.remove(item)
        item.on_drop()