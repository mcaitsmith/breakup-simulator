# The script of the game goes in this file.

# BRANCH: ENTROPY

# PASSAGE NAME: Understand what?

label understand_what:

    $ options += 1

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = True
    $ attacking_bass_tubas_on = False
    $ feigning_bass_bass_choir_on = False
    $ attacking_accepting_avoiding_core_piano_lead_on = False
    $ attacking_accepting_avoiding_core_piano_rhythm_on = False
    $ entropy_core_marimba_rhythm_on = True
    $ entropy_core_xylophone_lead_on = False
    $ feigning_begging_core_harp_lead_on = True
    $ feigning_begging_core_harp_rhythm_on = False
    $ accepting_harmony_cellos_on = False
    $ accepting_harmony_violas_on = False
    $ accepting_harmony_violins_2_on = False
    $ attacking_harmony_french_horns_on = False
    $ attacking_harmony_trombones_on = False
    $ begging_harmony_bassoons_on = True
    $ begging_harmony_clarinets_on = True
    $ feigning_harmony_alto_choir_on = False
    $ feigning_harmony_tenor_choir_on = False
    $ accepting_melody_violins_1_on = False
    $ accepting_melody_trumpets_on = False
    $ begging_melody_flutes_on = False
    $ begging_melody_oboes_on = True
    $ feigning_melody_soprano_choir_on = False
    $ attacking_accepting_percussion_cymbals_on = False
    $ update_layers(5) # update layer(s)

    scene bg livingroom with Dissolve(3.0):
        entropy_tint

    "\"You're not the problem here.\"" 

    "Impossible. If that were true you wouldn't be stuck here. You'd be somewhere else."

    "\"What I am...I can't do what you want me to do. It isn't in my nature.\""

    menu:
        "What are you?":
            jump what_are_you
        "{color=#59ba73}You're Entropy{/color}" if ending == 8 and hint == True and entropy == 1:
            jump entropy
        "You're Entropy" if (ending < 8 or (ending == 8 and hint == False)) and entropy == 1:
            jump entropy