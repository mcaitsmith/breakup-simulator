# The script of the game goes in this file.

# PASSAGE NAME: "Yes."

label yes:

    $ options += 1

    "\"Then I don't know who the fuck you are...And this isn't a relationship anymore, it's a hostage situation.\""

    menu:
        "\"Just tell me what it will take to make you love me.\"":
            jump make_you_love_me
        "\"No it isn't, we're in love.\"":
            jump let_go
        "Let them go":
            jump let_go