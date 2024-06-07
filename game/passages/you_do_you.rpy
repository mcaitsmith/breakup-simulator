# The script of the game goes in this file.

# PASSAGE NAME: "Yeah, it's fine. You do you."

label you_do_you:

    $ options += 1

    "'Y-you're cool with us breaking up?...That's great, actually. I was worried this would be a whole dragged out thing.'"

    menu:
        "'Oh, not at all. Honestly, you deserve better.'":
            jump deserve_better
        "'Oh, not at all. Honestly, I deserve better.'":
            jump deserve_better