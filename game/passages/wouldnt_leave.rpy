# The script of the game goes in this file.

# PASSAGE NAME: "If you were sorry then you wouldn't leave."

label wouldnt_leave:

    $ options += 1

    pause(3.0)

    "\"Is that really what you'd prefer? You'd rather I stay even if I'm unhappy? Are you so afraid to be alone that you'd hold me prisoner?\""

    menu:
        "{color=#6a2ad8}\"Yes.\"{/color}" if ending == 8 and hint == True and entropy == 0:
            jump yes
        "\"Yes.\"" if (ending < 8 or hint == False or (ending == 8 and entropy == 1)):
            jump yes
        "\"No.\"":
            jump no