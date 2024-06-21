# The script of the game goes in this file.

# BRANCH: ACCEPTING

# PASSAGE NAME: "I understand."

label i_understand:

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

    "\"Y-you do?\" They seem surprised and a bit relieved. It seems clear that they don't want to hurt you. But at the same time it seems like they're not sacrificing any more of their happiness to protect your feelings."

    "You could say that's cruel."

    "You could say it's even more cruel to let you live a lie, thinking you had a partner who was happy when you don't." 

    "Either way, it's all over now. It was over a while ago. You're just getting the memo now. Better now than in a year." 

    "Or ten years." 

    menu:
        "\"I guess.\"":
            jump stay_silent
        "\"It's better this way.\"":
            jump better_this_way