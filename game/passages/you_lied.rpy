# The script of the game goes in this file.

# PASSAGE NAME: "Bullshit. You lied to me."

label you_lied:

    $ options += 1

    "'I really didn't.'" 

    "But they did. They never cared about you. All that time they stole from you was just a way of biding their time until someone better came along. That's got to be it."

    menu:
        "'There's someone else isn't there?'":
            jump someone_else
        "Stay silent.":
            jump stay_silent