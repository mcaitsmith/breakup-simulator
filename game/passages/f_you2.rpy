# The script of the game goes in this file.

# PASSAGE NAME: "No, seriously, fuck you."

label f_you2:

    $ options += 1

    "Your (now ex) partner begins to cry. If your goal was to do more damage to them than they can do to you, this is your opportunity."

    "Otherwise, I'd wager you've made your point."

    menu:
        "Go in on them. Mention every terrible thing they ever did. Utilize every weakness they ever showed to make them regret crossing you.":
            jump toxic
        "Say nothing more.":
            jump stay_silent