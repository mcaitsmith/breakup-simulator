# The script of the game goes in this file.

# BRANCH: ATTACKING

# PASSAGE NAME: "Throwing me away won't fix your life. You don't have to be alone."

label throwing_me_away:

    $ options += 1

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = False
    $ attacking_bass_tubas_on = True
    $ feigning_bass_bass_choir_on = False
    $ attacking_accepting_avoiding_core_piano_lead_on = True
    $ attacking_accepting_avoiding_core_piano_rhythm_on = True
    $ entropy_core_marimba_rhythm_on = False
    $ entropy_core_xylophone_lead_on = False
    $ feigning_begging_core_harp_lead_on = False
    $ feigning_begging_core_harp_rhythm_on = False
    $ accepting_harmony_cellos_on = False
    $ accepting_harmony_violas_on = True
    $ accepting_harmony_violins_2_on = True
    $ attacking_harmony_french_horns_on = True
    $ attacking_harmony_trombones_on = True
    $ begging_harmony_bassoons_on = False
    $ begging_harmony_clarinets_on = False
    $ feigning_harmony_alto_choir_on = False
    $ feigning_harmony_tenor_choir_on = True
    $ accepting_melody_violins_1_on = False
    $ accepting_melody_trumpets_on = True
    $ begging_melody_flutes_on = False
    $ begging_melody_oboes_on = False
    $ feigning_melody_soprano_choir_on = False
    $ attacking_accepting_percussion_cymbals_on = True
    $ update_layers(5) # update layer(s)

    show bg livingroom with { "master" : Dissolve(3.0) }:
        attacking_tint
    window hide
    show ex frustrated with Dissolve(3.0)

    "\"I'm not throwing you away.\"" 

    "You notice their hands shaking." 

    "What's this?" 

    "Guilt? Shame? An opening in their armor?"

    menu:
        "{color=#6a2ad8}\"Yes you are.\"{/color}" if ending == 8 and hint == True and entropy == 0:
            jump yes_you_are
        "\"Yes you are.\"" if (ending < 8 or hint == False or (ending == 8 and entropy == 1)):
            jump yes_you_are
        "\"Whatever.\"":
            jump stay_silent
        "\"Do you think we can still be friends?\"":
            jump still_be_friends