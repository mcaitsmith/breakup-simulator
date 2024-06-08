# The script of the game goes in this file.

# PASSAGE NAME: Beg

label beg:

    $ options += 1

    "You start pleading with them to stay. You offer change, growth, even the possibility that they don't need to spend the 'future' with you, just a few more months. A few more weeks. Just one more day. They can have anything as long as they stay."

    "'Please don't make this difficult,' they say. 'Just let me go.'"

    "There's a million more things you want to say, but as you try, the words are stopped by the fear that anything you say will just make your situation worse." 

    "You look down and see that you're handing the key to them." 

    "You have no choice. You have to let them go."

    menu:
        "Let them go":
            jump let_go
        "'Do you think we can still be friends?'" if options >= 10:
            jump still_be_friends