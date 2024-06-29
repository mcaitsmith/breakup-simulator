# The script of the game goes in this file.

# PASSAGE NAME: "Yes."

label yes:

    $ options += 1

    window hide
    show ex frustrated with Dissolve(3.0)

    "\"Then I don't know who the fuck you are...And this isn't a relationship anymore, it's a hostage situation.\""

    menu:
        "{color=#6a2ad8}\"Just tell me what it will take to make you love me.\"{/color}" if ending == 8 and hint == True and entropy == 0:
            jump make_you_love_me
        "\"Just tell me what it will take to make you love me.\"" if (ending < 8 or hint == False or (ending == 8 and entropy == 1)):
            jump make_you_love_me
        "\"No it isn't, we're in love.\"":
            jump let_go
        "Let them go":
            jump let_go