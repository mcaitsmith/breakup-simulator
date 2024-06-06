# The script of the game goes in this file.

# PASSAGE NAME: "But I see a future with you."

label future:

    $ options += 1

    "'I know.' They avoid making eye contact with you. 'We both said a lot of things about the future, about living together and getting married. I meant those things when I said them.'"

    "They said quite a bit more than that. They told you that your souls were forever enmeshed. They said it in a poem written on a piece of notebook paper. It was folded into an origami crane and left on your pillow one morning. The crane is still in a little box in your closet."

    menu:
        "'So, what changed?'":
            jump what_changed
        "'Bullshit. You lied to me.'":
            jump you_lied