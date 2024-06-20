# The script of the game goes in this file.

# BRANCH: PASSIVE

# PASSAGE NAME: "No."

label no_key:

    $ options += 1

    "'Fine.' As they stand up to leave they drop your key on the floor. 'I won't be held hostage.' They say something ugly under their breath as they leave."

    "No. You can hold them here if you try. Just try harder."

    menu:
        "'Wait. Don't go.'":
            jump helpless