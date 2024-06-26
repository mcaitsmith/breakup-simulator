﻿# The script of the game goes in this file.

# BRANCH: ATTACKING

# PASSAGE NAME: "There's someone else isn't there?"

label someone_else:

    $ options += 1

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = False
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
    $ attacking_harmony_french_horns_on = True
    $ attacking_harmony_trombones_on = True
    $ begging_harmony_bassoons_on = False
    $ begging_harmony_clarinets_on = False
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
        attacking_tint
    window hide
    show ex frustrated with Dissolve(3.0)

    "\"No. There isn't.\""

    "They're lying to you. I've never been more certain. Infidelity. Betrayal. Make them admit there is someone else and prove that you're superior to them. You can stop this breakup."

    menu:
        "\"They'll never make you as happy as I did.\"":
            jump make_you_happy
        "\"Stop lying. Tell me who it is.\"":
            jump make_you_happy
        "Stay silent.":
            jump stay_silent