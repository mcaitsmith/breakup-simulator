# The script of the game goes in this file.

# PASSAGE NAME: "Why not?

label why_not_friends:

    $ options += 1

    "'I'm afraid that if we stay friends we might...relapse.'"

    "What does that mean? 'Relapse'?"

    "They mean, if they continue to talk to you, they will effortlessly find their way back into your arms. They can't trust themselves to not want you." 

    "This is good. THIS is how you stay with them. You play the long game." 

    menu:
        "'I don't think that'll be an issue. We can be civil.'":
            jump civil
        "'You might be right.'":
            jump let_go