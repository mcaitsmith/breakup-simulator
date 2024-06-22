# The script of the game goes in this file.

# BRANCH: FEIGNING/ACCEPTING

# PASSAGE NAME: "Sorry, I don't know what came over me."

label sorry:

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
    $ begging_melody_oboes_on = True
    $ feigning_melody_soprano_choir_on = False
    $ attacking_accepting_percussion_cymbals_on = False
    $ update_layers(5) # update layer(s)

    scene bg livingroom with Dissolve(3.0):
        feigning_accepting_tint

    "\"It's fine. You have a right to be angry.\""

    "You look at their hands and see that their fingers are red and scarred. They've been picking at their nails incessantly for days." 

    "This is an old habit of theirs. Something they do when they have something they need to do but keep putting it off, like sending a senstive email, or calling their parents. In the past you wrapped bandages around their fingers and held them until they got over whatever hurdle they were faced with."

    "But not today. Today the hurdle is you. And you proved their fears warranted."

    "\"I never wanted to blindside you,\" they say." 

    menu:
        "Continue":
            jump stay_silent