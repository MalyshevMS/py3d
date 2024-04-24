r"""
This module allows you to create and operate with 3d objects in 3d space

Main API
========
## Volume ##
Base class for creating 3d space using provided border limits.
This class includes these methods:

### `get_border():`
return list with border values, if border is NULL border - raises Volume.BorderError
(0 - X border;
1 - Y border;
2 - Z border)

### `get_name(name: str):`
trying to return object index in self.obj using name, else raises Volune.NoObjectError

### `create_box(name: str, x: int, y: int, z: int, size_x: int, size_y: int, size_z: int):`
trying to create box in space self with positional name and returns object, else raises Volume.BorderError

### `border_edit(axis: str = ALL_AXIS, value: int = 0):`
set self.border['axis'] to value,
where axis can be 'x', 'y', 'z' or 'ax+' (or you can use constants)

### `get_default():`
returns default Volume



## Box ##
Base class for creating box in provided 3d space.
*This class includes these methods:*

### `get_size():`
return dict with Cube size

### `get_coords():`
return dict with Cube coordinates

### `move(axis: str, value: int, method: str = ADD):`
moves cube along provided axis using provided method,
where axis can be 'x', 'y' or 'z';
method: 'MULTIPLY', 'ADD' or 'SET'
(or you can use *constants*)

### `scale(axis: str, value: int, method: str = MULTIPLY):`
scales cube along provided axis using provided method,
where axis can be 'x', 'y' or 'z';
method: 'MULTIPLY', 'ADD' or 'SET'
(or you can use *constants*)

### `display(plane: str = XY, box_fill: str = "#", empty_fill: str = ".", dist: str = " ", file = None):`
display current cube on provided plane (can write to provided file), 
where plane can be 'xy', 'xz' or 'zy'
(or you can use constants)



## Exeptions ##

### `BorderError(Exception):`
Object larger than border or function trying to get NULL border
        
### `NoObjectError(Exception):`
3d object not found or does not exist



Other API
=========
## IUI ##
Additional class with User Interface.
This class includes these functions:
### `clear():`
clearing console or provided file

### `manual():`
mode, where user can create his own Volume and Box

### `anim():`
mode, displaying simple animation

### `ui():`
function, where user can choose mode
"""

from time import sleep as wait
from subprocess import call as run
from typing import Literal

try:
    from constants import *
except:
    X: str = 'x'
    Y: str = 'y'
    Z: str = 'z'
    ALL_AXIS: str = "ax+"
    MULTIPLY: str = 'MULTIPLY'
    ADD: str = 'ADD'
    SET: str = 'SET'
    X_BORDER: int = 0
    Y_BORDER: int = 1
    Z_BORDER: int = 2
    XY: str = "xy"
    XZ: str = "xz"
    ZY: str = "zy"



class Volume():
    """
    class for creating Volume (3d space) 
    """
    # exeptions:
    class BorderError(Exception):
        """
        Object larger than border or function trying to get NULL border
        """
        pass
    class NoObjectError(Exception): 
        """
        3d object not found or does not exist
        """
        pass

    # methods:
    def get_default() -> object:
        """
        returns default Volume
        """ 
        return Volume()
    
    def __init__(self, border_x: int = 0, border_y: int = 0, border_z: int = 0) -> None:
        self.border: int = [border_x, border_y, border_z]
        self.obj: list = []
        self.names: list = []

    def get_border(self) -> list:
        """
        return list with border values, if border is NULL border - raises Volume.BorderError. \n
        (0 - X border;
        1 - Y border;
        2 - Z border)
        """
        if self.border[X_BORDER] and self.border[Y_BORDER] and self.border[Z_BORDER]: 
            return self.border
        else: raise self.BorderError("cannot get NULL border")
        
    def get_name(self, name: str) -> object:
        """
        trying to return object index in self.obj using name, else raises Volune.NoObjectError
        """
        try:
            return self.names[self.names.index(name) + 1]
        except: raise self.NoObjectError("there is no object, associated with this name")
        
    def create_box(self, name: str, x: int, y: int, z: int, size_x: int, size_y: int, size_z: int) -> object:
        """
        trying to create box in space self with positional name and returns object, else raises Volume.BorderError
        """
        if size_x + x <= self.border[X_BORDER] and size_y + y <= self.border[Y_BORDER] and size_z + z <= self.border[Z_BORDER] and (x >= 0 and y >= 0 and z >= 0):
            box = Box(self, x, y, z, size_x, size_y, size_z, name, False)
            self.obj.append(box)
            self.names.append(name)
            self.names.append(len(self.obj) - 1)

            return box
        else: raise self.BorderError(f"cannot create box '{name}': box out of border")

    def border_edit(self, axis: Literal['x', 'y', 'z', 'ax+'] = ALL_AXIS, value: int = 0):
        """
        set self.border['axis'] to value,\n
        where axis can be 'x', 'y', 'z' or 'ax+' (or you can use constants)
        """
        match axis:
            case "x":
                self.border[X_BORDER] = value
            case "y":
                self.border[Y_BORDER] = value
            case "z":
                self.border[Z_BORDER] = value
            case "ax+":
                self.border[X_BORDER] = value
                self.border[Y_BORDER] = value
                self.border[Z_BORDER] = value
        


class Box():
    """
    class for creating box in 3d space (Volume)
    """
    def __init__(self, space: Volume, x: int = 0 , y: int = 0, z: int = 0, size_x: int = 1, size_y: int = 1, size_z: int = 1, name: str = "", doNaming: Literal[True, False] = False) -> None:
        if (size_x + x <= space.border[X_BORDER] and size_y + y <= space.border[Y_BORDER] and size_z + z <= space.border[Z_BORDER]) and (x >= 0 and y >= 0 and z >= 0):
            self.x: int = x
            self.y: int = y
            self.z: int = z
            self.size_x: int = size_x
            self.size_y: int = size_y
            self.size_z: int = size_z
            self.space: Volume = space

            if doNaming:
                if not name:
                    space.obj.append(self)
                    space.names.append(f"box__x:{x}_y:{y}_z:{z}__size:{size_x}_{size_y}_{size_z}")
                    space.names.append(len(space.obj) - 1)
                    self.name = f"box__x:{x}_y:{y}_z:{z}__size:{size_x}_{size_y}_{size_z}"
                
                else:
                    space.obj.append(self)
                    space.names.append(name)
                    space.names.append(len(space.obj) - 1)
                    self.name = name

            else: self.name = f"box__x:{x}_y:{y}_z:{z}__size:{size_x}_{size_y}_{size_z}"

        else:
            try:
                raise Volume.BorderError(f"cannot create box '{self.name}': box out of border")
            except AttributeError:
                raise Volume.BorderError(f"cannot create box '{name}': box out of border")
        
    def get_size(self) -> dict[str, int]:
        """
        return dict with Cube size
        """
        return {"size_x": self.size_x, 
                "size_y": self.size_y, 
                "size_z": self.size_z}
    
    def get_coords(self) -> dict[str, int]:
        """
        return dict with Cube coordinates
        """
        return {"x": self.x, 
                "y": self.y, 
                "z": self.z}
    
    def move(self, axis: Literal["x", "y", "z"], value: int, method: Literal["ADD", "SET", "MULTIPLY"] = ADD) -> None:
        """
        moves cube along provided axis using provided method,\n
        where axis can be 'x', 'y' or 'z';
        method: 'MULTIPLY', 'ADD', 'SET'
        (or you can use constants)
        """
        match method:
            case "MULTIPLY":
                match axis:
                    case 'x':
                        if self.size_x + self.x * value <= self.space.border[X_BORDER] and self.x * value >= 0:
                            self.x *= value
                        else: raise Volume.BorderError(f"cannot move box '{self.name}': move value out of the border")
        
                    case 'y':
                        if self.size_y + self.y * value <= self.space.border[Y_BORDER] and self.y * value >= 0:
                            self.y *= value
                        else: raise Volume.BorderError(f"cannot move box '{self.name}': move value out of the border")

                    case 'z':
                        if self.size_z + self.z * value <= self.space.border[Z_BORDER] and self.z * value >= 0:
                            self.z *= value
                        else: raise Volume.BorderError(f"cannot move box '{self.name}': move value out of the border")

            case "ADD":
                match axis:
                    case 'x':
                        if self.size_x + self.x + value <= self.space.border[X_BORDER] and self.x + value >= 0:
                            self.x += value
                        else: raise Volume.BorderError(f"cannot move box '{self.name}': move value out of the border")
        
                    case 'y':
                        if self.size_y + self.y + value <= self.space.border[Y_BORDER] and self.y + value >= 0:
                            self.y += value
                        else: raise Volume.BorderError(f"cannot move box '{self.name}': move value out of the border")

                    case 'z':
                        if self.size_z + self.z + value <= self.space.border[Z_BORDER] and self.z + value >= 0:
                            self.z += value
                        else: raise Volume.BorderError(f"cannot move box '{self.name}': move value out of the border")

            case "SET":
                match axis:
                    case 'x':
                        if self.size_x + value <= self.space.border[X_BORDER] and value >= 0:
                            self.x = value
                        else: raise Volume.BorderError(f"cannot move box '{self.name}': move value out of the border")
        
                    case 'y':
                        if self.size_y + value <= self.space.border[X_BORDER] and value >= 0:
                            self.y = value
                        else: raise Volume.BorderError(f"cannot move box '{self.name}': move value out of the border")

                    case 'z':
                        if self.size_z + value <= self.space.border[X_BORDER] and value >= 0:
                            self.z = value
                        else: raise Volume.BorderError(f"cannot move box '{self.name}': move value out of the border")

    def scale(self,  axis: Literal["x", "y", "z"], value: int, method: Literal["ADD", "SET", "MULTIPLY"] = MULTIPLY) -> None:
        """
        scales cube along provided axis using provided method,\n
        where axis can be 'x', 'y' or 'z';
        method: 'MULTIPLY', 'ADD', 'SET'
        (or you can use constants)
        """
        match method:
            case "MULTIPLY":
                if value:
                    match axis:
                        case 'x':
                            if 0 <= self.size_x * value <= self.space.border[X_BORDER]:
                                self.size_x *= value
                            else: raise Volume.BorderError(f"cannot scale box '{self.name}': scale value out of the border")

                        case 'y':
                            if 0 <= self.size_y * value <= self.space.border[Y_BORDER]:
                                self.size_y *= value
                            else: raise Volume.BorderError(f"cannot move box '{self.name}': scale value out of the border")

                        case 'z':
                            if 0 <= self.size_z * value <= self.space.border[Z_BORDER] and self.z * value >= 0:
                                self.size_z *= value
                            else: raise Volume.BorderError(f"cannot move box '{self.name}': scale value out of the border")
                else: raise Volume.BorderError(f"cannot move box '{self.name}': scale 'MULTIPLY' value cannot be 0")

            case "ADD":
                match axis:
                    case 'x':
                        if self.size_x + value + self.x <= self.space.border[X_BORDER] and (self.x + value >= 0):
                            self.size_x += value
                        else: raise Volume.BorderError(f"cannot scale box '{self.name}': scale value out of the border")
                        
        
                    case 'y':
                        if self.size_y + value + self.y <= self.space.border[Y_BORDER] and (self.x + value >= 0):
                            self.size_y += value
                        else: raise Volume.BorderError(f"cannot scale box '{self.name}': scale value out of the border")

                    case 'z':
                        if self.size_z + value + self.z <= self.space.border[Z_BORDER] and (self.x + value >= 0):
                            self.size_z += value
                        else: raise Volume.BorderError(f"cannot scale box '{self.name}': scale value out of the border")

            case "SET":
                if value:
                    match axis:
                        case 'x':
                            if 0 <= value <= self.space.border[X_BORDER]:
                                self.size_x = value
                            else: raise Volume.BorderError(f"cannot scale box '{self.name}': scale value out of the border")

                        case 'y':
                            if 0 <= value <= self.space.border[Y_BORDER]:
                                self.size_y = value
                            else: raise Volume.BorderError(f"cannot scale box '{self.name}': scale value out of the border")

                        case 'z':
                            if 0 <= value <= self.space.border[Z_BORDER]:
                                self.size_z = value
                            else: raise Volume.BorderError(f"cannot scale box '{self.name}': scale value out of the border")
                else: raise Volume.BorderError(f"cannot scale box '{self.name}': scale 'SET' value cannot be 0")

    def display(self, plane: Literal["xy", "xz", "zy"] = XY, box_fill: str = "#", empty_fill: str = ".", dist: str = " ", file = None) -> None:
        """
        display current cube on provided plane (can write to provided file),\n
        where plane can be 'xy', 'xz' or 'zy'
        """
        match plane:
            case "xy":
                for i in range(self.space.border[Y_BORDER]):
                    for j in range(self.space.border[X_BORDER]):
                        if i in range(self.y, self.size_y + self.y) and j in range(self.x, self.size_x + self.x):
                            print(box_fill, end=dist, file=file)
                        else:
                            print(empty_fill, end=dist, file=file)
                    print(file=file)
            
            case "xz":
                for i in range(self.space.border[Z_BORDER]):
                    for j in range(self.space.border[X_BORDER]):
                        if i in range(self.z, self.size_z + self.z) and j in range(self.x, self.size_x + self.x):
                            print(box_fill, end=dist, file=file)
                        else:
                            print(empty_fill, end=dist, file=file)
                    print(file=file)

            case "zy":
                for i in range(self.space.border[Y_BORDER]):
                    for j in range(self.space.border[Z_BORDER]):
                        if i in range(self.y, self.size_y + self.y) and j in range(self.z, self.size_z + self.z):
                            print("# ", end="", file=file)
                        else:
                            print(". ", end="", file=file)
                    print(file=file)



class IUI():
    """
    Integrated User Interface
    -------------------------
    class with simple UI functions

    """

    def clear(self, file = None): 
        """
        clearing console or provided file
        """
        if file:
            with open(file, "w+") as f:
                f.truncate(0)
        else:
            try:
                run("powershell clear", shell=True)
            except:
                run("clear", shell=True)

    def anim(self):
        """
        mode, displaying simple animation
        """
        vol = Volume(10, 10, 10)
        box = Box(vol, 0, 0, 0, 2, 2, 2, "box", True)

        loops = int(input("How much animation loops do you want:"))

        for g in range(loops):
            for j in range(3):
                for i in range(8):
                    box.display(XY)
                    box.move(X, 1)
                    box.move(Y, 1)
                    self.clear()

                for i in range(8):
                    box.display(XY)
                    box.move(X, -1)
                    box.move(Y, -1)
                    self.clear()

            for j in range(3):
                box.move(X, 0, SET)
                box.move(Y, 0, SET)
                box.move(Z, 0, SET)

                for k in range(8):
                    box.display(XY)
                    box.scale(X, 1, ADD)
                    self.clear()
                
                for k in range(8):
                    box.display(XY)
                    box.scale(Y, 1, ADD)
                    self.clear()

                for k in range(8):
                    box.display(XY)
                    box.scale(X, -1, ADD)
                    self.clear()
                
                for k in range(8):
                    box.display(XY)
                    box.scale(Y, -1, ADD)
                    self.clear()

    def manual_mode(self):
        """
        mode, where user can create his own Volume and Box
        """
        self.clear()
        print("First we need to create a volume")
        hx = int(input("lenght of your volume:"))
        hy = int(input("width of your volume:"))
        hz = int(input("height of your volume:"))

        vol = Volume(hx, hy, hz)

        wait(1)
        self.clear()
        print("creating volume.")
        wait(0.5)
        self.clear()
        print("creating volume..")
        wait(0.5)
        self.clear()
        print("creating volume...")
        wait(0.5)
        self.clear()
        print("Volume successfuly created\nNow let's create your first box")

        bx_size = int(input("lenght of your box:"))
        by_size = int(input("width of your box:"))
        bz_size = int(input("height of your box:"))

        bx = int(input("X coordinate of your box:"))
        by = int(input("Y coordinate of your box:"))
        bz = int(input("Z coordinate of your box:"))

        box = Box(vol, bx, by, bz, bx_size, by_size, bz_size, "user_box", True)

        wait(1)
        self.clear()
        print("creating box.")
        wait(0.5)
        self.clear()
        print("creating box..")
        wait(0.5)
        self.clear()
        print("creating box...")
        wait(0.5)
        self.clear()
        print("Box successfully created with name 'user_box'")

        print("Available commands now:")
        print("display [plane]: displaying current scene, where plane is 'xy', 'xz' or 'zy'",
            "move [axis] [value] [mode]: moving 'user_box', where axis is 'xyz', mode is 'multiply', 'add' or 'set', value must be integer",
            "scale [axis] [value] [mode]: scales 'user_box', where axis is 'xyz', mode is 'multiply', 'add' or 'set', value must be integer",
            "get_coords: return 'user_box' coordinates",
            "get_size: return 'user_box' size", "", sep="\n")
        
        while True:
            com = input("py3d_v0.0.1\n└─$ ")

            if com[:7] == "display":
                box.display(com[8:].lower())
            elif com[:4] == "move":
                box.move(com[5].lower(), int(com[7]), com[9:].upper())
            elif com[:5] == "scale":
                box.scale(com[6].lower(), int(com[8]), com[10:].upper())
            elif com == "get_coords":
                print(box.get_coords())
            elif com == "get_size":
                print(box.get_size())

    def ui(self, doClear: bool = True):
        """
        function, where user can choose mode
        """
        if doClear: self.clear()

        print("Welcome to Python3D!")

        mode = input("select mode (animation / manual):")

        match mode.lower():
            case "animation":
                self.anim()

            case "manual":
                self.manual_mode()

            case _:
                print("incorrect mode")
