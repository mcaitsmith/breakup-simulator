# The script of the game goes in this file.

# PASSAGE NAME: Who are you?

label who_are_you:

    pause(3.0)

    "The silence of a room with nobody in it." 

    "The invisible force pulling galaxies apart from each other and towards the cold darkness of space."
    
    window hide
    pause 3.0

    "I am Entropy."

    "You've always known me. I was with you before birth and I'll reclaim you when your time comes." 

    window hide
    pause 3.0

    "I am Entropy."

    window hide
    pause 3.0

    "This place is just a playground for you to ping around, toy with, and ultimately hide from the world." 

    window hide
    pause 3.0

    menu:
        "{color=#6a2ad8}I am Entropy.{/color}" if ending == 8 and hint == True and entropy == 0:
            $ entropy = 1
            jump helpless
        "I am Entropy." if (ending < 8 or hint == False or (ending == 8 and entropy == 1)):
            $ entropy = 1
            jump helpless