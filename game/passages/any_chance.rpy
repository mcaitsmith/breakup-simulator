# The script of the game goes in this file.

# PASSAGE NAME: "Do you think there's any chance of us...being together again?"

label any_chance:

    $ options += 1

    "'I don't want to make any promises. Maybe.' They clench their fists. 'No. The answer has to be no.'"

    menu:
        "'Please just say maybe. Give me something.'":
            jump give_me_smth
        "'Make up your mind.'":
            jump make_up_mind