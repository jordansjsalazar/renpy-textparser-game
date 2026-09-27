label beginning:

    scene bg wall with dissolve
    show guard at center
    g "Halt!"
    l "Is there a problem?"
    g "Regrettably, yes. Outsiders are forbidden to enter the mountain this week without proper authorization."
    l "Yes, I have a letter from Young Namara."
    g "Oh, so you do. My apologies, sir! Please come inside."
    scene bg path_town_2 with dissolve
    pause 0.2
    scene bg path_town_1 with dissolve
    pause 0.2
    scene bg path_manor with dissolve
    pause 0.2
    scene bg parlor with dissolve
    show namara at center
    y "Ah! You made it. I'm glad. Erm, please sit down!"
    l_int "He gestured to a chair and poured me a cup of tea as I took a seat."
    y "So as you know, I'm looking to expand the mining operation soon. Maybe in the fall."
    y "But a lot of the villagers think the mountain has some crazy magic buried inside, and, well, I don't think they think that for no reason."
    y "So I was just wondering if you could maybe ask around, some of the people here have some stories and maybe you could tell if they were true."
    y "I mean, you were always much better at that kind of stuff than me."
    menu:
        "Investigating magic, you mean.":
            y "Yeah, exactly."
            l "Well, it is my job. No need to feel bad about calling the expert."
        "Talking to people?":
            y "Ah - Well, that too...."
            y "I meant about investigating magic stuff, though."
            l "I know, I know."
    show lani at left
    show namara at right
    l "Hahhh... I was looking forward to a nice vacation, though. And now you're making me work..."
    y "It's not exactly hard work. Just go around and talk to people, that's basically all I'm asking."
    y "You can stay in the guest cabin. It's just South and then East of here."
    l "All right, all right. I'll just put away my things and then get right on the case."
    y "That's the spirit!"
    l "Oh, by the way. Why are outsiders not allowed in?"
    y "Oh no, did the guards hassle you? I'm sorry!"
    y "Yeah, it's because of the time of year, with the stars and stuff. This week is the only week that certain rituals are possible."
    y "They don't let anyone in the mountain when it happens, except if they live or work in the village."
    l "How does that work? Don't people need to... go shopping or whatever?"
    y "Well, the shopping district here is pretty small."
    y "Only a few people actually live inside the gates anymore... Most of the townsfolk live in the lowlands, by the riverbed."
    y "I mean, my family stayed here because of the mines. And I came back to help them."
    y "Aside from us, there's the blacksmith {b}Chel{/b}, his apprentice {b}Shera{/b} - Oh, actually, she lives in the lowlands too. But she works here."
    y "There used to be one old farmer up here, but he passed away. His daughters {b}Moa{/b} and {b}Bia{/b} stayed, in the old farmhouse."
    y "There's a couple shopkeepers, {b}Sosi{/b}, {b}Old Heron{/b} and his wife {b}Lady Heron{/b}. And the doctor."
    y "Those are the only people who are here right now. Sorry, I should have warned you!"
    y "In a couple days the gates will reopen and you can go back into the village and talk to more people."
    l "It's fine, I'll just talk tomorrow with the people who are here."
    y "That would be great! Thank you!"
    y "And if you want to investigate the caves, you can... Maybe after the gates open up one of the miners could accompany you?"
    l "Yeah, we'll see."
    hide l
    hide y
    
    scene bg entry with dissolve
    pause 0.2
    scene bg path_manor with dissolve
    pause 0.2
    scene bg guest_cabin with dissolve
    
    l "I decided to turn in early. I woke up shortly after sunrise the next morning."
    
    jump guest_cabin

label meet_bia:
    
    b "Oh, hello. Namara's friend, I take it?"
    b "I'm Bia Heron. Pleased to meet you."
    $ met.append("bia")
    $ renpy.jump(area)

label meet_shera:
    
    s "Hello! I haven't seen you before! New in town?"
    l "No, I'm just here for a few days to help Namara with something."
    s "How mysterious! Well, anyway, I'm Shera. Nice to meet you!"
    $ met.append("shera")
    $ renpy.jump(area)

label meet_chel:
    
    c "Hey, Lani!"
    c "Oh, sorry if I caught you off guard! Namara told me you'd probably be stopping by. Nice to meet you!"
    $ met.append("chel")
    $ renpy.jump(area)
    
label meet_sosi:
    
    i "Oh, hello."
    i "I don't believe we've met... I'm Sosi. Can I help you find anything?"
    $ met.append("sosi")
    $ renpy.jump(area)

label meet_doctor:
    
    d "Hello!"
    d "Ah, you're not a local! That's okay. I'm the town's doctor."
    d "In case you need any first-aid supplies or anything, I sell those, too!"
    d "I hope you enjoy your stay in Ba Meniri!"
    $ met.append("doctor")
    $ renpy.jump(area)

label meet_heron:
    
    o "Ah, an out-of-towner."
    o "I wasn't aware we were having visitors! I'm Old Heron. Pleasure to meet you."
    $ met.append("heron")
    $ renpy.jump(area)

label meet_lady:
    
    h "Oh, hello, dear."
    h "It's nice to see a new face in town! I'm Lady Heron."
    $ met.append("lady")
    $ renpy.jump(area)

label ending_1:

    "Suddenly you hear a long, resonant scream from up the mountain!"
    "Along with a throng of villagers, you run up to the source of the noise."
    "It seems that the group is heading up to the cave."
    
    scene bg forest_path
    l "What happened?"
    c "There was so much blood..."
    l "Yeah, it looks like a body was dragged through here."
    l_int "He recoiled."
    c "I'm not going back in that cave. But you can look, Lani. Aren't you an investigator or something?"
    l "Not really. I mean, I can take a look, sure."
    c "Man, I wish Shera was still here. She could have taken you deeper into the cave, but she went home and they're definitely not gonna let her back in now."
    
    "Rollback to get a new ending."
    $ renpy.jump("ending_1")