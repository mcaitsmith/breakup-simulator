# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(kind=nvl)

define bg_music = "audio/V1_Saying_Goodbye.ogg"

# The game starts here.

label start:

    $ options = 0
    $ entropy = 0
    $ ending = 0

    play music bg_music

    jump intro