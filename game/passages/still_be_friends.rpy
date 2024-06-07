# The script of the game goes in this file.

# PASSAGE NAME: "Do you think we can still be friends?"

label still_be_friends:

    $ options += 1

    "You can tell they aren't sure what the answer to this question is."

    "'Maybe.' Their eyes trail around the room, looking at everything except you."

    "They have no intention of being friends with you or even having contact with you. They don't want to see you ever again."

    "They're disgusted by the thought of even being around you."

    menu:
        "'Why not?'":
            jump why_not
        "Let them go":
            jump let_go