# The script of the game goes in this file.

# PASSAGE NAME: "Okay! No Problem!"

label okay:

    $ options += 1

    "'W-what?' They seem a bit caught off guard by your response." 

    "As am I. What are you doing? Is this reverse psychology?"

    menu:
        "'Yeah, it's fine. You do you.'":
            jump you_do_you
        "'I was getting sort of bored with you too anyway!'":
            jump you_do_you