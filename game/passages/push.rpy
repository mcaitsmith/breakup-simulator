# The script of the game goes in this file.

# PASSAGE NAME: push

label push:

    $ options += 1

    "'It wasn't 'random', I've felt this way for a while now.'" 

    "Bullshit. This is all some sadistic game to them. Good people don't just throw other people away so flippantly." 

    menu:
        "'Fuck you.'":
            jump f_you
        "Stop pushing this.":
            jump stay_silent