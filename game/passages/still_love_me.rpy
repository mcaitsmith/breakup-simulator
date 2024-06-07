# The script of the game goes in this file.

# PASSAGE NAME: "Do you still love me?"

label still_love_me:

    $ options += 1

    "'Yes.' They say this quickly, then just as quickly mutter, 'I don't know.'"

    menu:
        "'You still love me.'":
            jump still_love_me2
        "'How can you not know?'":
            jump still_love_me2