# The script of the game goes in this file.

# PASSAGE NAME: Intro part 3

label intro3:

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
    pause(2.0)

    if ending >= 2:

        scene bg livingroom with Dissolve(3.0)
        window hide
        show ex neutral with Dissolve(3.0)

        "You blink and suddenly they're here again. You've been given another chance to get it right this time."

        window hide
        pause 1.0

    "\"I've been thinking for a while and...\" Their voice trails off. They're clearly trying to find the words to soften the blow. But the more they search, the less it seems like they can find them. Something changes in their face. You assume this means they're accepting their role. They have no choice but to hurt you."

    "\"I don't see a future with you.\"" 

    "And there it is. You never saw it coming. Not in a million years. But there it is anyway."

    menu:
        "\"What changed?\"":
            jump why_not
        "\"Did I do something wrong?\"":
            jump smth_wrong
        "{color=#db7b54}\"Okay! No Problem!\"{/color}" if options >= 10 and chose_okay == False:
            $ chose_okay = True
            jump okay
        "\"Okay! No Problem!\"" if options >= 10 and chose_okay == True:
            jump okay
        "{color=#59ba73}\"But I see a future with you.\"{/color}" if options >= 5 and ending == 8 and entropy == 1 and hint == True:
            $ chose_future = True
            jump future
        "{color=#db7b54}\"But I see a future with you.\"{/color}" if options >= 5 and (hint == False or ending < 8 or (ending == 8 and entropy == 0)) and chose_future == False:
            $ chose_future = True
            jump future
        "\"But I see a future with you.\"" if options >= 5 and (hint == False or ending < 8 or (ending == 8 and entropy == 0)) and chose_future == True:
            jump future
        "{color=#db7b54}\"Fuck you.\"{/color}" if options >= 15 and chose_f_you == False:
            $ chose_f_you = True
            jump f_you
        "\"Fuck you.\"" if options >= 15 and chose_f_you == True:
            jump f_you
        "{color=#db7b54}Stay silent.{/color}" if options >= 5 and chose_silent == False:
            $ chose_silent = True
            jump stay_silent
        "Stay silent." if options >= 5 and chose_silent == True:
            jump stay_silent
        "{color=#6a2ad8}\"I understand.\"{/color}" if options >= 20 and ending == 8 and entropy == 0 and hint == True:
            $ chose_understand = True
            jump i_understand
        "{color=#db7b54}\"I understand.\"{/color}" if options >= 20 and (hint == False or ending < 8 or (ending == 8 and entropy == 1)) and chose_understand == False:
            $ chose_understand = True
            jump i_understand
        "\"I understand.\""  if options >= 20 and (hint == False or ending < 8 or (ending == 8 and entropy == 1)) and chose_understand == True:
            jump i_understand