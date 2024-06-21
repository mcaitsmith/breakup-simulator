# The script of the game goes in this file.

# BRANCH: ENTROPY

# PASSAGE NAME: You're helpless to stop it.

label helpless:

    $ options += 1

    $ entropy_accent_glockenspiel_on = True
    $ entropy_accent_tubular_bells_on = True
    $ entropy_accent_viola_pluck_on = True
    $ entropy_accent_violin_pluck_on = True
    $ accepting_bass_bass_on = False
    $ attacking_bass_tubas_on = False
    $ feigning_bass_bass_choir_on = False
    $ attacking_accepting_avoiding_core_piano_lead_on = True
    $ attacking_accepting_avoiding_core_piano_rhythm_on = True
    $ entropy_core_marimba_rhythm_on = False
    $ entropy_core_xylophone_lead_on = False
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
    $ update_layers(3) # update layer(s)

    scene bg door with Dissolve(3.0)

    "As they leave the apartment, it's just you and" 

    menu:
        "the silence they've left behind." if ending == 1:
            jump ending1
        "the silence they've left behind." if ending == 2:
            jump ending2
        "the silence they've left behind." if ending == 3:
            jump ending3
        "the silence they've left behind." if ending == 4:
            jump ending4
        "the silence they've left behind." if ending == 5:
            jump ending5
        "the silence they've left behind." if ending == 6:
            jump ending6
        "the silence they've left behind." if ending == 7:
            jump ending7
        "the silence they've left behind." if ending == 8:
            jump ending8