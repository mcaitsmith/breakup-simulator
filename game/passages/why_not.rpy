# The script of the game goes in this file.

# PASSAGE NAME: "Why not?"

label why_not:

    $ options += 1

    "'I-I don't know. Believe me, I've been trying really hard to make things work between us. But when I try to imagine my future, and I picture you there, it just doesn't feel right.'"

    "You recall having the same experience, imagining your future together, except you couldn't imagine your future WITHOUT them. To hear that they couldn't imagine it WITH you..."

    "This is not the same person you've loved for the past two years. Something has changed. There has to have been something."

    menu:
        "'Did I do something wrong?'":
            jump smth_wrong
        "'I understand.'" if options >= 20:
            jump i_understand
        "Stay silent.":
            jump stay_silent