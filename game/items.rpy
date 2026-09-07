label look_at_glass:
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_glass:
    "Took the glass."
    $ areas[area].take_object("glass")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_bread:
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_bread:
    "Took the bread."
    $ areas[area].take_object("bread")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_hammer:
    "It's a hammer. Probably weighs about 3 pounds."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_hammer:
    "Took the hammer."
    $ areas[area].take_object("hammer")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))