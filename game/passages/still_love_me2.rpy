﻿# The script of the game goes in this file.

# BRANCH: BEGGING

# PASSAGE NAME: "You still love me."

label still_love_me2:

    $ options += 1

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = True
    $ attacking_bass_tubas_on = False
    $ feigning_bass_bass_choir_on = False
    $ attacking_accepting_avoiding_core_piano_lead_on = False
    $ attacking_accepting_avoiding_core_piano_rhythm_on = True
    $ entropy_core_marimba_rhythm_on = False
    $ entropy_core_xylophone_lead_on = False
    $ feigning_begging_core_harp_lead_on = True
    $ feigning_begging_core_harp_rhythm_on = False
    $ accepting_harmony_cellos_on = False
    $ accepting_harmony_violas_on = False
    $ accepting_harmony_violins_2_on = False
    $ attacking_harmony_french_horns_on = False
    $ attacking_harmony_trombones_on = False
    $ begging_harmony_bassoons_on = True
    $ begging_harmony_clarinets_on = True
    $ feigning_harmony_alto_choir_on = False
    $ feigning_harmony_tenor_choir_on = False
    $ accepting_melody_violins_1_on = False
    $ accepting_melody_trumpets_on = False
    $ begging_melody_flutes_on = False
    $ begging_melody_oboes_on = False
    $ feigning_melody_soprano_choir_on = False
    $ attacking_accepting_percussion_cymbals_on = False
    $ update_layers(5) # update layer(s)

    show bg livingroom with { "master" : Dissolve(3.0) }:
        begging_tint
    window hide
    show ex neutral with Dissolve(3.0)

    "\"I still love you. The feeling is still there, but I don't feel like I belong with you anymore. I don't feel like we have anything in common anymore.\""

    menu:
        "\"How could we not have anything in common? That doesn't make any sense!\"":
            jump arent_telling_me
        "{color=#59ba73}\"This is normal for a healthy relationship! Attraction is meant to ebb and flow!\"{/color}" if ending == 8 and hint == True and entropy == 1:
            jump attraction
        "\"This is normal for a healthy relationship! Attraction is meant to ebb and flow!\"" if ending < 8 or hint == False or (ending == 8 and entropy == 0):
            jump attraction
        "Reluctantly accept what they're saying to you as truth.":
            jump stay_silent