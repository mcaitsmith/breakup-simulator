# The script of the game goes in this file.

# PASSAGE NAME: say no

label no:

    window hide
    show ex neutral with Dissolve(3.0)

    "\"Then you have to let me go.\""

    menu:
        "Let them go":
            jump let_go