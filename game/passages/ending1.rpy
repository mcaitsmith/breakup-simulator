# The script of the game goes in this file.

# PASSAGE NAME: the silence they've left behind.

label ending1:

    $ ending = 2

    nvl clear
    pause 5.0

    "You know it's your fault, right?"

    nvl clear
    pause 10.0

    "There was a way to make them stay."

    nvl clear
    pause 15.0

    "You just need to find the right thing to say that will make them love you again." 

    nvl clear
    pause 20.0

    "Go back. Try again."

    nvl clear
    pause 23.0

    "Get it right this time."

    menu:
        "Try again.":
            jump intro3