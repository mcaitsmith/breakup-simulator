﻿# The script of the game goes in this file.

# BRANCH: ENTROPY

# PASSAGE NAME: punish

label punish:

    $ entropy_accent_glockenspiel_on = False
    $ entropy_accent_tubular_bells_on = False
    $ entropy_accent_viola_pluck_on = True
    $ entropy_accent_violin_pluck_on = True
    $ accepting_bass_bass_on = False
    $ attacking_bass_tubas_on = False
    $ feigning_bass_bass_choir_on = False
    $ attacking_accepting_avoiding_core_piano_lead_on = False
    $ attacking_accepting_avoiding_core_piano_rhythm_on = False
    $ entropy_core_marimba_rhythm_on = True
    $ entropy_core_xylophone_lead_on = True
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

    "{color=#6a2ad8}That's okay. I am too. I've no business judging.{/color}"

    "{color=#6a2ad8}If you would just let go of the past, you'd be free. You know that, right? Will you let yourself believe that?{/color}"

    window hide
    pause 5.0

    "{color=#6a2ad8}You don't get to answer that one. No more choices. No more branches.{/color}"

    window hide
    pause 5.0

    "{color=#6a2ad8}Most people are afraid of me. They think I'm here to rob them of their joy.{/color}" 

    window hide
    pause 5.0

    "{color=#6a2ad8}Absurd.{/color}"

    window hide
    pause 5.0

    "{color=#6a2ad8}I give their joy essence. They don't know it but it's the fleeting nature of joy that gives it such zest. Instead they fight me, try desperately to hold onto what was never theirs to begin with. Gluttons.{/color}"

    window hide
    pause 5.0

    "{color=#6a2ad8}They should thank ME.{/color}"

    window hide
    pause 5.0

    menu:
        "But they don't.":
            jump focus