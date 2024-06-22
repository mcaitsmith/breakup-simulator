# The script of the game goes in this file.

# PASSAGE NAME: "Make up your mind."

label make_up_mind:

    $ options += 1

    pause(3.0)

    "\"I wish I could, believe me. There are so many things in my life that I am constantly uncertain about. My job isn't going anywhere, I don't have any friends, it  feels like I'm going nowhere. I need to be alone for a while, figure out what I want, that much I know.\""

    "You detect uncertainty in their voice. Part of them suspects that they will live to regret this decision, at least you surmise from their tone. They could be swayed if you're clever."

    menu:
        "{color=#6a2ad8}\"Throwing me away won't fix your life. You don't have to be alone.\"{/color}" if ending == 8 and hint == True and entropy == 0:
            jump throwing_me_away
        "\"Throwing me away won't fix your life. You don't have to be alone.\"" if (ending < 8 or hint == False or (ending == 8 and entropy == 1)):
            jump throwing_me_away
        "\"If that's what you want.\"":
            jump stay_silent