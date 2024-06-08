# The script of the game goes in this file.

# PASSAGE NAME: ending 2

label ending2:

    $ ending = 3

    nvl clear
    pause 5.0

    "You did it wrong."

    nvl clear
    pause 10.0

    "I don't know what it was that you said, but somewhere in there you said the wrong thing."

    nvl clear
    pause 15.0

    "If you lose them, you will die alone and you will deserve it." 

    nvl clear
    pause 20.0

    "Go back. Find the correct path."

    nvl clear
    pause 23.0

    "You CAN make them stay."

    menu:
        "Go back.":
            jump intro3