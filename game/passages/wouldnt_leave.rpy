# The script of the game goes in this file.

# PASSAGE NAME: "If you were sorry then you wouldn't leave."

label wouldnt_leave:

    $ options += 1

    "'Is that really what you'd prefer? You'd rather I stay even if I'm unhappy? Are you so afraid to be alone that you'd hold me prisoner?'"

    menu:
        "'Yes.'":
            jump yes
        "'No.'":
            jump no