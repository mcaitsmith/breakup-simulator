# The script of the game goes in this file.

# PASSAGE NAME: "Throwing me away won't fix your life. You don't have to be alone."

label throwing_me_away:

    $ options += 1

    "'I'm not throwing you away.'" 

    "You notice their hands shaking." 

    "What's this?" 

    "Guilt? Shame? An opening in their armor?"

    menu:
        "'Yes you are.'":
            jump yes_you_are
        "'Whatever.'":
            jump stay_silent
        "'Do you think we can still be friends?'":
            jump still_be_friends