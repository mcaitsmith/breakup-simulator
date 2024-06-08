# The script of the game goes in this file.

# PASSAGE NAME: Keep going

label keep_going:

    $ options += 1

    "In a moment of glorious precision, you assemble a verbal dronestrike comprised of every insecurity, every fear, every vulnerability, and you unleash it upon them in a single sentence." 

    "As they hear you say it, your ex becomes nearly catatonic."

    "The two of you sit in silence."

    nvl clear
    pause 5.0

    "You aren't sure anymore if what you did here was right, but you did what felt necessary in the moment." 

    nvl clear
    pause 10.0

    menu:
        "And yet.":
            jump helpless