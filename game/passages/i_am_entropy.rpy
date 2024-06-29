# The script of the game goes in this file.

# BRANCH: ENTROPY

# PASSAGE NAME: I am Entropy.

label i_am_entropy:

    pause(2.0)

    scene black with Dissolve(3.0)

    window hide
    pause 5.0

    "{color=#6a2ad8}You saw a future with them.{/color}"

    window hide
    pause 5.0

    "{color=#6a2ad8}Then something changed.{/color}"

    window hide
    pause 5.0

    "{color=#6a2ad8}They still love you.{/color}" 

    window hide
    pause 5.0

    "{color=#6a2ad8}But not even love is immune to {b}entropy{/b}.{/color}"

    window hide
    pause 5.0

    "{color=#6a2ad8}I'm so glad we get to share the pain together.{/color}"

    menu:
        "{color=#6a2ad8}Share the pain.{/color}":
            jump intro3