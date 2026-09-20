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

label look_twigs:
    "There are a lot of twigs on the ground."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_twigs:
    "You pick up a few of the twigs."
    $ areas[area].add_object("twigs")
    $ areas[area].take_object("twigs")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))
    
label look_cave_salt:
    "The salt scattered around the cave forms a circle."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_cave_salt:
    "You disturb the lines of the salt."
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

label look_at_necklace:
    "The necklace consists of a gold chain and a long pendant inlaid with jewels. On the back of the pendant, some runes are carved."
    "You can tell the runes spell a proper name in magical script, but you aren't familiar with the entity they invoke."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_necklace:
    "You can't take that, at least not without permission from the Herons."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_salt:
    "There's a bag of salt on the counter."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_salt:
    "Took the salt."
    $ areas[area].take_object("salt")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_knife:
    "The knife is a general purpose one, around 10cm long with a pointed end, for chopping vegetables and such."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_knife:
    "The Herons will probably notice their knife going missing, and you haven't asked them if you can take it."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))
    
label look_at_flint:
    "A small flint and steel for firestarting."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_flint:
    "Took the flint."
    $ areas[area].take_object("flint")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_gravel:
    "Around the outhouse are some small stones of gravel. You eventually look down the chute and see that dumped on top of the usual waste, there's a pile of gravel."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_gravel:
    "It's been dropped down the chute of the outhouse. You aren't touching that."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_body:
    "The dead body clearly belongs to Moa Heron."
    "She appears to have had her throat slit with a blade and bled out from the jugular."
    "The body is otherwise undisturbed."
    "The water around the corpse is stained red."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label take_body:
    "Moa's body is too heavy for you to lift."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))
