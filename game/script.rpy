# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(kind=nvl)

# define location images
# image bg main = "backgrounds/bg office.png"
# image bg office blur = im.Blur("backgrounds/bg office.png", 1.5) # blurred version

# image policelights:
#     "#f00"
#     alpha 0.0
#     linear .45 alpha 0.2    
#     linear .45 alpha 0.0
#     "#00f"
#     alpha 0.0
#     linear .45 alpha 0.2    
#     linear .45 alpha 0.0
#     repeat

# define sound effects & music
# define sfx_clatter = "audio/sfx/Clatter_SantaSecret_SFX.wav"
define bg_music = "audio/V1_Saying_Goodbye.ogg"

# The game starts here.

label start:

    $ options = 0
    $ entropy = 0
    $ ending = 0

    play music bg_music

    jump intro