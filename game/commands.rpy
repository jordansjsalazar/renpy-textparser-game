#GENERAL
label use_fail:
    "Use what?"
    $ renpy.jump(last_label)

label enter_fail:
    "Go where?"
    $ renpy.jump(last_label)

label take_fail():
    "Take what?"
    $ renpy.jump(last_label)

label fail:
    "Unfortunately, you can't do that here."
    $ renpy.jump(last_label)

label inv:
    label inventory:
        if inventory:
            python:
                invString = ""
                for i in inventory:
                    if i in objects_texts:
                        renpy.say(narrator, objects_texts[i])
                    else:
                        invString += i+"\n"
                if invString != "\n":
                    renpy.say(narrator, invString)
        else:
            "Inventory is empty!"
        $ renpy.jump(last_label)

label cmd:
    "Commands: {b}look, look at, use, take, enter, north, south, east, west, inventory.{/b}"
    "You can also simply type {b}n, s, e, w{/b} for directions and {b}inv{/b} to view inventory."
    "If you use the {b}\"look\"{/b} command, some interactable objects may be pointed out."
    "Additionally, you can sometimes {b}use{/b} some items from your {b}inventory{/b}."
    "You can choose to progress time by simply pressing enter."
    $ renpy.jump(last_label)

#CHEL BACKYARD
label backyard_chel:
    scene bg backyard
    $ area = "backyard_chel"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_hammer:
    "Took the hammer."
    $ areas[area].take_object("hammer")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL SHOP
label shop_chel:
    scene bg shop_1
    $ area = "shop_chel"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_bag_of_gold:
    "You debated the ethics of stealing gold from your cousin."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL KITCHEN
label kitchen_chel:
    scene bg kitchen_chel
    $ area = "kitchen_chel"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_glass:
    "Took the glass."
    $ areas[area].take_object("glass")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_bread:
    "Took the bread."
    $ areas[area].take_object("bread")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_sink:
    "You don't want to waste water."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label use_glass_on_sink:
    $ use_item("glass")
    "Filled up the glass."
    $ areas["kitchen"].add_object("full_glass")
    $ areas["kitchen"].take_object("full_glass")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL BATHROOM
label bathroom_chel:
    scene bg bathroom_chel
    $ area = "bathroom_chel"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL BEDROOM
label bedroom_chel:
    scene bg bedroom_chel
    $ area = "bedroom_chel"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#PATH 1
label path_town_1:
    scene bg path_town_1
    $ area = "path_town_1"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#PATH 1
label path_town_2:
    scene bg path_town_2
    $ area = "path_town_2"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#PATH MANOR
label path_manor:
    scene bg path_manor
    $ area = "path_manor"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#GUEST CABIN
label guest_cabin:
    scene bg guest_cabin
    $ area = "guest_cabin"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CABIN BACKYARD
label cabin_backyard:
    scene bg cabin_backyard
    $ area = "cabin_backyard"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))
