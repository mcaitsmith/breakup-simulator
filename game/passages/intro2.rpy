# The script of the game goes in this file.

# PASSAGE NAME: Intro part 2

label intro2:

    $ ending = 1
    $ options = 1

    window hide
    show ex neutral with Dissolve(3.0)

    "As the TV is abruptly muted, your partner slides a few inches away from you on the couch. Their eyes are glued to the floor, avoiding yours like the plague. When you reach to take their hand again, their arm reluctantly goes limp."

    "Finally, they say it:"

    show bg livingroom with { "master" : Dissolve(3.0) }:
        entropy_tint

    "{cps=15}\"I think we should break up.\"{/cps}"

    window hide
    pause 3.0

    "Somewhere in the world, a semi-truck merges into the next lane without looking, causing a six car collision."

    pause 2.0

    menu:
        "\"Why?\"":
            jump intro3
        "Stay silent":
            jump intro3