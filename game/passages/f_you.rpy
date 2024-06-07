# The script of the game goes in this file.

# PASSAGE NAME: "Fuck you."

label f_you:

    $ options += 1

    "The words surprise you as they pass your lips. Each syllable is like a stone being hurled at your partner. How dare they do this to you?"

    "If you're clever, you can deal as much damage to them as they've dealt to you. Maybe then they'll see how horrible what they're doing is and change their mind."

    "'Look, I-I know I'm blindsiding you here, I know this is shitty, but can we try to at least be mature adults?'"

    menu:
        "'No, seriously, fuck you.'":
            jump f_you2
        "'Sorry, I don't know what came over me.'":
            jump sorry