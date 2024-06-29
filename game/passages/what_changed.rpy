# The script of the game goes in this file.

# BRANCH: BEGGING

# PASSAGE NAME: "So, what changed?"

label what_changed:

    $ options += 1

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = False
    $ entropy_accent_violin_pluck_on = False
    $ accepting_bass_bass_on = False
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

    show bg livingroom with Dissolve(3.0):
        begging_tint

    "\"I don't know. Nothing. Everything.\"" 

    "A vague response." 

    "\"There was a moment where I loved you and then there was a moment where I didn't. I don't know what triggered the switch. It could've been nothing at all. That happens to people sometimes.\""

    "'Nothing at all'? Can people just stop loving you overnight? They go to bed with a full heart and wake up with an empty one?"

    "Perhaps the answer to this question exists elsewhere."

    menu:
        "{color=#59ba73}\"Do you still love me?\"{/color}" if ending == 8 and hint == True and entropy == 1:
            jump still_love_me
        "\"Do you still love me?\"" if ending < 8 or hint == False or (ending == 8 and entropy == 0):
            jump still_love_me
        "{color=#59ba73}\"What the hell does that even mean?!\"{/color}" if ending == 8 and hint == True and entropy == 1:
            jump still_love_me2
        "\"What the hell does that even mean?!\"" if ending < 8 or hint == False or (ending == 8 and entropy == 0):
            jump still_love_me2
        "{color=#59ba73}\"Don't spare my feelings. Just say if you still love me.\"{/color}" if ending == 8 and hint == True and entropy == 1:
            jump still_love_me
        "\"Don't spare my feelings. Just say if you still love me.\"" if ending < 8 or hint == False or (ending == 8 and entropy == 0):
            jump still_love_me