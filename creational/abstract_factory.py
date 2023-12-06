from abc import ABC, abstractmethod



class AbstractDoor(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


class RegularDoor(AbstractDoor):
    def __init__(self):
        self.is_open = False

    def open(self):
        print("Player open the door")
        self.is_open = True

    def close(self):
        print("Player close the door")
        self.is_open = False


class SpikyDoor(AbstractDoor):
    def __init__(self):
        self.is_open = False

    def open(self):
        print("Player open the door")
        self.attack()
        self.is_open = True

    def close(self):
        print("Player close the door")
        self.attack()
        self.is_open = False

    def attack(self):
        print("Door's spike hurt player with 10 damage")



class DungeonFactory(ABC):
    @abstractmethod
    def createRoom(self):
        pass

    @abstractmethod
    def createWall(self):
        pass

    @abstractmethod
    def createDoor(self) -> AbstractDoor:
        pass


class BeginnerDungeonFactory(DungeonFactory):
    def createRoom(self):
        print("Create beginner dungeon room")

    def createWall(self):
        print("Create beginner dungeon wall")

    def createDoor(self) -> AbstractDoor:
        print("Create beginner dungeon door")
        return RegularDoor()


class AdvancedDungeonFactory(DungeonFactory):
    def createRoom(self):
        print("Create advanced dungeon room")

    def createWall(self):
        print("Create advanced dungeon wall")

    def createDoor(self) -> AbstractDoor:
        print("Create advanced dungeon door")
        return SpikyDoor()



def create_dungeon(factory: DungeonFactory):
    room = factory.createRoom()
    wall_1 = factory.createWall()
    wall_2 = factory.createWall()
    wall_3 = factory.createWall()
    wall_4 = factory.createWall()
    door = factory.createDoor()

    door.open()
    door.close()


def main():
    dungeon_factory = AdvancedDungeonFactory()
    create_dungeon(dungeon_factory)



if __name__ == "__main__":
    main()