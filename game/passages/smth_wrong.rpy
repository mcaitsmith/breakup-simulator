# The script of the game goes in this file.

# PASSAGE NAME: "Did I do something wrong?"

label smth_wrong:

    $ options += 1

    "'No. No, you haven't done anything wrong. I swear, if you had, I would've told you. I want to make sure you know that there wasn't anything you could've done differently.' Their voice is shaking as they say this."

    "You can't tell if this is the truth or a fabrication to get themselves out of the situation as quickly as possible. The partner you knew would never do something like this, but the partner you knew would never leave in the first place. Clearly this is someone...else."

    "Even though they say that you didn't do anything wrong, you can't help but imagine all the times you were short with them. You picture every time you got annoyed with them, every eye roll, every 'I think I need some space today' that you requested. In doing so, you doubt that they're telling the truth. Somewhere along the way, you did something that made them lose faith in you."

    "In other words, it's your fault, but maybe that faith can be restored?"

    menu:
        "I don't know who you are anymore.":
            jump arent_telling_me
        "You aren't telling me something.":
            jump arent_telling_me
        "I can win them back.":
            jump stay_silent
        "It is what it is.":
            jump stay_silent