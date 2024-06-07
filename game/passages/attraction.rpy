# The script of the game goes in this file.

# PASSAGE NAME: Attraction

label attraction:

    $ options += 1

    "Have you not made your way around the dialogue tree enough to understand yet?"

    menu:
        "Understand what?":
            jump understand_what
        "I think so.":
            jump understand_what