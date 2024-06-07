# The script of the game goes in this file.

# PASSAGE NAME: "They'll never make you as happy as I did."

label make_you_happy:

    $ options += 1

    "'There isn't anyone, I told you.' They clench their fists and raise their voice. Whatever sentimentality was keeping them gentle towards you, it isn't endless. There is a limit. If you keep pushing this, you may regret it."

    "'I just don't see the point in being together anymore. We don't have much in common.'"

    menu:
        "Believe them":
            jump stay_silent
        "'What do you mean that we don't have anything in common? How did you randomly decide that now?'":
            jump push