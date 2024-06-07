# The script of the game goes in this file.

# PASSAGE NAME: "You aren't telling me something"

label arent_telling_me:

    $ options += 1

    "They sigh."

    "'I wish it was something we could fix together,' they say. 'If it was, I promise I would stay here with you and fight to keep what we have, but it isn't. There isn't a future for us and that's that.'"

    "Your stomach is in knots. 'that's that' they insist." 
    "You look over at the TV, still frozen in place. 'One episode to go' the screen says at the top."

    menu:
        "Stay silent.":
            jump stay_silent
        "They're abandoning you":
            jump stay_silent
        "The whole relationship was a farce":
            jump stay_silent
        "'Fuck you.'" if options >= 15:
            jump f_you