# The script of the game goes in this file.

# BRANCH: ATTACKING

# PASSAGE NAME: "Fuck you."

label f_you:

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
    $ update_layers(5) # update layer(s)

    show bg livingroom with { "master" : Dissolve(3.0) }:
        attacking_tint
    window hide
    show ex anxious with Dissolve(3.0)

    "The words surprise you as they pass your lips. Each syllable is like a stone being hurled at your partner. How dare they do this to you?"

    "If you're clever, you can deal as much damage to them as they've dealt to you. Maybe then they'll see how horrible what they're doing is and change their mind."

    "\"Look, I-I know I'm blindsiding you here, I know this is shitty, but can we try to at least be mature adults?\""

    menu:
        "\"No, seriously, fuck you.\"":
            jump f_you2
        "\"Sorry, I don't know what came over me.\"":
            jump sorry