# The script of the game goes in this file.

label intro2:

    $ ending = 1
    $ options = 1

    "As the TV is abruptly muted, your partner slides a few inches away from you on the couch. Their eyes are glued to the floor, avoiding yours like the plague. When you reach to take their hand again, their arm reluctantly goes limp."

    "Finally, they say it:"

    "'I think we should break up.'"

    "Somewhere in the world, a semi-truck merges into the next lane without looking, causing a six car collision."

    menu:
        "'Why?'":
            jump intro3
        "Stay silent":
            jump intro3