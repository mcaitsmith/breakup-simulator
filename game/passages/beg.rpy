# The script of the game goes in this file.

# BRANCH: BEGGING

# PASSAGE NAME: Beg

label beg:

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
    $ feigning_harmony_alto_choir_on = False
    $ feigning_harmony_tenor_choir_on = False
    $ accepting_melody_violins_1_on = False
    $ accepting_melody_trumpets_on = False
    $ begging_melody_flutes_on = True
    $ begging_melody_oboes_on = False
    $ feigning_melody_soprano_choir_on = False
    $ attacking_accepting_percussion_cymbals_on = False
    $ update_layers(1) # update layer(s)

    "You start pleading with them to stay. You offer change, growth, even the possibility that they don't need to spend the 'future' with you, just a few more months. A few more weeks. Just one more day. They can have anything as long as they stay."

    "'Please don't make this difficult,' they say. 'Just let me go.'"

    "There's a million more things you want to say, but as you try, the words are stopped by the fear that anything you say will just make your situation worse." 

    "You look down and see that you're handing the key to them." 

    "You have no choice. You have to let them go."

    menu:
        "Let them go":
            jump let_go
        "'Do you think we can still be friends?'" if options >= 10:
            jump still_be_friends