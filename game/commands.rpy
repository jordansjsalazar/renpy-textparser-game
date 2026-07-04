label use_fail:
    "Use what?"
    $ renpy.jump(last_label)

label interact_fail:
    "Do what with what?"
    $ renpy.jump(last_label)

label enter_fail:
    "Go where?"
    $ renpy.jump(last_label)

label fail:
    "Sorry, that command didn't register. You can type cmd for a list of commands."
    $ renpy.jump(last_label)