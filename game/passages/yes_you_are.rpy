# The script of the game goes in this file.

# PASSAGE NAME: "Yes you are."

label yes_you_are:

    $ options += 1

    "They choke on their own words for a second." 

    "\"I don't mean to hurt you. I'm sorry, I really am.\""

    "You found it: an opening." 

    menu:
        "\"If you were sorry then you wouldn't leave.\"":
            jump wouldnt_leave
        "Back off.":
            jump stay_silent