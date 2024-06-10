# The script of the game goes in this file.

# PASSAGE NAME: You're helpless to stop it.

label helpless:

    $ options += 1

    "As they leave the apartment, it's just you and" 

    menu:
        "the silence they've left behind." if ending == 1:
            jump ending1
        "the silence they've left behind." if ending == 2:
            jump ending2
        "the silence they've left behind." if ending == 3:
            jump ending3
        "the silence they've left behind." if ending == 4:
            jump ending4
        "the silence they've left behind." if ending == 5:
            jump ending5
        "the silence they've left behind." if ending == 6:
            jump ending6
        "the silence they've left behind." if ending == 7:
            jump ending7
        "the silence they've left behind." if ending == 8:
            jump ending8