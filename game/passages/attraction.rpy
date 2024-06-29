# The script of the game goes in this file.

# BRANCH: BEGGING

# PASSAGE NAME: Attraction

label attraction:

    $ options += 1

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = True
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

    show bg livingroom with Dissolve(3.0):
        begging_tint

    "Have you not made your way around the dialogue tree enough to understand yet?"

    menu:
        "{color=#59ba73}Understand what?{/color}" if ending == 8 and hint == True and entropy == 1:
            jump understand_what
        "Understand what?" if ending < 8 or hint == False or (ending == 8 and entropy == 0):
            jump understand_what
        "{color=#59ba73}I think so.{/color}" if ending == 8 and hint == True and entropy == 1:
            jump understand_what
        "I think so." if ending < 8 or hint == False or (ending == 8 and entropy == 0):
            jump understand_what