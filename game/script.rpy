# MECHANICAL STUFF

init:
    transform faceright: 
        xzoom -1.0
    transform faceleft:
        xzoom 1.0

init python:
    
    area = ""
    time = 0
    
    def input(s):
        act = renpy.input(prompt=s)
        act = act.lower()
        
    class Area:
        name = ""
        exits = []
        objects = []
        interactables = []
        
        def __init__(self, name):
            self.name = name
            self.exits = []
            self.objects = []
            self.interactables = []
        
        def add_exit(self, a2):
            self.exits.append(a2)
    
    def create_path(a1, a2):
        a1.add_exit(a2)
        a2.add_exit(a1)

    areas = {"backyard":Area("backyard"),
    "shop_1":Area("shop_1"),
    "kitchen":Area("kitchen"),
    "upstairs":Area("upstairs"),
    "bathroom":Area("bathroom"),
    "bedroom":Area("bedroom"),
    "path_1":Area("path_1"),
    "path_2":Area("path_2"),
    "food_stall":Area("food_stall"),
    "shop_2":Area("shop_2"),
    "storage":Area("storage"),
    "secret_path_0":Area("secret_path_0"),
    "cave_1":Area("cave_1"),
    "waterfall":Area("waterfall")
    }
    
    create_path(areas["backyard"], areas["shop_1"])
    create_path(areas["kitchen"], areas["shop_1"])
    create_path(areas["path_1"], areas["shop_1"])
    create_path(areas["kitchen"], areas["upstairs"])
    create_path(areas["bedroom"], areas["upstairs"])
    create_path(areas["bathroom"], areas["upstairs"])
    create_path(areas["path_1"], areas["path_2"])
    create_path(areas["path_1"], areas["secret_path_0"])
    create_path(areas["food_stall"], areas["path_2"])
    create_path(areas["shop_2"], areas["path_2"])
    create_path(areas["shop_2"], areas["storage"])
    create_path(areas["waterfall"], areas["secret_path_0"])
    create_path(areas["cave_1"], areas["secret_path_0"])
    
    def test_paths(area):
        st = areas[area].name + ": "
        for x in areas[area].exits:
            st += x.name
            st += " "
        return st

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    
    $renpy.say(e, test_paths("backyard"))
    $renpy.say(e, test_paths("shop_1"))

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
