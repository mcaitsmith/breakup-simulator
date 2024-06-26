﻿# The script of the game goes in this file.

# BRANCH: ENTROPY

# PASSAGE NAME: What are you?

label what_are_you:

    $ options += 1

    $ entropy_accent_glockenspiel_on = True
    $ entropy_accent_tubular_bells_on = True
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = False
    $ attacking_bass_tubas_on = False
    $ feigning_bass_bass_choir_on = False
    $ attacking_accepting_avoiding_core_piano_lead_on = False
    $ attacking_accepting_avoiding_core_piano_rhythm_on = False
    $ entropy_core_marimba_rhythm_on = True
    $ entropy_core_xylophone_lead_on = True
    $ feigning_begging_core_harp_lead_on = False
    $ feigning_begging_core_harp_rhythm_on = False
    $ accepting_harmony_cellos_on = False
    $ accepting_harmony_violas_on = False
    $ accepting_harmony_violins_2_on = False
    $ attacking_harmony_french_horns_on = False
    $ attacking_harmony_trombones_on = False
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
        entropy_tint
    window hide
    show ex entropy with Dissolve(3.0)

    "\"It might be easier for you if you stopped digging, accepted that this is a game you were never meant to win.\""

    "It stands up to leave once again."

    "\"If you're truly desperate, then keep scurrying through this labyrinth of despair. You'll find your answer.\""

    pause(2.0)

    scene bg door
    show ex leaving_entropy
    with Dissolve(3.0)

    $ loops += 1

    "It reaches for the door handle, then turns back to you."

    "\"When you have the answer, come visit me here once more. We can be more honest with each other then.\""

    hide ex with Dissolve(3.0)

    menu:
        "Where?":
            jump where