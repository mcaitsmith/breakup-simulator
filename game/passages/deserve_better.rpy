# The script of the game goes in this file.

# BRANCH: FEIGNING

# PASSAGE NAME: "Oh, not at all. Honestly, you deserve better."

label deserve_better:

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
    $ feigning_harmony_alto_choir_on = False
    $ feigning_harmony_tenor_choir_on = True
    $ accepting_melody_violins_1_on = False
    $ accepting_melody_trumpets_on = False
    $ begging_melody_flutes_on = False
    $ begging_melody_oboes_on = False
    $ feigning_melody_soprano_choir_on = False
    $ attacking_accepting_percussion_cymbals_on = False
    $ update_layers(5) # update layer(s)

    show bg livingroom with Dissolve(3.0):
        feigning_tint

    "\"That's a way to put it, I guess. I think we both deserve better. You deserve someone who is sure about being with you. I deserve...I don't know. Maybe to just be by myself for a while.\""

    menu:
        "{color=#6a2ad8}\"Do you think there's any chance of us...being together again?\"{/color}" if ending == 8 and hint == True and entropy == 0:
            jump any_chance
        "\"Do you think there's any chance of us...being together again?\"" if (ending < 8 or hint == False or (ending == 8 and entropy == 1)):
            jump any_chance
        "\"Good luck with that!\"":
            jump let_go