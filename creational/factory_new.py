from abc import ABC, abstractmethod

class MazeGame(ABC):
    @abstractmethod
    def create_room(self):
        pass

    @abstractmethod
    def create_door(self):
        pass

    @abstractmethod
    def create_wall(self):
        pass


class BeginnerMazeGame(MazeGame):
    def create_room(self):
        print("Create beginner maze room")

    def create_door(Self):
        print("Create beginner maze door")

    def create_wall(self):
        print("Create beginner maze wall")


class AdvancedMazeGame(MazeGame):
    def create_room(self):
        print("Create advanced maze room")

    def create_door(self):
        print("Create advanced maze door")

    def create_wall(self):
        print("Create advanced maze wall")



def main():
    maze_game = AdvancedMazeGame()
    room = maze_game.create_room()
    wall = maze_game.create_wall()
    door = maze_game.create_door()



if __name__ == "__main__":
    main()
