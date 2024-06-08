# The script of the game goes in this file.

# PASSAGE NAME: Key

label key:

    $ options += 1

    "You reach into your pocket and get your keychain. You twirl the keys around and remove the matching spare key to their apartment." 

    "At one point in the past you had a pretty nasty fight. After saying your apologies, you handed them this key and said 'give this back to me when I've earned it.'" 

    "They ended up giving you the key back after a few hours."

    "They hold out their palm. If you give up this key you'll never be able to enter that place again. It'll be closed off from you forever. Never to open again."

    "You have to give up the key."

    menu:
        "Give up the key":
            jump give_up
        "No. I'm keeping this.":
            jump keeping_this