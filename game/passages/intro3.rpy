# The script of the game goes in this file.

# PASSAGE NAME: Intro part 3

label intro3:

    if ending >= 2:

        scene bg livingroom with Dissolve(3.0)

        "You blink and suddenly they're here again. You've been given another chance to get it right this time."

    "'I've been thinking for a while and...' Their voice trails off. They're clearly trying to find the words to soften the blow. But the more they search, the less it seems like they can find them. Something changes in their face. You assume this means they're accepting their role. They have no choice but to hurt you."

    "'I don't see a future with you.'" 

    "And there it is. You never saw it coming. Not in a million years. But there it is anyway."

    menu:
        "'What changed?'":
            jump why_not
        "'Did I do something wrong?'":
            jump smth_wrong
        "'Okay! No Problem!'" if options >= 10:
            jump okay
        "'But I see a future with you.'" if options >= 5:
            jump future
        "'Fuck you.'" if options >= 15:
            jump f_you
        "Stay silent." if options >= 5:
            jump stay_silent
        "'I understand.'" if options >= 20:
            jump i_understand