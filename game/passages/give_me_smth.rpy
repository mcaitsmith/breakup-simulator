# The script of the game goes in this file.

# BRANCH: BEGGING

# PASSAGE NAME: "Please just say maybe. Give me something."

label give_me_smth:

    $ options += 1

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = False
    $ attacking_bass_tubas_on = False
    $ feigning_bass_bass_choir_on = True
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
    $ begging_harmony_bassoons_on = False
    $ begging_harmony_clarinets_on = False
    $ feigning_harmony_alto_choir_on = True
    $ feigning_harmony_tenor_choir_on = True
    $ accepting_melody_violins_1_on = True
    $ accepting_melody_trumpets_on = False
    $ begging_melody_flutes_on = False
    $ begging_melody_oboes_on = False
    $ feigning_melody_soprano_choir_on = True
    $ attacking_accepting_percussion_cymbals_on = False
    $ update_layers(5) # update layer(s)

    show bg livingroom with Dissolve(3.0):
        begging_tint

    "\"That wouldn't be fair to you. We have to leave it at \"no\" for now.\""

    "Fair to you?! This whole thing has been unfair to you. Pulling the rug out from under you was unfair. They want to talk about \"fair\"? Bullshit."

    menu:
        "\"Fine.\"":
            jump let_go
        "\"Fuck you.\"":
            jump let_go