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

    c "asdf"
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_chel:

    "Chel Arn is a journeyman blacksmith. He's short, but well muscled – thanks to his work, obviously."
    "You don't know him very well, but you know he's a friend of Young Namara."
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_chel_about_chel:

    menu:
        "What have you been up to recently":
            c "You mean today? Just working. Gotta grind out some orders for the Namaras!"
            c "Nothing out of the ordinary. Pickaxes won't make themselves!"
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_chel_about_bia:

    c "Yeah, she's Moa's sister. They both work in town at the Herons' shop."
    c "Nice girls, both of them."
    c "...By the way, y'know, villagers can be gossipy... I wouldn't believe everything people tell you, necessarily."
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_chel_about_moa:

    c "Yeah, I know her. She's friends with Shera, so she comes by here pretty often!"
    c "I'm not sure if she's coming by today, though."
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_chel_about_heron:

    c "Old Heron is one of the most respected merchants in town. Everyone knows him."
    c "I've done business with him myself, from time to time. He's a good dude."
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_chel_about_namara:

    c "Oh yeah, he's cool. I mean, you two are friends, right?"
    c "You probably know him a lot better than I do. I mean, he was away from the town for so long and just got back recently."
    c "I like hanging out with him, but he's so quiet. Sometimes I feel like I don't know anything about him."
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_chel_about_lady:

    c "Lady Heron also runs the jewelry store. She's a really nice lady."
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_chel_about_shera:

    c "My apprentice? Well... What do you wanna know?"
    c "She's been working for me for about a year now."
    c "Before that she was apprenticing in another village, because I wasn't a journeyman yet, so there was nobody here to teach her."
    c "Shera is... Not the brightest, but she certainly livens up the place! So I can't complain too much."
    c "Although if you know any qualified smiths who're looking for work then I certainly wouldn't mind if you sent them my way."
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_chel_about_sosi:

    c "The guy who runs the flower shop? Mhm, I know the one you're talking about."
    c "Seems like they're doing some good business over there."
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_chel_about_doctor:

    c "That guy is a life saver. He works really hard and he always has medicines in stock, for every kind of sickness."
    hide chel
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))


#TALK TO MOA
label talk_moa:

    m "asdf"
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_moa:

    "Moa is a local shop girl. She's pretty short and doesn't seem very muscular."
    "You've gathered from your short time here that Moa has a good reputation in town."
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_moa_about_chel:

    m "Right, you mean Shera's boss? I mean, she complains sometimes, but he seems pretty laidback to me."
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_moa_about_bia:

    m "My sister, yeah, she works at the jewelry store too."
    m "She hangs out up the mountain most often. Her and every guy in the village."
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_moa_about_moa:

    menu:
        "What have you been up to recently?":
            m "Same as usual, really. I work two jobs, so that keeps me pretty busy."
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_moa_about_heron:

    m "Old Heron is a good man. He's been nothing but kind to me and my sister."
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_moa_about_namara:

    m "Oh, I don't talk to him much I mean, he's really important in the town."
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_moa_about_lady:

    m "Lady Heron is like a second mother to everyone who grew up here. Including me and Bia."
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_moa_about_shera:

    m "Me and Shera have been friends since we were kids!"
    m "Since we were neighbors, I probably spent more time at her house than mine."
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_moa_about_sosi:

    m "He's really nice! He gives me really good recommendations whenever I go to buy flowers."
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_moa_about_doctor:

    m "I hardly ever see him, he's always at the clinic. Seems like a really hardworking person!"
    hide moa
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))


#TALK TO BIA
label talk_bia:

    b "asdf"
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_bia:

    "Bia is a local shop girl. She's tall, but not muscular."
    "Bia seems to be a bit infamous for petty crime and leading young men astray."
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_bia_about_chel:

    b "Hmm... I don't know very much."
    b "I see him out walking around the caves, sometimes, but we've never exchanged more than a greeting."
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_bia_about_bia:

    menu:
        "What have you been up to recently?":
            b "Recently? Well, it's been raining a lot. As I'm sure you know, there are a lot of magicks that can only be worked during this season."
            l "So you're doing spells? Like what?"
            b "Oh, I didn't mean that... Don't read too much into what I say."
            l_int "What did you mean, then?"
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_bia_about_moa:

    b "I'm sure you've heard a lot of good things about her already."
    b "I have nothing to add. My sister is a good girl. Heaven knows nobody's ever given her any reason not to be."
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_bia_about_heron:

    b "Yes, I work in his shop sometimes. He's a nice old man, but I wonder how much longer he plans to run that shop for."
    b "Not to imply anything about his mental state, just, it can't be easy to appraise items when your vision is going."
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_bia_about_namara:

    b "I like Young Namara just fine. Oh, that's right, you two are friends, right?"
    b "That's cool."
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_bia_about_lady:

    b "Honestly, I don't talk with her much. I just work for the woman."
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_bia_about_shera:

    b "Moa would be able to tell you more than me. Those two are practically attached at the hip."
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_bia_about_sosi:

    b "He seems a little odd, but he's sweet."
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_bia_about_doctor:

    b "He's good at what he does. If a bit judgmental, maybe."
    hide bia
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))


#TALK TO OLD HERON
label talk_heron:

    o "asdf"
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_heron:

    "Old Heron is the owner of the jewelry store, along with his wife. He appears quite feeble."
    "He's respected amongst the townsfolk."
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_heron_about_chel:

    o "Oh, he's a fine young man. Very hardworking, but not too serious!"
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_heron_about_bia:

    o "Well, she's not the worst employee in the world."
    o "I think she's a bit... troubled."
    o "My wife caught her stealing from the store once. I could hardly believe it at first, but of course Pari would never lie to me."
    o "Since then she's been a bit better-behaved. Oh, did we ever give her a stern warning."
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_heron_about_moa:

    o "Moa is a very respectable young lady! Whoever marries her will be a lucky man."
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_heron_about_heron:

    menu:
        "What have you been up to recently?":
            o "Recently? Oh, recently the weather has been hell on my joints. The lady and I have been going on short walks, just to keep active, you know."
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_heron_about_namara:

    o "I wish he would be a little friendlier with the other kids. Oh, I suppose they're not kids anymore, though..."
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_heron_about_lady:

    o "We've been married for almost fifty years now. I know her habits like I know my own left foot!"
    o "If you ever need anything from either of us, Lani, don't hesitate to ask. We're usually at home these days."
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_heron_about_shera:

    o "Those girls like to eat lunch together in the shop. We love having her over! She's a very respectful guest."
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_heron_about_sosi:

    o "Sosi is a newcomer to town, and he's already so successful!"
    o "Reminds me of Pari, back in the day. You know we met in the city?"
    o "But she agreed to move back here with me. And she took to the small town life like a duck to water!"
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_heron_about_doctor:

    o "Yes, I see him at the clinic sometimes. Although you know, despite my age, I'm quite healthy!"
    o "I hardly ever see the doctor anywhere but the clinic. I hope he isn't overworking himself..."
    hide old
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))


#TALK TO YOUNG NAMARA
label talk_namara:

    y "asdf"
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_namara:

    "Young Namara is the heir of Namara family, who run the mining operation."
    "He is tall, but you don't think he's got much muscle hiding under there."
    "You two went to secondary school together near his mother's hometown in Ba Hamavi."
    "He's cripplingly shy, and not a very interesting conversationalist, but he has his uses."
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_namara_about_chel:

    y "Ah, yeah! Chel is really cool. I'm glad you two got to finally meet each other!"
    y "It's like my two worlds colliding. My best school friend and my best home friend. It's a little weird for me, actually."
    y "Not in a bad way or anything!"
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_namara_about_bia:

    y "Oh, that's Moa's sister, right?"
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_namara_about_moa:

    y "Yeah, I know her, she's very friendly."
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_namara_about_heron:

    y "When I came back home, I was shocked that Old Heron is still running that shop! I thought for sure he would have retired by now."
    y "I'm glad he at least has Moa and Bia to help him now!"
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_namara_about_namara:

    menu:
        "What have you been up to recently?":
            y "Well, you know, I've been busy."
            y "Lots to do for the mines. And my parents are away, too..."
            y "I don't mind, though. It's nice to be needed."
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_namara_about_lady:

    y "Oh, yes, she comes up here sometimes!"
    y "I let her have access to some of our books."
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_namara_about_shera:

    y "She's Moa's friend, right?"
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_namara_about_sosi:

    y "Oh, yeah, him. I haven't really been to the flower shop, so I couldn't tell you much."
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_namara_about_doctor:

    y "Let's see... I see him a couple times a year for a check-up. He seems very... professional?"
    hide young
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))


#TALK TO LADY HERON
label talk_lady:

    h "asdf"
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_lady:

    "Lady Heron is the owner of the jewelry store along with her husband. She's healthy for her age, but still not strong."
    "She's respected by most of the townsfolk."
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_lady_about_chel:

    h "The blacksmith? He's a good kid and a great teacher. You wouldn't think it, but he's gotten a lot of good work out of Shera!"
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_lady_about_bia:

    h "Bia? Yes, she works at the shop sometimes."
    h "She's been doing her job okay recently."
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_lady_about_moa:

    h "Yes, she works for us! A sweet girl. Good worker, too. Although you'd think tending our little shop would be the easiest job in the world..."
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_lady_about_heron:

    h "You know, we've been married for fifty years now!"
    h "That's half a century! Time just flies, doesn't it?"
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_lady_about_namara:

    h "I'm sure I don't have to tell you, but that boy is not a very good conversationalist."
    h "It's okay. Not everyone has to be a social butterfly!"
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_lady_about_lady:

    menu:
        "What have you been up to recently?":
            h "Not much. Cooking and reading, mostly!"
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_lady_about_shera:

    h "I like her. She's an odd one."
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_lady_about_sosi:

    h "Oh, my husband and I visit him often since he's just across the street!"
    h "I remember back when he first moved in, we would bring him food all the time. I wish we could do things like that more often now, but, you know, being old."
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_lady_about_doctor:

    h "He's a handsome fellow! And we're lucky to have the clinic so close by. If anything ever happens, he's just right there!"
    hide lady
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))


#TALK TO SHERA
label talk_shera:

    s "asdf"
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_shera:

    "Shera is Chel's apprentice. She's average height and pretty muscular."
    "You think she's friends with Moa."
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_shera_about_chel:

    s "Yeah, he's fine sometimes. And then some days he makes me do his job while he goes off to the waterfall or whatever."
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_shera_about_bia:

    s "Moa's sister totally freaks me out... Like, yikes."
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_shera_about_moa:

    s "She owes me lunch right now. But yeah, she's cool."
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_shera_about_heron:

    s "He's great! Moa says he's the chillest boss ever."
    s "Must be nice for her..."
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_shera_about_namara:

    s "Oh, wow, it's been forever since I talked to Namara."
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_shera_about_lady:

    s "She's a great cook."
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_shera_about_shera:

    menu:
        "What have you been up to recently?":
            s "Work, work, work. Nothing more than that."
            s "I guess the miners need equipment, so, whatever."
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_shera_about_sosi:

    s "asdf"
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_shera_about_doctor:

    s "asdf"
    hide shera
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))


#TALK TO SOSI
label talk_sosi:

    i "asdf"
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_sosi:

    "Sosi runs the flower shop, apparently. He's tall but pretty skinny."
    "It seems like he doesn't get out much since he runs this place alone, so the only people he knows are the other shopkeepers, but they seem to like him okay."
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_sosi_about_chel:

    i "asdf"
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_sosi_about_bia:

    i "asdf"
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_sosi_about_moa:

    i "asdf"
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_sosi_about_heron:

    i "asdf"
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_sosi_about_namara:

    i "asdf"
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_sosi_about_lady:

    i "asdf"
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_sosi_about_shera:

    i "asdf"
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_sosi_about_sosi:

    i "asdf"
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_sosi_about_doctor:

    i "asdf"
    hide sosi
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))


#TALK TO DOCTOR
label talk_doctor:

    d "asdf"
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_at_doctor:

    "The doctor runs the clinic. He's short but quite muscular."
    "He seems very busy here in the clinic, but you haven't heard a bad word about him."
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_doctor_about_chel:

    d "asdf"
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_doctor_about_bia:

    d "asdf"
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_doctor_about_moa:

    d "asdf"
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_doctor_about_heron:

    d "asdf"
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_doctor_about_namara:

    d "asdf"
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_doctor_about_lady:

    d "asdf"
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_doctor_about_shera:

    d "asdf"
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_doctor_about_sosi:

    d "asdf"
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label talk_doctor_about_doctor:

    d "asdf"
    hide doctor
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))


#CHEL BACKYARD
label backyard_chel:
    scene bg backyard
    $ area = "backyard_chel"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_backyard_chel:
    "This is a covered backyard where Chel and his apprentice work."
    "There are two anvils and some metal and tools laying around."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL SHOP
label shop_chel:
    scene bg shop_1
    $ area = "shop_chel"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_shop_chel:
    "There's a counter with some daily necessities for sale, probably the kinds of things the apprentice makes during downtime."
    "Nails, various sorts of knives, hammers and files..."
    "Leaning against the wall are some half-finished projects."
    "Behind the counter is a {b}bag of gold.{/b}"
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL KITCHEN
label kitchen_chel:
    scene bg kitchen_chel
    $ area = "kitchen_chel"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_kitchen_chel:
    "The kitchen is narrow and crowded. Utensils and cooking pots line the shelves."
    "There's a table and two chairs in the corner."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CHEL BATHROOM
label bathroom_chel:
    scene bg bathroom_chel
    $ area = "bathroom_chel"
    $ last_label = area
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_fp_1:
    "Where are you?"
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FOREST PATH PUZZLE 2 
label fp_2:
    scene bg fp_2
    $ area = "fp_2"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_fp_2:
    "Where are you?"
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FOREST PATH PUZZLE 3
label fp_3:
    scene bg fp_3
    $ area = "fp_3"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_fp_3:
    "Where are you?"
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FOREST PATH PUZZLE 4
label fp_4:
    scene bg fp_4
    $ area = "fp_4"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_fp_4:
    "Where are you?"
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#WATERFALL
label waterfall:
    scene bg waterfall
    $ area = "fp_4"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_waterfall:
    "The mountain water here is fresh and clear. Someone who's inclined to remark on such things might call it beautiful."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CAVE
label cave:
    scene bg cave
    $ area = "cave"
    $ last_label = area
    $ rendernpc()
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
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_guest_cabin:
    "Your friend Young Namara graciously let you stay in this cabin for the duration of your visit."
    "The main room is used for cooking, sleeping and eating, so there's not much else here."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CABIN BACKYARD
label cabin_backyard:
    scene bg cabin_backyard
    $ area = "cabin_backyard"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_cabin_backyard:
    "There's a little veggie garden in here, but none of the plants are in season right now."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FIELDS
label fields:
    scene bg fields
    $ area = "fields"
    $ last_label = area
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_outhouse:
    "It's a relatively clean public outhouse."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#FLOWER SHOP
label shop_flowers:
    scene bg flower shop
    $ area = "shop_flowers"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_shop_flowers:
    "This is an upscale shop with plate glass windows."
    "There are arrangements with gorgeous flowering shrubs in the window display."
    "Along the walls stand smaller flowerpots with single flowers."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#CLINIC
label clinic:
    scene bg clinic
    $ area = "clinic"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_clinic:
    "This doesn't appear to be a place for treating patients, but rather a place to buy various remedies."
    ""
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#JEWELRY SHOP
label shop_heron:
    scene bg shop_heron
    $ area = "shop_heron"
    $ last_label = area
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_entry:
    "The Namara manor is so big it has its own entry hall."
    "There are two coat racks and several pairs of snow boots on the floor."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#HALLWAY
label hallway:
    scene bg hallway
    $ area = "hallway"
    $ last_label = area
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_hallway:
    "The large entry funnels into a high-ceilinged hallway with several sets of sliding doors."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#PARLOR
label parlor:
    scene bg parlor
    $ area = "parlor"
    $ last_label = area
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_kitchen_namara:
    "It seems Lady Namara doesn't have servants, so this nice kitchen is probably her own."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

#MANOR BATHROOM
label bathroom_namara:
    scene bg bathroom_namara
    $ area = "bathroom_namara"
    $ last_label = area
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
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
    $ rendernpc()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))

label look_bedroom_master:
    "Old Namara and Lady Namara must keep all their things together, because there's only one wardrobe and one trunk."
    $ look()
    $ renpy.jump(inp("Type \'help\', \'cmd\' or \'h\' for a list of commands."))
