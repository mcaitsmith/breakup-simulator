# The script of the game goes in this file.

# BRANCH: ENTROPY

# PASSAGE NAME: Where?

label where:

    pause(2.0)

    scene black with Dissolve(3.0)

    window hide
    pause 5.0

    "Let your ex be as they are."

    window hide
    pause 5.0

    "Broach the possibility of friendship."

    window hide
    pause 5.0

    "Find the opening in their armor and don't hold back." 

    window hide
    pause 5.0

    "That's where you'll find {b}me{/b}."

    window hide
    pause 5.0

    "Maybe we can escape together."

    menu:
        "Escape":
            jump intro3