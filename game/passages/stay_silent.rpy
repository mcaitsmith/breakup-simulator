# The script of the game goes in this file.

# BRANCH: PASSIVE

# PASSAGE NAME: Stay silent.

label stay_silent:

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

    "\"I can't tell you how sorry I really am. You mean so much to me, and the time we've spent together has meant the world. But I think this is what's best for both of us.\"" 

    "No matter how they try to sugarcoat their words, they continue to feel like daggers."

    "They reach into their pocket and hand you the spare key to your apartment. You remember having spare keys made over a year ago. You were together on a trip to the hardware store and saw the key copying machine by the checkout line. It was a sweet spur of the moment gesture that demonstrated the trust they had in you. You could go to their place and they could come to yours. It meant your lives were truly becoming enmeshed." 

    menu:
        "Give them the key to their apartment":
            jump key
        "Start begging":
            jump beg