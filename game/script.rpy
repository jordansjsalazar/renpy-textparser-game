# MECHANICAL STUFF

init:
    transform faceright: 
        xzoom -1.0
    transform faceleft:
        xzoom 1.0

init python:

# VOICE

    renpy.music.register_channel("beep", mixer="voice")
    
    def voice(event, interact=True, file="audio/bleep001.ogg", **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play(file, loop=True, channel="beep")
        elif event == "slow_done":
            renpy.sound.stop(fadeout=1, channel="beep")

# VARS

    time = 0
    inventory = []
    last_label = "guest_cabin"
    possible_actions = {
    "north":"n", "n":"n", "south":"s", "s":"s", "west":"w", "w":"w", "east":"e", "e":"e",
    "progress":"progress",
    "enter":"enter", "go":"enter",
    "look":"look",
    "use":"use",
    "take":"take",
    "inventory":"inv", "inv":"inv",
    "cmd":"cmd", "help":"cmd", "h":"cmd",
    "talk":"talk", "ask":"talk"
    }
    
    def use_item(name):
        if name in inventory:
            inventory.remove(name)

# INPUT FUNCTIONS

    def inp(s):
        act = renpy.input(prompt=s)
        act = act.lower()
        return parse_input(act)

    def parse_input(act):
        if debug:
            if act == "end1":
                store.time = 99
                time_check()
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
                    if lst[0] in inventory or areas[area].has_exit(lst[0]) or areas[area].has_object(lst[0]) or areas[area].has_interact(lst[0]):
                        return [lst[0]]
                    for npc in npcs:
                        if areas[npc.current_location] == areas[area]:
                            if npc.name == lst[0]:
                                print("asdf")
                                return [lst[0]]
                    return ["fail"]
        else:
            return check_input([lst[0]]) + check_input(lst[1:])
    
    def find_label(command):
        #if debug:
            #renpy.say(narrator, str(command))
            #renpy.say(narrator, areas[area].name)
        if "n" in command:
            if areas[area].has_north():
                time_check()
                return areas[area].north.get_label_name()
        if "e" in command:
            if areas[area].has_east():
                time_check()
                return areas[area].east.get_label_name()
        if "w" in command:
            if areas[area].has_west():
                time_check()
                return areas[area].west.get_label_name()
        if "s" in command:
            if areas[area].has_south():
                time_check()
                return areas[area].south.get_label_name()
        if "enter" in command:
            for i in command:
                if areas[area].has_exit(i):
                    time_check()
                    return areas[area].has_exit(i).get_label_name()
            else:
                return "enter_fail"
        if "use" in command:
            for i in command:
                if areas[area].has_object(i):
                    time_check()
                    return "use_" + i
                elif areas[area].has_interact(i):
                    for x in command:
                        if areas[area].get_interact(i).has_key(x):
                            time_check()
                            return "use_" + x + "_on_" + i
                    return "interact_" + areas[area].get_interact(i).name
            return "use_fail"
        if "take" in command:
            for i in command:
                if areas[area].has_object(i):
                    time_check()
                    return "take" + "_" + i
            return "take_fail"
        if "talk" in command:
            for i in command:
                for npc in npcs:
                    if areas[npc.current_location] == areas[area]:
                        if i == npc.name:
                            for o in command:
                                if npc.has_topic(o):
                                    time_check()
                                    return "talk_" + i + "_about_" + o
                            time_check()
                            return "talk_" + i
            return "talk_fail"
        if "progress" in command:
            #return "progress_" + str(time)
            return "progress"
        if "look" in command:
            for i in command:
                if areas[area].has_object(i) or areas[area].has_interact(i):
                    time_check()
                    return "look_at_" + i
                for npc in npcs:
                    if areas[npc.current_location] == areas[area]:
                        if i == npc.name:
                            time_check()
                            return "look_at_" + i
            return "look_" + area
        if "inv" in command:
            return "inv"
        if "cmd" in command:
            return "cmd"
        return "fail"
    
    def time_check():
        store.time += 1
        if store.time == 100:
            renpy.jump("ending_1")
        for npc in npcs:
            npc.current_location = npc.locations[store.time]
        #if debug:
            #renpy.say(narrator, str(time))
    
# CLASSES
# Interactable

    class Interactable:
        name = ""
        keys = []
        
        def __init__(self, name):
            self.name = name
        
        def add_key(self, key):
            self.keys.append(key)
        
        def has_key(self, key):
            for x in self.keys:
                if key == x:
                    return x
            return False

# Area

    class Area:
        name = ""
        label_name = ""
        exits = []
        objects = []
        interactables = {}
        
        north = False
        east = False
        west = False
        south = False
        
        def __init__(self, name, label_name):
            self.name = name
            self.label_name = label_name
            self.exits = []
            self.objects = []
            self.interactables = {}
        
        def add_exit(self, a2):
            self.exits.append(a2)
        
        def add_north(self, x):
            self.north = x
            x.south = self
        
        def add_east(self, x):
            self.east = x
            x.west = self
        
        def add_west(self, x):
            self.west = x
            x.east = self
        
        def add_south(self, x):
            self.south = x
            x.north = self
        
        def has_north(self):
            return self.north
        
        def has_east(self):
            return self.east
        
        def has_west(self):
            return self.west
        
        def has_south(self):
            return self.south
        
        def has_exit(self, e):
            for x in self.exits:
                if e == x.name:
                    return x
            return False
        
        def has_object(self, e):
            for x in self.objects:
                if e == x:
                    return x
            return False
        
        def has_interact(self, e):
            for x in self.interactables:
                if e == x:
                    return x
            return False
        
        def get_interact(self, e):
            if self.has_interact(e):
                return self.interactables[e]
        
        def add_interactable(self, name):
            self.interactables[name] = Interactable(name)
        
        def add_key(self, e, k):
            if self.has_interact(e):
                self.interactables[e].add_key(k)
        
        def add_name(self, e, name):
            if self.has_interact(e):
                self.interactables[name] = self.interactables[e]
        
        def add_object(self, name):
            self.objects.append(name)
        
        def take_object(self, name):
            if name in self.objects:
                self.objects.remove(name)
                inventory.append(name)
        
        def get_label_name(self):
            return self.label_name
    
    def create_path(a1, a2):
        a1.add_exit(a2)
        a2.add_exit(a1)

    def look():
        area = areas[store.area]
        if area.north:
            renpy.say(narrator, "To the north is the {b}" + area.north.name + "{/b}.")
        if area.east:
            renpy.say(narrator, "To the east is the {b}" + area.east.name + "{/b}.")
        if area.west:
            renpy.say(narrator, "To the west is the {b}" + area.west.name + "{/b}.")
        if area.south:
            renpy.say(narrator, "To the south is the {b}" + area.south.name + "{/b}.")
        for i in area.objects:
            renpy.say(narrator, "There is a {b}" + i + "{/b} here.")
        for npc in npcs:
            if areas[npc.current_location] == area:
                renpy.say(narrator, "{b}" + npc.name.upper()[0] + npc.name[1:] + "{/b} is standing here.")

#NPC

    class Npc:
        
        name = ""
        locations = []
        current_location = ""
        topics = []
        
        def __init__(self, name):
            self.name = name
            self.locations = []
            self.current_location = ""
            file = renpy.open_file("schedules/" + self.name + ".txt")
            for word in file:
                self.locations.append(word.decode("utf-8").strip())
            file.close()
            self.current_location = self.locations[0]
        
        def has_topic(self, e):
            for i in self.topics:
                if i == e:
                    return True
            return False
        
        def add_topic(self, e):
            self.topics.append(e)

# GAME SETUP

    npcs = [Npc("chel"),
    Npc("bia"),
    Npc("moa"),
    Npc("heron"),
    Npc("namara"),
    Npc("lady"),
    Npc("shera"),
    Npc("sosi"),
    Npc("doctor")
    ]
    
    areas = {"backyard_chel":Area("backyard", "backyard_chel"),
    "shop_chel":Area("shop", "shop_chel"),
    "kitchen_chel":Area("kitchen", "kitchen_chel"),
    "bathroom_chel":Area("bathroom", "bathroom_chel"),
    "bedroom_chel":Area("bedroom", "bedroom_chel"),
    
    "shop_heron":Area("shop", "shop_heron"),
    "kitchen_heron":Area("kitchen", "kitchen_heron"),
    "storage":Area("storage", "storage"),
    "bedroom_heron":Area("bedroom", "bedroom_heron"),
    "bathroom_heron":Area("bathroom", "bathroom_heron"),
    
    "path_town_1":Area("path", "path_town_1"),
    "path_town_2":Area("path", "path_town_2"),
    "path_manor":Area("path", "path_manor"),
    
    "bar":Area("bar", "bar"),
    "fields":Area("fields", "fields"),
    "shop_flowers":Area("shop", "shop_flowers"),
    "clinic":Area("clinic", "clinic"),
    "outhouse":Area("outhouse", "outhouse"),
    
    "farmhouse":Area("farmhouse", "farmhouse"),
    "bedroom_farmhouse":Area("bedroom", "bedroom_farmhouse"),
    
    "forest_path":Area("path", "forest_path"),
    "fp_1":Area("path", "fp_1"),
    "fp_2":Area("path", "fp_2"),
    "fp_3":Area("path", "fp_3"),
    "fp_4":Area("path", "fp_4"),
    "cave":Area("cave", "cave"),
    "waterfall":Area("waterfall", "waterfall"),
    
    "entry":Area("manor", "entry"),
    "parlor":Area("parlor", "parlor"),
    "hallway":Area("hallway", "hallway"),
    "bedroom_namara":Area("bedroom", "bedroom_namara"),
    "dining_room":Area("dining room", "dining_room"),
    "kitchen_namara":Area("kitchen", "kitchen_namara"),
    "upstairs":Area("upstairs", "upstairs"),
    "bedroom_master":Area("bedroom", "bedroom_master"),
    "bathroom_namara":Area("bathroom", "bathroom_namara"),
    
    "guest_cabin":Area("cabin", "guest_cabin"),
    "cabin_backyard":Area("backyard", "cabin_backyard")
    
    }
    
    create_path(areas["forest_path"], areas["path_manor"])
    create_path(areas["forest_path"], areas["cave"])
    create_path(areas["forest_path"], areas["fp_1"])
    
    create_path(areas["guest_cabin"], areas["path_manor"])
    create_path(areas["guest_cabin"], areas["cabin_backyard"])
    
    create_path(areas["entry"], areas["path_manor"])
    create_path(areas["parlor"], areas["entry"])
    create_path(areas["entry"], areas["hallway"])
    create_path(areas["upstairs"], areas["hallway"])
    create_path(areas["bedroom_namara"], areas["hallway"])
    create_path(areas["dining_room"], areas["hallway"])
    create_path(areas["upstairs"], areas["bedroom_master"])
    create_path(areas["upstairs"], areas["bathroom_namara"])
    create_path(areas["dining_room"], areas["kitchen_namara"])
    
    create_path(areas["backyard_chel"], areas["shop_chel"])
    create_path(areas["kitchen_chel"], areas["shop_chel"])
    create_path(areas["kitchen_chel"], areas["bathroom_chel"])
    create_path(areas["kitchen_chel"], areas["bedroom_chel"])
    
    create_path(areas["kitchen_heron"], areas["shop_heron"])
    create_path(areas["storage"], areas["shop_heron"])
    create_path(areas["kitchen_heron"], areas["bedroom_heron"])
    create_path(areas["bathroom_heron"], areas["bedroom_heron"])
    
    create_path(areas["path_town_1"], areas["path_manor"])
    create_path(areas["path_town_1"], areas["shop_chel"])
    create_path(areas["path_town_1"], areas["shop_heron"])
    create_path(areas["path_town_1"], areas["path_town_2"])
    
    create_path(areas["bar"], areas["path_town_2"])
    create_path(areas["fields"], areas["path_town_2"])
    create_path(areas["shop_flowers"], areas["path_town_2"])
    create_path(areas["clinic"], areas["path_town_2"])
    
    create_path(areas["fields"], areas["farmhouse"])
    create_path(areas["bedroom_farmhouse"], areas["farmhouse"])
    
    areas["entry"].add_south(areas["path_manor"])
    areas["path_manor"].add_south(areas["path_town_1"])
    areas["path_manor"].add_west(areas["forest_path"])
    areas["path_town_1"].add_south(areas["path_town_2"])
    areas["path_town_2"].add_south(areas["fields"])
    areas["fields"].add_east(areas["farmhouse"])
    areas["farmhouse"].add_east(areas["bedroom_farmhouse"])
    
    areas["guest_cabin"].add_west(areas["path_manor"])
    areas["guest_cabin"].add_east(areas["cabin_backyard"])
    
    areas["path_town_1"].add_west(areas["shop_chel"])
    areas["path_town_1"].add_east(areas["shop_heron"])
    
    areas["shop_chel"].add_west(areas["backyard_chel"])
    areas["shop_chel"].add_north(areas["kitchen_chel"])
    
    areas["forest_path"].add_west(areas["fp_1"])
    areas["fp_1"].add_north(areas["fp_2"])
    areas["fp_2"].add_west(areas["fp_3"])
    areas["fp_2"].add_east(areas["fp_4"])
    areas["fp_3"].add_west(areas["fp_4"])
    areas["fp_4"].add_north(areas["waterfall"])
    
    
    areas["backyard_chel"].add_object("hammer")
    areas["kitchen_chel"].add_interactable("larder")
    
    areas["kitchen_namara"].add_interactable("sink")
    areas["kitchen_namara"].add_key("sink", "glass")
    areas["kitchen_namara"].add_object("glass")
    areas["kitchen_namara"].add_object("bread")
    
    areas["shop_chel"].add_interactable("bag_of_gold")
    areas["shop_chel"].add_name("bag_of_gold", "bag")
    areas["shop_chel"].add_name("bag_of_gold", "gold")
    
    areas["guest_cabin"].add_interactable("wood_stove")
    areas["guest_cabin"].add_name("wood_stove", "stove")
    
    areas["cabin_backyard"].add_interactable("backyard_outhouse")
    areas["cabin_backyard"].add_name("backyard_outhouse", "outhouse")
    
    
    objects_texts = {
        "glass":"Glass\nAn empty glass for water."
    }
    
    area = "guest_cabin"

# TESTER FUNCTIONS
    def test_paths(area):
        st = areas[area].name + ": "
        for x in areas[area].exits:
            st += x.name
            st += " "
        return st
    
    debug = True

define l = Character("Lani", callback=voice, cb_file="bleep008.ogg", what_prefix='\"', what_suffix='\"')
define l_int = Character("Lani", what_prefix='(', what_suffix=')')
define o = Character("Old Heron", callback=voice, cb_file="bleep011.ogg", what_prefix='\"', what_suffix='\"')
define b = Character("Bia", callback=voice, cb_file="bleep027.ogg", what_prefix='\"', what_suffix='\"')
define m = Character("Moa", callback=voice, cb_file="bleep009.ogg", what_prefix='\"', what_suffix='\"')
define c = Character("Chel", callback=voice, cb_file="bleep019.ogg", what_prefix='\"', what_suffix='\"')
define y = Character("Young Namara", callback=voice, cb_file="bleep017.ogg", what_prefix='\"', what_suffix='\"')
define h = Character("Lady Heron", callback=voice, cb_file="bleep001.ogg", what_prefix='\"', what_suffix='\"')
define s = Character("Shera", callback=voice, cb_file="bleep010.ogg", what_prefix='\"', what_suffix='\"')
define i = Character("Sosi", callback=voice, cb_file="bleep003.ogg", what_prefix='\"', what_suffix='\"')
define d = Character("Doctor", callback=voice, cb_file="bleep030.ogg", what_prefix='\"', what_suffix='\"')

# The game starts here.

label start:

    python:
        if debug:
            renpy.jump("guest_cabin")
    
    "This game uses a text prompt mechanic. You can always type {b}\"h\"{/b}, {b}\"help\"{/b}, or {b}\"cmd\"{/b} for a full list of commands."
    "This is a mystery with multiple unique endings. Each new ending will reveal new information, so if you die, don't worry! You can always rollback to get another ending."
    "You can always press enter without inputting a command to progress time."
    "Please keep this in mind when playing! Have fun!"
    
    show lani at center
    "Your name is Lani Choe."
    "You're a researcher whose job is to investigate sites of magical importance."
    "About a year after graduating magic school, you receive a letter from one of your former classmates."
    
    show lani:
        faceright
        left
    show young:
        faceleft
        right
    y "Hello, Lani."
    y "My family is going to expand the mining operation soon."
    y "I was hoping that you could come by and investigate the caves in our town..."
    y "I know I never had your eye for magic stuff, and the mountain is really sacred. It would be good to get your opinion on it, if you're not too busy of course!"
    y "If you come, you can stay in our guest cabin. Just show up to Ba Meniri and show anyone this letter, they'll direct you to the manor."
    y "Thank you. Hope to see you soon!"
    y "- Young Namara"
    
    scene bg fields
    
    show lani at center
    l "Let's see..."
    l "There! Hello, miss."
    
    show lani:
        faceright
        left
    show moa:
        faceleft
        right
    m "Oh, hello! It's rare to see travelers here."
    l "Yeah, I'm Young Namara's friend. I was going to visit him."
    m "Oh! A friend! From school, I guess?"
    l "Yep. I've got this letter -"
    m "Let's see... Oh, yeah! I can take you to the manor house if you want. He's probably there right now."
    l "I wouldn't want to bother you."
    m "Oh, don't be silly! I'm on my way up the mountain anyway."
    l "I see. In that case, sure. Thank you."
    m "Great! This way!"
    
    scene bg path_town_2
    show lani:
        faceright
        left
    show moa:
        faceleft
        right
    m "I'm Moa, by the way."
    l "Nice to meet you. I'm Lani."
    m "Right. I saw on the letter, but I didn't know how to pronounce it!"
    m "Oh, maybe I should give you a bit of a tour."
    m "Up here is the flower shop, then on the other side is the bar and the clinic."
    m "I'm actually working at the bar tonight."
    
    scene bg path_town_1
    show lani:
        faceright
        left
    show moa:
        faceleft
        right
    m "On this side is the blacksmith's shop."
    m "This is the jewelry store where my sister and I work. I mean, I'm only there some days."
    
    scene bg path_manor
    show lani:
        faceright
        left
    show moa:
        faceleft
        right
    m "Well, here we are!"
    l "Thanks for the tour."
    m "No problem!"
    m "You can stop by the bar later, if you want! I'll introduce you to whoever's there."
    l "We'll see, I'm not sure what Young Namara wants from me tonight. But thanks for the invite."
    m "Of course! Well, see you later!"
    hide moa
    "You knock on the door, and it opens almost instantly."
    show young:
        faceleft
        right
    y "Who is it?"
    y "Oh, Lani! You came!"
    l "Yep. Nice to see you, Namara."
    y "Should I show you to the guest house? You can put down your bags first."
    l "Okay, sounds good."
    
    scene bg guest_cabin
    show young:
        faceright
        left
    show lani:
        faceleft
        right
    y "Here's the guest cabin. Sorry it's not much... There's a backyard with an outhouse. If you want, you can come to the main house to bathe and eat."
    l "Perfectly fine. I'm used to worse, in my travels."
    y "Oh, good! I mean - I'm sorry! But that's a relief for me."
    "You set your bags down at the foot of the bed."
    l "You probably want to go talk business elsewhere, right?"
    y "I don't mind! I mean, we can go sit in the parlor, if you want?"
    
    scene bg path_manor with dissolve
    pause 0.2
    scene bg entry with dissolve
    pause 0.2
    scene bg parlor with dissolve
    "You spent some time catching up with your friend over tea, and then he explained to you the situation."
    y "So, if you could, just spend some time "
    
    python:
        if not debug:
            renpy.jump("guest_cabin")
    
    scene bg backyard
    
    show bia:
        faceleft
        right
    b "test 1"
    show chel:
        faceleft
        right
    show bia:
        faceright
        left
    c "test 2"
    hide bia
    show chel:
        faceright
        left
    show moa:
        faceleft
        right
    m "test 3"
    hide chel
    show moa:
        faceright
        left
    show young:
        faceleft
        right
    y "test 4"
    hide moa
    show young:
        faceright
        left
    show old:
        faceleft
        right
    o "test 5"
    hide young
    show old:
        faceright
        left
    show lani:
        faceleft
        right
    l "test 6"
    hide old
    show lani:
        faceright
        left
    show lady:
        faceleft
        right
    l_int "test 7"
    hide lani
    show lady:
        faceright
        left
    show shera:
        faceleft
        right
    h "test 8"
    hide lady
    show shera:
        faceright
        left
    s "test 9"
    
    jump guest_cabin

label progress_0:

    "Progress time?"
    menu:
        "Yes":
            jump afternoon_1
        "No":
            $ renpy.jump(last_label)

label afternoon_1:

    l "asdfdasfasd"

    # This ends the game.

    return
