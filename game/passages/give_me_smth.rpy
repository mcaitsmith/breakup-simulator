# The script of the game goes in this file.

# PASSAGE NAME: "Please just say maybe. Give me something."

label give_me_smth:

    $ options += 1

    "'That wouldn't be fair to you. We have to leave it at 'no' for now.'"

    "Fair to you?! This whole thing has been unfair to you. Pulling the rug out from under you was unfair. They want to talk about 'fair'? Bullshit."

    menu:
        "'Fine.'":
            jump let_go
        "'Fuck you.'":
            jump let_go