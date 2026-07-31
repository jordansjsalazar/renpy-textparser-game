label waterfall_1:

    y "Bia."
    b "Oh! I was starting to get worried you wouldn't come."

label storage_1:

    b "Oh, you're here."
    m "Is this why you keep disappearing into the woods? You're courting him behind my back?"
    b "And so what if I am?"
    m "You know you'll never have him! I already took Young Namara's hand in marriage!"

label ending_1:
    "Suddenly you hear a long, resonant scream from up the mountain!"
    "Along with a throng of villagers, you run up to the source of the noise."
    "It seems that the group is heading up to the cave."
    
    scene bg cave
    l "What happened?"
    c "There was so much blood..."
    
    
    "Rollback to get a new ending."
    $ renpy.jump("ending_1")