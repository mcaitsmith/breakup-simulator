﻿# The script of the game goes in this file.

# BRANCH: BEGGING

# PASSAGE NAME: Persist

label persist:

    $ options += 1

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = True
    $ attacking_bass_tubas_on = False
    $ feigning_bass_bass_choir_on = False
    $ attacking_accepting_avoiding_core_piano_lead_on = False
    $ attacking_accepting_avoiding_core_piano_rhythm_on = False
    $ entropy_core_marimba_rhythm_on = False
    $ entropy_core_xylophone_lead_on = False
    $ feigning_begging_core_harp_lead_on = True
    $ feigning_begging_core_harp_rhythm_on = True
    $ accepting_harmony_cellos_on = True
    $ accepting_harmony_violas_on = True
    $ accepting_harmony_violins_2_on = True
    $ attacking_harmony_french_horns_on = False
    $ attacking_harmony_trombones_on = False
    $ begging_harmony_bassoons_on = True
    $ begging_harmony_clarinets_on = True
    $ feigning_harmony_alto_choir_on = False
    $ feigning_harmony_tenor_choir_on = False
    $ accepting_melody_violins_1_on = False
    $ accepting_melody_trumpets_on = False
    $ begging_melody_flutes_on = True
    $ begging_melody_oboes_on = True
    $ feigning_melody_soprano_choir_on = False
    $ attacking_accepting_percussion_cymbals_on = False
    $ update_layers(5) # update layer(s)

    show bg livingroom with Dissolve(3.0):
        begging_tint

    "\"I don't want that!\""

    "That may have been the wrong option. Far far too desparate sounding to be worthy of love. Maybe you'll get it on the next go around?"

    "\"God! This is why I can't be around you! This is why we can't be friends!\""

    "As they shout this, they quickly stand up and move towards the door."

    "\"I can't see you anymore. Ever.\""

    $ leave_exp = "relieved"

    menu:
        "\"Wait, please, just talk to me.\"":
            jump helpless
        "\"Fine, I don't need you anyway.\"":
            jump helpless
        "\"Please stay. Please please stay.\"":
            jump helpless
        "\"FUCK YOU!\"":
            jump helpless
        "\"Don't say that don't say that please for the love of God don't say that.\"":
            jump helpless