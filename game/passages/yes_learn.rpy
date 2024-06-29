# The script of the game goes in this file.

# PASSAGE NAME: Yes.

label yes_learn:

    pause(3.0)

    "You can't. Nothing you can do in a sea of infinite choices will prevent the inevitability that eventually everyone drifts apart. Claw at people all you want, sink your teeth into them like the animal starved for love that you are, it changes nothing. Whether it's from a slow loss of communication, a sudden termination of a relationship, or an unexpected death, eventually there will only be you and I."

    menu:
        "{color=#6a2ad8}Who are you?{/color}" if ending == 8 and hint == True and entropy == 0:
            jump who_are_you
        "Who are you?" if (ending < 8 or hint == False or (ending == 8 and entropy == 1)):
            jump who_are_you