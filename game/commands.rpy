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

#BACKYARD
label backyard:
    scene bg backyard
    $ area = "backyard"
    $ last_label = "backyard"
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_hammer:
    "Took the hammer."
    $ areas[area].take_object("hammer")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#SHOP
label shop:
    scene bg shop_1
    $ area = "shop_1"
    $ last_label = "shop"
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_bag_of_gold:
    "You debated the ethics of stealing gold from your cousin."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#KITCHEN
label kitchen:
    scene bg kitchen
    $ area = "kitchen"
    $ last_label = "kitchen"
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_glass:
    "Took the glass."
    $ areas[area].take_object("glass")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_bread:
    "Took the bread."
    $ areas[area].take_object("bread")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

