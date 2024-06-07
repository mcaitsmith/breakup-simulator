# The script of the game goes in this file.

# PASSAGE NAME: "I don't think that'll be an issue. We can be civil."

label civil:

    $ options += 1

    "'No,' they say resolutely. 'It's not about 'being civil'. I don't think my life can move forward with you in it.'"

    menu:
        "'Please try. I don't want to live without you.'":
            jump persist
        "'If you know that we'll end up together, then why fight that?'":
            jump persist
        "'Whatever.'":
            jump let_go