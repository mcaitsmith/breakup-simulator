# The script of the game goes in this file.

# BRANCH: BEGGING

# PASSAGE NAME: "But I see a future with you."

label future:

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
    pause(2.0)

    "\"I know.\" They avoid making eye contact with you. \"We both said a lot of things about the future, about living together and getting married. I meant those things when I said them.\""

    "They said quite a bit more than that. They told you that your souls were forever enmeshed. They said it in a poem written on a piece of notebook paper. It was folded into an origami crane and left on your pillow one morning. The crane is still in a little box in your closet."

    menu:
        "\"So, what changed?\"":
            jump what_changed
        "\"Bullshit. You lied to me.\"":
            jump you_lied