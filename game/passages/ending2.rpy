# The script of the game goes in this file.

# BRANCH: ENTROPY

# PASSAGE NAME: ending 2

label ending2:

    $ ending = 3

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = True
    $ entropy_accent_violin_pluck_on = True
    $ accepting_bass_bass_on = False
    $ attacking_bass_tubas_on = False
    $ feigning_bass_bass_choir_on = False
    $ attacking_accepting_avoiding_core_piano_lead_on = False
    $ attacking_accepting_avoiding_core_piano_rhythm_on = True
    $ entropy_core_marimba_rhythm_on = False
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
    pause(2.0)

    scene black with Dissolve(3.0)

    window hide
    pause 5.0

    "You did it wrong."

    window hide
    pause 5.0

    "I don't know what it was that you said, but somewhere in there you said the wrong thing."

    window hide
    pause 5.0

    "If you lose them, you will die alone and you will deserve it." 

    window hide
    pause 5.0

    "Go back. Find the correct path."

    window hide
    pause 5.0

    "You CAN make them stay."

    menu:
        "Go back.":
            jump intro3