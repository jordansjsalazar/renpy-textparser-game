#INTERACTABLES

label look_at_larder:
    "You can open the larder using the handle."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_larder:
    "Inside the larder, there are a few cuts of meat and some fresh vegetables."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_sink:
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

label look_at_bag_of_gold:
    "It's pretty full."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_bag_of_gold:
    "You debated the logistics of stealing gold from the shop, but decided against it."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_wood_stove:
    "There's a bit of wood still in the stove."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_wood_stove:
    "The stove isn't lit."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_backyard_outhouse:
    "It's an outhouse. Nothing weird in there."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_backyard_outhouse:
    "You use the outhouse."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_path_gravel:
    "There's a pile of gravel on the side of the road. Probably the town is planning to re-pave the main dirt road with gravel."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_path_gravel:
    "You take some gravel from the pile."
    $ areas[area].add_object("gravel")
    $ areas[area].take_object("gravel")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_plant:
    "The plant in the window display appears to be some kind of shrub, barely flowering with small white flowers."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_plant:
    "You'd better not touch that plant unless you're prepared to pay for it."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_wheelbarrow:
    "The wheelbarrow is lined with a blanket."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_wheelbarrow:
    "You test the wheelbarrow. It rolls easily and feels surprisingly light to push."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_path_gravel:
    "There are a lot of twigs on the ground."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_path_gravel:
    "You pick up a few of the twigs."
    $ areas[area].add_object("twigs")
    $ areas[area].take_object("twigs")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#OBJECTS

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

    areas["storage"].add_object("necklace")
    areas["kitchen_heron"].add_object("salt")
    areas["kitchen_heron"].add_object("knife")
    areas["kitchen_heron"].add_object("flint and steel")
    areas["path_town_1"].add_object("gravel")
    areas["waterfall"].add_object("body")
    areas["cave"].add_interact("salt")