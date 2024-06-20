# The script of the game goes in this file.

# PASSAGE NAME: Intro

label intro:

    # start adaptive music

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

    $ update_layers(0) # update layer(s)
    $ start_layers(0) # start playing layers

    $ ending = 1

    pause 5.0

    scene bg livingroom with fade

    "It's Saturday morning and you're sitting on the couch with your partner of two years, holding hands as you watch the latest binge-worthy show. The sun is shining through the window into your shabby yet cozy apartment. The both of you worked hard to pick out the furniture, the wall art, the rugs. This place is the emboidment of your love, your time spent together. It isn't perfect, but it feels like home."

    "You initially planned to spend the day cleaning, but when you came into the room to see your partner on the couch, when their face lit up as you made eye contact, you knew that you weren't going to do anything productive today. How could you? Not with them sitting there, being perfect."

    "As you feel their palm in yours, you look over and think to yourself 'I've never been so happy in my entire life.'"

    "Your partner takes a breath. They reach over to the remote and pause the show."

    jump intro2
