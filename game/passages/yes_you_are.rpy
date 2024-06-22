# The script of the game goes in this file.

# PASSAGE NAME: "Yes you are."

label yes_you_are:

    $ options += 1

    pause(3.0)

    "They choke on their own words for a second." 

    "\"I don't mean to hurt you. I'm sorry, I really am.\""

    "You found it: an opening." 

    menu:
        "{color=#6a2ad8}\"If you were sorry then you wouldn't leave.\"{/color}" if ending == 8 and hint == True and entropy == 0:
            jump wouldnt_leave
        "\"If you were sorry then you wouldn't leave.\"" if (ending < 8 or hint == False or (ending == 8 and entropy == 1)):
            jump wouldnt_leave
        "Back off.":
            jump stay_silent