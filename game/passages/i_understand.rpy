# The script of the game goes in this file.

# PASSAGE NAME: "I understand."

label i_understand:

    $ options += 1

    "'Y-you do?' They seem surprised and a bit relieved. It seems clear that they don't want to hurt you. But at the same time it seems like they're not sacrificing any more of their happiness to protect your feelings."

    "You could say that's cruel."

    "You could say it's even more cruel to let you live a lie, thinking you had a partner who was happy when you don't." 

    "Either way, it's all over now. It was over a while ago. You're just getting the memo now. Better now than in a year." 

    "Or ten years." 

    menu:
        "'I guess.'":
            jump stay_silent
        "'It's better this way.'":
            jump better_this_way