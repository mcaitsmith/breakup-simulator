# The script of the game goes in this file.

# PASSAGE NAME: "So, what changed?"

label what_changed:

    $ options += 1

    "'I don't know. Nothing. Everything.'" 

    "A vague response." 

    "'There was a moment where I loved you and then there was a moment where I didn't. I don't know what triggered the switch. It could've been nothing at all. That happens to people sometimes.'"

    "'Nothing at all'? Can people just stop loving you overnight? They go to bed with a full heart and wake up with an empty one?"

    "Perhaps the answer to this question exists elsewhere."

    menu:
        "'Do you still love me?'":
            jump still_love_me
        "'What the hell does that even mean?!'":
            jump still_love_me2
        "'Don't spare my feelings. Just say if you still love me.'":
            jump still_love_me