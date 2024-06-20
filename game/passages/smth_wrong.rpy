# The script of the game goes in this file.

# BRANCH: FEIGNING

# PASSAGE NAME: "Did I do something wrong?"

label smth_wrong:

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
    $ feigning_begging_core_harp_rhythm_on = True
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
    $ update_layers(1) # update layer(s)

    "'No. No, you haven't done anything wrong. I swear, if you had, I would've told you. I want to make sure you know that there wasn't anything you could've done differently.' Their voice is shaking as they say this."

    "You can't tell if this is the truth or a fabrication to get themselves out of the situation as quickly as possible. The partner you knew would never do something like this, but the partner you knew would never leave in the first place. Clearly this is someone...else."

    "Even though they say that you didn't do anything wrong, you can't help but imagine all the times you were short with them. You picture every time you got annoyed with them, every eye roll, every 'I think I need some space today' that you requested. In doing so, you doubt that they're telling the truth. Somewhere along the way, you did something that made them lose faith in you."

    "In other words, it's your fault, but maybe that faith can be restored?"

    menu:
        "I don't know who you are anymore.":
            jump arent_telling_me
        "You aren't telling me something.":
            jump arent_telling_me
        "I can win them back.":
            jump stay_silent
        "It is what it is.":
            jump stay_silent