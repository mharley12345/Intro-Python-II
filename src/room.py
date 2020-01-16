class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
# Each room has N W S E doors and they are initialized as None until object is instantiated
        self.n_to = None
        self.w_to = None
        self.s_to = None
        self.e_to = None
        self.items = []

    def __str__(self):
        return f"{self.name}"

    def getDesc(self):
        return f"{self.description}"

    def getRoomItems(self):
        return self.items

    def addItem(self, item):
        # player picks item adds to their inventory and Item method is fired
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)