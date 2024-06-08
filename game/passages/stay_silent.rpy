# The script of the game goes in this file.

# PASSAGE NAME: Stay silent.

label stay_silent:

    $ options += 1

    "'I can't tell you how sorry I really am. You mean so much to me, and the time we've spent together has meant the world. But I think this is what's best for both of us.'" 

    "No matter how they try to sugarcoat their words, they continue to feel like daggers."

    "They reach into their pocket and hand you the spare key to your apartment. You remember having spare keys made over a year ago. You were together on a trip to the hardware store and saw the key copying machine by the checkout line. It was a sweet spur of the moment gesture that demonstrated the trust they had in you. You could go to their place and they could come to yours. It meant your lives were truly becoming enmeshed." 

    menu:
        "Give them the key to their apartment":
            jump key
        "Start begging":
            jump beg