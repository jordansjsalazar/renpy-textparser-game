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

label talk_fail():
    "Talk to who?"
    $ renpy.jump(last_label)

label fail:
    "Unfortunately, you can't do that here."
    $ renpy.jump(last_label)

label inv:
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
    "Commands: {b}look, look at, use, take, talk to, enter, north, south, east, west, inventory.{/b}"
    "You can also simply type {b}n, s, e, w{/b} for directions and {b}inv{/b} to view inventory."
    "If you use the {b}\"look\"{/b} command, some interactable objects may be pointed out."
    "You can {b}use{/b} objects in your inventory as well as objects in the environment."
    "Additionally, you can {b}use{/b} objects from your {b}inventory{/b} on objects in the environment."
    "NPCs in the area will not be visible on screen until you {b}talk to{/b} them, so you should {b}look{/b} to see who's around sometimes."
    "You can choose to progress time by simply pressing enter."
    $ renpy.jump(last_label)

label progress:
    $ time_check()
    $ renpy.say(narrator, "Current time: " + str(time) + " out of 100")
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#TALK TO CHEL
label talk_chel:
    show chel at center
    c "asdf"
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_chel:
    show chel at center
    "Chel Arn is a journeyman blacksmith. He's short, but well muscled – thanks to his work, obviously."
    "You don't know him very well, but you know he's a friend of Young Namara."
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#TALK TO MOA
label talk_moa:
    show moa at center
    m "asdf"
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_moa:
    show moa at center
    "Moa is a local shop girl. She's pretty short and doesn't seem very muscular."
    "You've gathered from your short time here that Moa has a good reputation in town."
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#TALK TO BIA
label talk_bia:
    show bia at center
    b "asdf"
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_bia:
    show bia at center
    "Bia is a local shop girl. She's tall, but not muscular."
    "Bia seems to be a bit infamous for petty crime and leading young men astray."
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#TALK TO OLD HERON
label talk_heron:
    show old at center
    o "asdf"
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_heron:
    show old at center
    "Old Heron is the owner of the jewelry store, along with his wife. He appears quite feeble."
    "He's respected amongst the townsfolk."
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#TALK TO YOUNG NAMARA
label talk_namara:
    show young normal at center
    y "asdf"
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_namara:
    show young normal at center
    "Young Namara is the heir of Namara family, who run the mining operation."
    "He is tall, but you don't think he's got much muscle hiding under there."
    "You two went to secondary school together near his mother's hometown in Ba Hamavi."
    "He's cripplingly shy, and not a very interesting conversationalist, but he has his uses."
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL BACKYARD
label backyard_chel:
    scene bg backyard
    $ area = "backyard_chel"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_backyard_chel:
    "This is a covered backyard where Chel and his apprentice work."
    "There are two anvils and some metal and tools laying around."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_hammer:
    "It's a hammer. Probably weighs about 3 pounds."
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

label look_shop_chel:
    "There's a counter with some daily necessities for sale, probably the kinds of things the apprentice makes during downtime."
    "Nails, various sorts of knives, hammers and files..."
    "Leaning against the wall are some half-finished projects."
    "Behind the counter is a {b}bag of gold.{/b}"
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_bag_of_gold:
    "It's pretty full."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label interact_bag_of_gold:
    "You debated the logistics of stealing gold from the shop, but decided against it."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL KITCHEN
label kitchen_chel:
    scene bg kitchen_chel
    $ area = "kitchen_chel"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_kitchen_chel:
    "The kitchen is narrow and crowded. Utensils and cooking pots line the shelves."
    "There's a table and two chairs in the corner."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_larder:
    "You can open the larder using the handle."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label use_larder:
    "Inside the larder, there are a few cuts of meat and some fresh vegetables."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL BATHROOM
label bathroom_chel:
    scene bg bathroom_chel
    $ area = "bathroom_chel"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_bathroom_chel:
    "A pretty normal bathroom."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL BEDROOM
label bedroom_chel:
    scene bg bedroom_chel
    $ area = "bedroom_chel"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_bedroom_chel:
    "The ceiling in this room is quite short. It's a bit uncomfortable to stand in, but might be cozy for sleeping."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#PATH 1
label path_town_1:
    scene bg path_town_1
    $ area = "path_town_1"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_path_town_1:
    "The path continues uphill to the manor, and further downhill through the town."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#PATH 2
label path_town_2:
    scene bg path_town_2
    $ area = "path_town_2"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_path_town_2:
    "The path continues uphill through town and downhill to the fields."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#PATH MANOR
label path_manor:
    scene bg path_manor
    $ area = "path_manor"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_path_manor:
    "The path here diverges into a trail leading into the wilderness."
    "Downhill, it leads you all the way through the main drag of the town."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FOREST PATH
label forest_path:
    scene bg forest_path
    $ area = "forest_path"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_forest_path:
    "The trail from the manor goes into a nice bit of forest."
    "You suppose the nobles still enjoy a good hike from time to time."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FOREST PATH PUZZLE ENTRY   
label fp_1:
    scene bg fp_1
    $ area = "fp_1"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_fp_1:
    "Where are you?"
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FOREST PATH PUZZLE 2 
label fp_2:
    scene bg fp_2
    $ area = "fp_2"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_fp_2:
    "Where are you?"
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FOREST PATH PUZZLE 3
label fp_3:
    scene bg fp_3
    $ area = "fp_3"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_fp_3:
    "Where are you?"
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FOREST PATH PUZZLE 4
label fp_4:
    scene bg fp_4
    $ area = "fp_4"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_fp_4:
    "Where are you?"
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CAVE
label cave:
    scene bg cave
    $ area = "cave"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_cave:
    "It's not blocked off. You suppose the miners use another entrance."
    "This part of the cave system might be a meeting point. Cool against the heat, and the sloped rock wall provides room for sitting."
    "You imagine kids might play here, on a day when it isn't raining."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#GUEST CABIN
label guest_cabin:
    scene bg guest_cabin
    $ area = "guest_cabin"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_guest_cabin:
    "Your friend Young Namara graciously let you stay in this cabin for the duration of your visit."
    "The main room is used for cooking, sleeping and eating, so there's not much else here."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_wood_stove:
    "There's a bit of wood still in the stove."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label use_wood_stove:
    "The stove isn't lit."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CABIN BACKYARD
label cabin_backyard:
    scene bg cabin_backyard
    $ area = "cabin_backyard"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_cabin_backyard:
    "There's a little veggie garden in here, but none of the plants are in season right now."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_backyard_outhouse:
    "It's an outhouse. Nothing weird in there."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label use_backyard_outhouse:
    "You use the outhouse."
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FIELDS
label fields:
    scene bg fields
    $ area = "fields"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_fields:
    "The land here is flat, so you can see many fields and a few farmers at work."
    "One cabin near the path stands out to you. The rest are far off on the horizon."
    "There's a river flowing perpendicular to the path, ending the road through town."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FARMHOUSE
label farmhouse:
    scene bg farmhouse
    $ area = "farmhouse"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_farmhouse:
    "The room is completely barren. An empty fire pit is built against one wall, but no cooking equipment is nearby."
    "The short table in the corner of the room looks as though it hasn't been used recently."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FARMHOUSE BEDROOM
label bedroom_farmhouse:
    scene bg bedroom_farmhouse
    $ area = "bedroom_farmhouse"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_bedroom_farmhouse:
    "There are two twin beds against the walls."
    "Snooping in the trunks, the only other piece of furniture, reveals that two women live here."
    "One seems to like darker colors, while one wears light-colored robes."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#BAR
label bar:
    scene bg bar
    $ area = "bar"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_bar:
    "The back of the bar is lined with kegs of ale. The room holds a few solemn guests and a few more sociable parties."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#OUTHOUSE
label outhouse:
    scene bg outhouse
    $ area = "outhouse"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_outhouse:
    "It's a relatively clean public outhouse."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FLOWER SHOP
label shop_flowers:
    scene bg shop_flowers
    $ area = "shop_flowers"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_shop_flowers:
    "This is an upscale shop with plate glass windows."
    "There are arrangements with gorgeous flowering shrubs in the window display."
    "Along the walls stand smaller flowerpots with single flowers."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CARPENTRY SHOP
label shop_carpentry:
    scene bg shop_carpentry
    $ area = "shop_carpentry"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_shop_carpentry:
    "There are three workbenches towards the back of the room, and a few display pieces towards the front."
    "On top of the larger furniture are some smaller wooden toys and other household items."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CARPENTRY SHOP
label shop_heron:
    scene bg shop_heron
    $ area = "shop_heron"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_shop_heron:
    "Old Heron runs this jewelry shop."
    "The sample pieces are fenced in behind a mesh net to prevent stealing."
    "To one side of the room is a nice little table set for two. It seems he hosts visitors in this room often."
    "There's a workbench behind the counter with some tools for appraising gems."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#HERON KITCHEN
label kitchen_heron:
    scene bg kitchen_heron
    $ area = "kitchen_heron"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_kitchen_heron:
    "The kitchen is open and sunny."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#HERON BATHROOM
label bathroom_heron:
    scene bg bathroom_heron
    $ area = "bathroom_heron"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_bathroom_heron:
    "The Herons' bathroom. It seems that the family has a very clear aesthetic for their house."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#HERON BEDROOM
label bedroom_heron:
    scene bg bedroom_heron
    $ area = "bedroom_heron"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_bedroom_heron:
    "The Herons' bed is neatly made. There's a stack of ornamental quilts on the chair in the corner."
    "The art and tapestries on the wall look very unique. They don't look Saavi, but they're clearly not from around here, either."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#STORAGE
label storage:
    scene bg storage
    $ area = "storage"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_storage:
    "The storage room is lined with shelves."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#ENTRY
label entry:
    scene bg entry
    $ area = "entry"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_entry:
    "The Namara manor is so big it has its own entry hall."
    "There are two coat racks and several pairs of snow boots on the floor."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#PARLOR
label parlor:
    scene bg parlor
    $ area = "parlor"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_parlor:
    "The parlor has paper screen windows, making it a bit dim."
    "The table in the middle is currently unset, but the cabinets of porcelain don't look dusty."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#DINING ROOM
label dining_room:
    scene bg dining_room
    $ area = "dining_room"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_dining_room:
    "The room smells like dried flowers."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#MANOR KITCHEN
label kitchen_namara:
    scene bg kitchen_namara
    $ area = "kitchen_namara"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_kitchen_namara:
    "It seems Lady Namara doesn't have servants, so this nice kitchen is probably her own."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_glass:
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_bread:
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_sink:
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

#MANOR BATHROOM
label bathroom_namara:
    scene bg bathroom_namar
    $ area = "bathroom_namara"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_bathroom_namara:
    "The high window gives a beautiful view over the town."
    "Kind of pointless since you can't see it during 95%% of the activities taking place in this room."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#NAMARA BEDROOM
label bedroom_namara:
    scene bg bedroom_namara
    $ area = "bedroom_namara"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_bedroom_namara:
    "There aren't any papers on or in the writing desk."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#UPSTAIRS
label upstairs:
    scene bg upstairs
    $ area = "upstairs"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_upstairs:
    "The window faces the forest, filtering in the smell of wet trees."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#MASTER BEDROOM
label bedroom_master:
    scene bg bedroom_master
    $ area = "bedroom_master"
    $ last_label = area
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_bedroom_master:
    "Old Namara and Lady Namara must keep all their things together, because there's only one wardrobe and one trunk."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))
