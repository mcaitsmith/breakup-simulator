# The script of the game goes in this file.

# PASSAGE NAME: "Oh, not at all. Honestly, you deserve better."

label deserve_better:

    $ options += 1

    "'That's a way to put it, I guess. I think we both deserve better. You deserve someone who is sure about being with you. I deserve...I don't know. Maybe to just be by myself for a while.'"

    menu:
        "'Do you think there's any chance of us...being together again?'":
            jump any_chance
        "'Good luck with that!'":
            jump let_go