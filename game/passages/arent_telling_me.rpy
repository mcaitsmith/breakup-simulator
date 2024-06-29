# The script of the game goes in this file.

# BRANCH: FEIGNING

# PASSAGE NAME: "You aren't telling me something"

label arent_telling_me:

    $ options += 1

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = False
    $ attacking_bass_tubas_on = False
    $ feigning_bass_bass_choir_on = False
    $ attacking_accepting_avoiding_core_piano_lead_on = False
    $ attacking_accepting_avoiding_core_piano_rhythm_on = False
    $ entropy_core_marimba_rhythm_on = False
    $ entropy_core_xylophone_lead_on = False
    $ feigning_begging_core_harp_lead_on = True
    $ feigning_begging_core_harp_rhythm_on = True
    $ accepting_harmony_cellos_on = False
    $ accepting_harmony_violas_on = False
    $ accepting_harmony_violins_2_on = False
    $ attacking_harmony_french_horns_on = True
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

    show bg livingroom with Dissolve(3.0):
        feigning_tint

    "They sigh."

    "\"I wish it was something we could fix together,\" they say. \"If it was, I promise I would stay here with you and fight to keep what we have, but it isn't. There isn't a future for us and that's that.\""

    "Your stomach is in knots. \"that's that\" they insist." 
    "You look over at the TV, still frozen in place. \"One episode to go\" the screen says at the top."

    menu:
        "Stay silent.":
            jump stay_silent
        "They're abandoning you":
            jump stay_silent
        "The whole relationship was a farce":
            jump stay_silent
        "\"Fuck you.\"" if options >= 15:
            jump f_you