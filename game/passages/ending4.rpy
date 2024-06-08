# The script of the game goes in this file.

# PASSAGE NAME: ending 4

label ending4:

    $ ending = 5

    nvl clear
    pause 5.0

    "You were close that time."

    nvl clear
    pause 10.0

    "Did they seem angry? Sad? Nostalgic? Did they say anything about me?"

    nvl clear
    pause 15.0

    "Play harder into those feelings. Press as many buttons as you can." 

    nvl clear
    pause 20.0

    "If you try hard enough you can keep them forever."

    nvl clear
    pause 23.0

    "Everything will be perfect."

    menu:
        "Forever...":
            jump intro3