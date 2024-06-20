# The script of the game goes in this file.

# BRANCH: PASSIVE

# PASSAGE NAME: Key

label key:

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
    $ feigning_begging_core_harp_lead_on = False
    $ feigning_begging_core_harp_rhythm_on = False
    $ accepting_harmony_cellos_on = False
    $ accepting_harmony_violas_on = False
    $ accepting_harmony_violins_2_on = False
    $ attacking_harmony_french_horns_on = False
    $ attacking_harmony_trombones_on = False
    $ begging_harmony_bassoons_on = False
    $ begging_harmony_clarinets_on = False
    $ feigning_harmony_alto_choir_on = True
    $ feigning_harmony_tenor_choir_on = False
    $ accepting_melody_violins_1_on = False
    $ accepting_melody_trumpets_on = False
    $ begging_melody_flutes_on = False
    $ begging_melody_oboes_on = False
    $ feigning_melody_soprano_choir_on = True
    $ attacking_accepting_percussion_cymbals_on = False
    $ update_layers(1) # update layer(s)

    "You reach into your pocket and get your keychain. You twirl the keys around and remove the matching spare key to their apartment." 

    "At one point in the past you had a pretty nasty fight. After saying your apologies, you handed them this key and said 'give this back to me when I've earned it.'" 

    "They ended up giving you the key back after a few hours."

    "They hold out their palm. If you give up this key you'll never be able to enter that place again. It'll be closed off from you forever. Never to open again."

    "You have to give up the key."

    menu:
        "Give up the key":
            jump give_up
        "No. I'm keeping this.":
            jump keeping_this