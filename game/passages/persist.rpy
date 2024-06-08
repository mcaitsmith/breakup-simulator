# The script of the game goes in this file.

# PASSAGE NAME: Persist

label persist:

    $ options += 1

    "'I don't want that!'"

    "That may have been the wrong option. Far far too desparate sounding to be worthy of love. Maybe you'll get it on the next go around?"

    "'God! This is why I can't be around you! This is why we can't be friends!'"

    "As they shout this, they quickly stand up and move towards the door."

    "'I can't see you anymore. Ever.'"

    menu:
        "'Wait, please, just talk to me.'":
            jump helpless
        "'Fine, I don't need you anyway.'":
            jump helpless
        "'Please stay. Please please stay.'":
            jump helpless
        "'FUCK YOU!'":
            jump helpless
        "'Don't say that don't say that please for the love of God don't say that.'":
            jump helpless