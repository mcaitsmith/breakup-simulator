﻿# The script of the game goes in this file.

# PASSAGE NAME: Just tell me what it will take to make you love me.

label make_you_love_me:

    pause(3.0)

    "\"I won't,\" they say plainly. Their face goes blank, looking completely different from the way you remember it."

    "You can relive this memory as many times as you like, imagine all the different things you want to say, imagine all the things I might have said in response, but it doesn't change reality. I left. You didn't do anything wrong, you didn't miss any important cues, I just left because I felt like it. There was nothing you could do." 

    "Why do you keep torturing yourself like this? Are you hoping you'll learn an important lesson, playing out scenario after scenario, hoping to find the key to stopping this from ever happening again?" 

    menu:
        "{color=#6a2ad8}Yes.{/color}" if ending == 8 and hint == True and entropy == 0:
            jump yes_learn
        "Yes." if (ending < 8 or hint == False or (ending == 8 and entropy == 1)):
            jump yes_learn