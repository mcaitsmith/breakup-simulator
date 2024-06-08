# The script of the game goes in this file.

# PASSAGE NAME: Understand what?

label understand_what:

    $ options += 1

    "'You're not the problem here.'" 

    "Impossible. If that were true you wouldn't be stuck here. You'd be somewhere else."

    "'What I am...I can't do what you want me to do. It isn't in my nature.'"

    menu:
        "What are you?":
            jump what_are_you
        "You're Entropy" if entropy == 1:
            jump entropy