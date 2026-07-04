# MECHANICAL STUFF

init:
    transform faceright: 
        xzoom -1.0
    transform faceleft:
        xzoom 1.0

init python:

# VARS

    time = 0
    inventory = []
    last_label = "test"
    possible_actions = {
    "north":"n", "n":"n", "south":"s", "s":"s", "west":"w", "w":"w", "east":"e", "e":"e",
    "progress":"progress",
    "enter":"enter", "go":"enter",
    "look":"look",
    "use":"use",
    "take":"take",
    "inventory":"inv", "inv":"inv",
    "cmd":"cmd", "help":"cmd", "h":"cmd"
    }

# INPUT FUNCTIONS

    def inp(s):
        act = renpy.input(prompt=s)
        act = act.lower()
        return parse_input(act)

    def parse_input(act):
        lst = []
        index = 0;
        while (act != "" and index<len(act)):
            if (act[index]==" "):
                lst.append(act[:index])
                act = act[index+1:]
                index = 0
            index += 1
        lst.append(act)
        return find_label(check_input(lst))
    
    def check_input(lst):
        if len(lst) < 2:
            if lst[0] == "":
                return ["progress"]
            else:
                for p in possible_actions:
                    if lst[0] == p:
                        return [possible_actions[lst[0]]]
                else:
                    if lst[0] in inventory or area.has_exit(lst[0]) or area.has_object(lst[0]) or area.has_interact(lst[0]):
                        return [lst[0]]
                    else:
                        return ["fail"]
        else:
            return check_input([lst[0]]) + check_input(lst[1:])
    
    def find_label(command):
        if debug:
            renpy.say(narrator, str(command))
        if "enter" in command:
            for i in command:
                if area.has_exit(i):
                    return i
                else:
                    return "enter_fail"
        if "use" in command:
            for i in command:
                if area.has_object(i):
                    return "use_" + i
                elif area.has_interact(i):
                    for x in command:
                        if area.get_interact(i).has_key(x):
                            return "use_" + x + "_on_" + i
                    return "interact_fail"
            return "use_fail"
        if "take" in command:
            for i in command:
                if area.has_object(i):
                    return "take" + "_" + i
        if "progress" in command:
            return "progress_" + str(time)
        if "look" in command:
            for i in command:
                if area.has_object(i):
                    return "look_at_" + i
            return "look_" + area
        if "inv" in command:
            return "inv"
        if "cmd" in command:
            return "cmd"
        return "fail"
    
# CLASSES
# Interactable

    class Interactable:
        name = ""
        keys = []
        
        def __init__(self, name):
            self.name = name
        
        def add_key(self, key):
            self.keys.append(key)

# Area

    class Area:
        name = ""
        exits = []
        objects = []
        interactables = {}
        
        def __init__(self, name):
            self.name = name
            self.exits = []
            self.objects = []
            self.interactables = {}
        
        def add_exit(self, a2):
            self.exits.append(a2)
        
        def has_exit(self, e):
            for x in self.exits:
                if e == x.name:
                    return True
            return False
        
        def has_object(self, e):
            for x in self.objects:
                if e == x.name:
                    return True
            return False
        
        def has_interact(self, e):
            for x in self.interactables:
                if e == x.name:
                    return True
            return False
        
        def get_interact(self, e):
            if self.has_interact(e):
                return interactables[e]
        
        def add_exit(self, a2):
            self.exits.append(a2)
        
        def add_interactable(self, name):
            self.interactables.add(name, Interactable(name))
    
    def create_path(a1, a2):
        a1.add_exit(a2)
        a2.add_exit(a1)

# GAME SETUP
    areas = {"backyard":Area("backyard"),
    "shop_1":Area("shop"),
    "kitchen":Area("kitchen"),
    "upstairs":Area("upstairs"),
    "bathroom":Area("bathroom"),
    "bedroom":Area("bedroom"),
    "path_1":Area("path"),
    "path_2":Area("path"),
    "food_stall":Area("food stall"),
    "shop_2":Area("shop"),
    "storage":Area("storage"),
    "secret_path_0":Area("path"),
    "cave_1":Area("cave"),
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
    
    area = areas["backyard"]

# TESTER FUNCTIONS
    def test_paths(area):
        st = areas[area].name + ": "
        for x in areas[area].exits:
            st += x.name
            st += " "
        return st
    
    debug = True

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

label test:

    $ renpy.jump(inp("test"))

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
