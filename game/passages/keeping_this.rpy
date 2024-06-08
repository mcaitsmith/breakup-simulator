# The script of the game goes in this file.

# PASSAGE NAME: No. I'm keeping this.

label keeping_this:

    $ options += 1

    "Your ex looks at you with a twinge of frustration." 

    "'Please. Can I have my key back?'"

    menu:
        "Give up.":
            jump give_up
        "Refuse to give up.":
            jump refuse