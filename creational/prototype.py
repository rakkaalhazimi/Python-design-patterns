from uuid import uuid4

class BasicDoor:
    def __init__(self):
        self.id = uuid4().hex

    def clone(self):
        return self

class BasicWall:
    def __init__(self):
        self.id = uuid4().hex

    def clone(self):
        return self

class BasicRoom:
    def __init__(self):
        self.id = uuid4().hex

    def clone(self):
        return self



class BasicDungeonPrototypeFactory:
    def __init__(self, door, wall, room):
        self.prototype_door = door
        self.prototype_wall = wall
        self.prototype_room = room

    def create_door(self):
        return self.prototype_door.clone()

    def create_wall(self):
        return self.prototype_wall.clone()

    def create_room(self):
        return self.prototype_room.clone()



def main():

    door = BasicDoor()
    wall = BasicWall()
    room = BasicRoom()

    dungeon = BasicDungeonPrototypeFactory(
        door, wall, room
    )

    dungeon_door = dungeon.create_door()

    print("Base doro id: ", id(door))
    print("Dungeon door id: ", id(dungeon_door))


if __name__ == "__main__":
    main()