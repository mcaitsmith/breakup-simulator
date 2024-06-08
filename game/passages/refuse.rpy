# The script of the game goes in this file.

# PASSAGE NAME: Refuse to give up.

label refuse:

    $ options += 1

    "You realize that as long as this key is in your hand they won't leave. You can hold on forever. You can keep them prisoner in this moment in time forever."

    "'You're making this so much harder than it needs to be. Please, just give me the key.'"

    menu:
        "Give up the key":
            jump give_up
        "'No.'":
            jump no_key