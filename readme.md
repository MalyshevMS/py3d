This module allows you to create and operate with 3d objects in 3d space

Main API
========
## Volume ##
Base class for creating 3d space using provided border limits.
***This class includes these methods:***

### `get_border():`
return list with border values, if border is **NULL** border - raises **Volume.BorderError**
(0 - X border;
1 - Y border;
2 - Z border)

### `get_name(name: str):`
trying to return object index in **self.obj** using name, else raises **Volune.NoObjectError**

### `create_box(name: str, x: int, y: int, z: int, size_x: int, size_y: int, size_z: int):`
trying to create box in space **self** with positional **name** and returns object, else raises **Volume.BorderError**

### `border_edit(axis: str = ALL_AXIS, value: int = 0):`
set **self.border['axis']** to value,
where axis can be **'x'**, **'y'**, **'z'** or **'ax+'** (or you can use *constants*)

### `get_default():`
returns default **Volume**



## Box ##
Base class for creating box in provided 3d space.
***This class includes these methods:***

### `get_size():`
return dict with **Cube** size

### `get_coords():`
return dict with **Cube** coordinates

### `move(axis: str, value: int, method: str = ADD):`
moves cube along provided axis using provided method,
where axis can be **'x'**, **'y'** or **'z'**;
method: **'MULTIPLY'**, **'ADD'** or **'SET'**
(or you can use *constants*)

### `scale(axis: str, value: int, method: str = MULTIPLY):`
scales cube along provided axis using provided method,
where axis can be **'x'**, **'y'** or **'z'**;
method: **'MULTIPLY'**, **'ADD'** or **'SET'**
(or you can use *constants*)

### `display(plane: str = XY, box_fill: str = "#", empty_fill: str = ".", dist: str = " ", file = None):`
display current cube on provided plane (can write to provided file), 
where plane can be **'xy'**, **'xz'** or **'zy'**
(or you can use *constants*)



## Exeptions ##

### `BorderError(Exception):`
Object larger than border or function trying to get **NULL** border
        
### `NoObjectError(Exception):`
3d object not found or does not exist



Other API
=========
## IUI ##
Additional class with User Interface.
***This class includes these functions:***
### `clear():`
clearing console or provided file

### `manual():`
mode, where user can create his own Volume and Box

### `anim():`
mode, displaying simple animation

### `ui():`
function, where user can choose mode