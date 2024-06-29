# The script of the game goes in this file.

# BRANCH: PASSIVE

# PASSAGE NAME: "No."

label no_key:

    $ options += 1

    show bg livingroom with { "master" : Dissolve(3.0) }:
        passive_tint
    window hide
    show ex frustrated with Dissolve(3.0)

    "\"Fine.\" As they stand up to leave they drop your key on the floor. \"I won't be held hostage.\" They say something ugly under their breath as they leave."

    "No. You can hold them here if you try. Just try harder."

    menu:
        "\"Wait. Don't go.\"":
            jump helpless