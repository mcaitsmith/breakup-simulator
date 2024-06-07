# The script of the game goes in this file.

# PASSAGE NAME: "There's someone else isn't there?"

label someone_else:

    $ options += 1

    "'No. There isn't.'"

    "They're lying to you. I've never been more certain. Infidelity. Betrayal. Make them admit there is someone else and prove that you're superior to them. You can stop this breakup."

    menu:
        "'They'll never make you as happy as I did.'":
            jump make_you_happy
        "'Stop lying. Tell me who it is.'":
            jump make_you_happy
        "Stay silent.":
            jump stay_silent