# The script of the game goes in this file.

# BRANCH: BEGGING/PASSIVE

# PASSAGE NAME: "Why not?"

label why_not:

    $ options += 1

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = False
    $ attacking_bass_tubas_on = False
    $ feigning_bass_bass_choir_on = False
    $ attacking_accepting_avoiding_core_piano_lead_on = True
    $ attacking_accepting_avoiding_core_piano_rhythm_on = True
    $ entropy_core_marimba_rhythm_on = False
    $ entropy_core_xylophone_lead_on = False
    $ feigning_begging_core_harp_lead_on = False
    $ feigning_begging_core_harp_rhythm_on = False
    $ accepting_harmony_cellos_on = True
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
    $ begging_melody_oboes_on = True
    $ feigning_melody_soprano_choir_on = False
    $ attacking_accepting_percussion_cymbals_on = False
    $ update_layers(5) # update layer(s)
    pause(2.0)

    "\"I-I don't know. Believe me, I've been trying really hard to make things work between us. But when I try to imagine my future, and I picture you there, it just doesn't feel right.\""

    "You recall having the same experience, imagining your future together, except you couldn't imagine your future WITHOUT them. To hear that they couldn't imagine it WITH you..."

    "This is not the same person you've loved for the past two years. Something has changed. There has to have been something."

    menu:
        "\"Did I do something wrong?\"":
            jump smth_wrong
        "\"I understand.\"" if options >= 20:
            jump i_understand
        "Stay silent.":
            jump stay_silent