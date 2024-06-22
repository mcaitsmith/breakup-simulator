# The script of the game goes in this file.

# BRANCH: ATTACKING

# PASSAGE NAME: Toxic

label toxic:

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
    $ attacking_harmony_french_horns_on = True
    $ attacking_harmony_trombones_on = False
    $ begging_harmony_bassoons_on = False
    $ begging_harmony_clarinets_on = False
    $ feigning_harmony_alto_choir_on = False
    $ feigning_harmony_tenor_choir_on = True
    $ accepting_melody_violins_1_on = False
    $ accepting_melody_trumpets_on = True
    $ begging_melody_flutes_on = False
    $ begging_melody_oboes_on = False
    $ feigning_melody_soprano_choir_on = False
    $ attacking_accepting_percussion_cymbals_on = False
    $ update_layers(5) # update layer(s)

    scene bg livingroom with Dissolve(3.0):
        attacking_tint

    "A flood of insults begins to pour from you. Every frustration you've ever had with this person is unleashed in a volley of hatred and vitriol." 

    "After two years of loving this person, you know exactly what their weak points are. They made the mistake of betraying you, the one person in the world who can target their insecurities with laser precision. You are going to WIN this." 

    "As you lay into this person, you surprise even yourself with the level of cruelty you show."

    "After several minutes of taking your verbal abuse, your ex partner just sits there. Hollow." 

    "\"I deserve that,\" they say, holding back tears." 

    "Damn right." 

    "They want to leave? Fine. Say something that will haunt them forever."

    menu:
        "Say the most grotesque thing you can imagine.":
            jump keep_going
        "That's enough.":
            jump stay_silent