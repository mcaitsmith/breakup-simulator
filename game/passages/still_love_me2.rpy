# The script of the game goes in this file.

# PASSAGE NAME: "You still love me."

label still_love_me2:

    $ options += 1

    "'I still love you. The feeling is still there, but I don't feel like I belong with you anymore. I don't feel like we have anything in common anymore.'"

    menu:
        "'How could we not have anything in common? That doesn't make any sense!'":
            jump arent_telling_me
        "'This is normal for a healthy relationship! Attraction is meant to ebb and flow!'":
            jump attraction
        "Reluctantly accept what they're saying to you as truth.":
            jump stay_silent