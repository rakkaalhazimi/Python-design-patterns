"""
Adapter pattern is a structural design pattern that allows objects with incompatible
interfaces to collaborates.

In the code below, we will use the electrical plug example.
"""


from abc import ABC, abstractmethod


# 1. Create socket abstract base clase
class Socket(ABC):
    @abstractmethod
    def plugged_by(self):
        ...

# 2. Create plugger abstract base clase
class Plugger(ABC):
    @abstractmethod
    def plugs(self):
        ...

# 3. Create rectangle socket class
#    it has a .require attribute and .plugger_by() method
#    .require is the plugger shape for this socket
#    .plugged_by() is when the plugger try to be inserted
class RectangleSocket(Socket):
    require = "rectangle"
    def plugged_by(self, plugger: Plugger):
        return True if self.require == plugger.shape else False


# 4. This is the adapter function to adapt any plugger shape into a specific socket
#    the function take socket object as argument and return a plugger with matching shape
def adapt(socket: Socket) -> Plugger:
    plug_map = {
        "rectangle": RectanglePlugger,
        "circle": CirclePlugger
    }
    return plug_map.get(socket.require)


# 5. The other two class below is a Plugger class
#    this class have .shape attribute and .plugs() method
#    .shape is the type of the plugger
#    .plugs() is when this plugger try to be inserted into a socket
class RectanglePlugger(Plugger):
    shape = "rectangle"
    def plugs(self, socket: Socket) -> bool:
        adapted_plugger: Plugger = adapt(socket, self)
        return socket.plugged_by(adapted_plugger)

class CirclePlugger(Plugger):
    shape = "circle"
    def plugs(self, socket: Socket) -> bool:
        adapted_plugger: Plugger = adapt(socket)
        return socket.plugged_by(adapted_plugger)





if __name__ == "__main__":
    rect_socket = RectangleSocket()
    circle_plug = CirclePlugger()

    print(circle_plug.plugs(rect_socket))
    