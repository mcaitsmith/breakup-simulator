# The script of the game goes in this file.

# PASSAGE NAME: "It's better this way."

label better_this_way:

    $ options += 1

    "'I'm really glad to hear you say that.'" 

    "They take your hand and squeeze it tightly." 

    "'Believe me when I say this was the hardest thing I've ever had to do.'"

    "Do you actually understand or is this just another ploy to make them change their mind?"

    menu:
        "I mean it.":
            jump i_mean_it
        "I'm still holding on to hope.":
            jump you_do_you