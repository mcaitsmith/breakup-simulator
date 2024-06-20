# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(kind=nvl)

# define location images
# image bg main = "backgrounds/bg office.png"
# image bg office blur = im.Blur("backgrounds/bg office.png", 1.5) # blurred version

# image policelights:
#     "#f00"
#     alpha 0.0
#     linear .45 alpha 0.2    
#     linear .45 alpha 0.0
#     "#00f"
#     alpha 0.0
#     linear .45 alpha 0.2    
#     linear .45 alpha 0.0
#     repeat

# define sound effects & music
# define sfx_clatter = "audio/sfx/Clatter_SantaSecret_SFX.wav"
define bg_music = "audio/V1_Saying_Goodbye.ogg"

init python:
    # define music channels
    renpy.music.register_channel("ENTROPY ACCENT Glockenspiel", "music")
    renpy.music.register_channel("ENTROPY ACCENT Tubular Bells", "music")
    renpy.music.register_channel("ENTROPY ACCENT Viola Pluck", "music")
    renpy.music.register_channel("ENTROPY ACCENT Violin Pluck", "music")

    renpy.music.register_channel("ACCEPTING BASS Bass", "music")
    renpy.music.register_channel("ATTACKING BASS Tubas", "music")
    renpy.music.register_channel("FEIGNING BASS Bass Choir", "music")

    renpy.music.register_channel("ATTACKING-ACCEPTING-AVOIDING CORE Piano Lead", "music")
    renpy.music.register_channel("ATTACKING-ACCEPTING-AVOIDING CORE Piano Rhythm", "music")
    renpy.music.register_channel("ENTROPY CORE Marimba Rhythm", "music")
    renpy.music.register_channel("ENTROPY CORE Xylophone Lead", "music")
    renpy.music.register_channel("FEIGNING-BEGGING CORE Harp Lead", "music")
    renpy.music.register_channel("FEIGNING-BEGGING CORE Harp Rhythm", "music")

    renpy.music.register_channel("ACCEPTING HARMONY Cellos", "music")
    renpy.music.register_channel("ACCEPTING HARMONY Violas", "music")
    renpy.music.register_channel("ACCEPTING HARMONY Violins 2", "music")
    renpy.music.register_channel("ATTACKING HARMONY French Horns", "music")
    renpy.music.register_channel("ATTACKING HARMONY Trombones", "music")
    renpy.music.register_channel("BEGGING HARMONY Bassoons", "music")
    renpy.music.register_channel("BEGGING HARMONY Clarinets", "music")
    renpy.music.register_channel("FEIGNING HARMONY Alto Choir", "music")
    renpy.music.register_channel("FEIGNING HARMONY Tenor Choir", "music")

    renpy.music.register_channel("ACCEPTING MELODY Violins 1", "music")
    renpy.music.register_channel("ATTACKING MELODY Trumpets", "music")
    renpy.music.register_channel("BEGGING MELODY Flutes", "music")
    renpy.music.register_channel("BEGGING MELODY Oboes", "music")
    renpy.music.register_channel("FEIGNING MELODY Soprano Choir", "music")

    renpy.music.register_channel("ATTACKING-ACCEPTING PERCUSSION Cymbals", "music")

    # function to start playing layers
    def start_layers(delay=3):
        renpy.music.play("audio/music/ACCENT/ENTROPY ACCENT Glockenspiel.ogg", channel='ENTROPY ACCENT Glockenspiel', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/ACCENT/ENTROPY ACCENT Tubular Bells.ogg", channel='ENTROPY ACCENT Tubular Bells', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/ACCENT/ENTROPY ACCENT Viola Pluck.ogg", channel='ENTROPY ACCENT Viola Pluck', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/ACCENT/ENTROPY ACCENT Violin Pluck.ogg", channel='ENTROPY ACCENT Violin Pluck', loop=True, synchro_start=True, fadein=delay)

        renpy.music.play("audio/music/BASS/ACCEPTING BASS Bass.ogg", channel='ACCEPTING BASS Bass', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/BASS/ATTACKING BASS Tubas.ogg", channel='ATTACKING BASS Tubas', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/BASS/FEIGNING BASS Bass Choir.ogg", channel='FEIGNING BASS Bass Choir', loop=True, synchro_start=True, fadein=delay)

        renpy.music.play("audio/music/CORE/ATTACKING-ACCEPTING-AVOIDING CORE Piano Lead.ogg", channel='ATTACKING-ACCEPTING-AVOIDING CORE Piano Lead', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/CORE/ATTACKING-ACCEPTING-AVOIDING CORE Piano Rhythm.ogg", channel='ATTACKING-ACCEPTING-AVOIDING CORE Piano Rhythm', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/CORE/ENTROPY CORE Marimba Rhythm.ogg", channel='ENTROPY CORE Marimba Rhythm', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/CORE/ENTROPY CORE Xylophone Lead.ogg", channel='ENTROPY CORE Xylophone Lead', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/CORE/FEIGNING-BEGGING CORE Harp Lead.ogg", channel='FEIGNING-BEGGING CORE Harp Lead', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/CORE/FEIGNING-BEGGING CORE Harp Rhythm.ogg", channel='FEIGNING-BEGGING CORE Harp Rhythm', loop=True, synchro_start=True, fadein=delay)

        renpy.music.play("audio/music/HARMONY/ACCEPTING HARMONY Cellos.ogg", channel='ACCEPTING HARMONY Cellos', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/HARMONY/ACCEPTING HARMONY Violas.ogg", channel='ACCEPTING HARMONY Violas', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/HARMONY/ACCEPTING HARMONY Violins 2.ogg", channel='ACCEPTING HARMONY Violins 2', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/HARMONY/ATTACKING HARMONY French Horns.ogg", channel='ATTACKING HARMONY French Horns', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/HARMONY/ATTACKING HARMONY Trombones.ogg", channel='ATTACKING HARMONY Trombones', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/HARMONY/BEGGING HARMONY Bassoons.ogg", channel='BEGGING HARMONY Bassoons', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/HARMONY/BEGGING HARMONY Clarinets.ogg", channel='BEGGING HARMONY Clarinets', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/HARMONY/FEIGNING HARMONY Alto Choir.ogg", channel='FEIGNING HARMONY Alto Choir', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/HARMONY/FEIGNING HARMONY Tenor Choir.ogg", channel='FEIGNING HARMONY Tenor Choir', loop=True, synchro_start=True, fadein=delay)

        renpy.music.play("audio/music/MELODY/ACCEPTING MELODY Violins 1.ogg", channel='ACCEPTING MELODY Violins 1', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/MELODY/ATTACKING MELODY Trumpets.ogg", channel='ATTACKING MELODY Trumpets', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/MELODY/BEGGING MELODY Flutes.ogg", channel='BEGGING MELODY Flutes', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/MELODY/BEGGING MELODY Oboes.ogg", channel='BEGGING MELODY Oboes', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/music/MELODY/FEIGNING MELODY Soprano Choir.ogg", channel='FEIGNING MELODY Soprano Choir', loop=True, synchro_start=True, fadein=delay)

        renpy.music.play("audio/music/PERCUSSION/ATTACKING-ACCEPTING PERCUSSION Cymbals.ogg", channel='ATTACKING-ACCEPTING PERCUSSION Cymbals', loop=True, synchro_start=True, fadein=delay)

    # function to stop playing layers
    def stop_layers(delay=None):
        renpy.music.stop(channel='ENTROPY ACCENT Glockenspiel', fadeout=delay)
        renpy.music.stop(channel='ENTROPY ACCENT Tubular Bells', fadeout=delay)
        renpy.music.stop(channel='ENTROPY ACCENT Viola Pluck', fadeout=delay)
        renpy.music.stop(channel='ENTROPY ACCENT Violin Pluck', fadeout=delay)
        renpy.music.stop(channel='ACCEPTING BASS Bass', fadeout=delay)
        renpy.music.stop(channel='ATTACKING BASS Tubas', fadeout=delay)
        renpy.music.stop(channel='FEIGNING BASS Bass Choir', fadeout=delay)
        renpy.music.stop(channel='ATTACKING-ACCEPTING-AVOIDING CORE Piano Lead', fadeout=delay)
        renpy.music.stop(channel='ATTACKING-ACCEPTING-AVOIDING CORE Piano Rhythm', fadeout=delay)
        renpy.music.stop(channel='ENTROPY CORE Marimba Rhythm', fadeout=delay)
        renpy.music.stop(channel='ENTROPY CORE Xylophone Lead', fadeout=delay)
        renpy.music.stop(channel='FEIGNING-BEGGING CORE Harp Lead', fadeout=delay)
        renpy.music.stop(channel='FEIGNING-BEGGING CORE Harp Rhythm', fadeout=delay)
        renpy.music.stop(channel='ACCEPTING HARMONY Cellos', fadeout=delay)
        renpy.music.stop(channel='ACCEPTING HARMONY Violas', fadeout=delay)
        renpy.music.stop(channel='ACCEPTING HARMONY Violins 2', fadeout=delay)
        renpy.music.stop(channel='ATTACKING HARMONY French Horns', fadeout=delay)
        renpy.music.stop(channel='ATTACKING HARMONY Trombones', fadeout=delay)
        renpy.music.stop(channel='BEGGING HARMONY Bassoons', fadeout=delay)
        renpy.music.stop(channel='BEGGING HARMONY Clarinets', fadeout=delay)
        renpy.music.stop(channel='FEIGNING HARMONY Alto Choir', fadeout=delay)
        renpy.music.stop(channel='FEIGNING HARMONY Tenor Choir', fadeout=delay)
        renpy.music.stop(channel='ACCEPTING MELODY Violins 1', fadeout=delay)
        renpy.music.stop(channel='ATTACKING MELODY Trumpets', fadeout=delay)
        renpy.music.stop(channel='BEGGING MELODY Flutes', fadeout=delay)
        renpy.music.stop(channel='BEGGING MELODY Oboes', fadeout=delay)
        renpy.music.stop(channel='FEIGNING MELODY Soprano Choir', fadeout=delay)
        renpy.music.stop(channel='ATTACKING-ACCEPTING PERCUSSION Cymbals', fadeout=delay)

    # function to update layers
    def update_layers(delay=1):
        entropy_accent_glockenspiel = 1 if entropy_accent_glockenspiel_on else 0
        entropy_accent_tubular_bells = 1 if entropy_accent_tubular_bells_on else 0
        entropy_accent_viola_pluck = 1 if entropy_accent_viola_pluck_on else 0
        entropy_accent_violin_pluck = 1 if entropy_accent_violin_pluck_on else 0
        accepting_bass_bass = 1 if accepting_bass_bass_on else 0
        attacking_bass_tubas = 1 if attacking_bass_tubas_on else 0
        feigning_bass_bass_choir = 1 if feigning_bass_bass_choir_on else 0
        attacking_accepting_avoiding_core_piano_lead = 1 if attacking_accepting_avoiding_core_piano_lead_on else 0
        attacking_accepting_avoiding_core_piano_rhythm = 1 if attacking_accepting_avoiding_core_piano_rhythm_on else 0
        entropy_core_marimba_rhythm = 1 if entropy_core_marimba_rhythm_on else 0
        entropy_core_xylophone_lead = 1 if entropy_core_xylophone_lead_on else 0
        feigning_begging_core_harp_lead = 1 if feigning_begging_core_harp_lead_on else 0
        feigning_begging_core_harp_rhythm = 1 if feigning_begging_core_harp_rhythm_on else 0
        accepting_harmony_cellos = 1 if accepting_harmony_cellos_on else 0
        accepting_harmony_violas = 1 if accepting_harmony_violas_on else 0
        accepting_harmony_violins_2 = 1 if accepting_harmony_violins_2_on else 0
        attacking_harmony_french_horns = 1 if attacking_harmony_french_horns_on else 0
        attacking_harmony_trombones = 1 if accepting_harmony_trombones_on else 0
        begging_harmony_bassoons = 1 if begging_harmony_bassoons_on else 0
        begging_harmony_clarinets = 1 if begging_harmony_clarinets_on else 0
        feigning_harmony_alto_choir = 1 if feigning_harmony_alto_choir_on else 0
        feigning_harmony_tenor_choir = 1 if feigning_harmony_tenor_choir_on else 0
        accepting_melody_violins_1 = 1 if accepting_melody_violins_1_on else 0
        accepting_melody_trumpets = 1 if accepting_melody_trumpets_on else 0
        begging_melody_flutes = 1 if begging_melody_flutes_on else 0
        begging_melody_oboes = 1 if begging_melody_oboes_on else 0
        feigning_melody_soprano_choir = 1 if feigning_melody_soprano_choir_on else 0
        attacking_accepting_percussion_cymbals = 1 if attacking_accepting_percussion_cymbals_on else 0
        
        renpy.music.set_volume(entropy_accent_glockenspiel, delay=delay, channel='ENTROPY ACCENT Glockenspiel')
        renpy.music.set_volume(entropy_accent_tubular_bells, delay=delay, channel='ENTROPY ACCENT Tubular Bells')
        renpy.music.set_volume(entropy_accent_viola_pluck, delay=delay, channel='ENTROPY ACCENT Viola Pluck')
        renpy.music.set_volume(entropy_accent_violin_pluck, delay=delay, channel='ENTROPY ACCENT Violin Pluck')
        renpy.music.set_volume(accepting_bass_bass, delay=delay, channel='ACCEPTING BASS Bass')
        renpy.music.set_volume(attacking_bass_tubas, delay=delay, channel='ATTACKING BASS Tubas')
        renpy.music.set_volume(feigning_bass_bass_choir, delay=delay, channel='FEIGNING BASS Bass Choir')
        renpy.music.set_volume(attacking_accepting_avoiding_core_piano_lead, delay=delay, channel='ATTACKING-ACCEPTING-AVOIDING CORE Piano Lead')
        renpy.music.set_volume(attacking_accepting_avoiding_core_piano_rhythm, delay=delay, channel='ATTACKING-ACCEPTING-AVOIDING CORE Piano Rhythm')
        renpy.music.set_volume(entropy_core_marimba_rhythm, delay=delay, channel='ENTROPY CORE Marimba Rhythm')
        renpy.music.set_volume(entropy_core_xylophone_lead, delay=delay, channel='ENTROPY CORE Xylophone Lead')
        renpy.music.set_volume(feigning_begging_core_harp_lead, delay=delay, channel='FEIGNING-BEGGING CORE Harp Lead')
        renpy.music.set_volume(feigning_begging_core_harp_rhythm, delay=delay, channel='FEIGNING-BEGGING CORE Harp Rhythm')
        renpy.music.set_volume(accepting_harmony_cellos, delay=delay, channel='ACCEPTING HARMONY Cellos')
        renpy.music.set_volume(accepting_harmony_violas, delay=delay, channel='ACCEPTING HARMONY Violas')
        renpy.music.set_volume(accepting_harmony_violins_2, delay=delay, channel='ACCEPTING HARMONY Violins 2')
        renpy.music.set_volume(attacking_harmony_french_horns, delay=delay, channel='ATTACKING HARMONY French Horns')
        renpy.music.set_volume(attacking_harmony_trombones, delay=delay, channel='ATTACKING HARMONY Trombones')
        renpy.music.set_volume(begging_harmony_bassoons, delay=delay, channel='BEGGING HARMONY Bassoons')
        renpy.music.set_volume(begging_harmony_clarinets, delay=delay, channel='BEGGING HARMONY Clarinets')
        renpy.music.set_volume(feigning_harmony_alto_choir, delay=delay, channel='FEIGNING HARMONY Alto Choir')
        renpy.music.set_volume(feigning_harmony_tenor_choir, delay=delay, channel='FEIGNING HARMONY Tenor Choir')
        renpy.music.set_volume(accepting_melody_violins_1, delay=delay, channel='ACCEPTING MELODY Violins 1')
        renpy.music.set_volume(accepting_melody_trumpets, delay=delay, channel='ATTACKING MELODY Trumpets')
        renpy.music.set_volume(begging_melody_flutes, delay=delay, channel='BEGGING MELODY Flutes')
        renpy.music.set_volume(begging_melody_oboes, delay=delay, channel='BEGGING MELODY Oboes')
        renpy.music.set_volume(feigning_melody_soprano_choir, delay=delay, channel='FEIGNING MELODY Soprano Choir')
        renpy.music.set_volume(attacking_accepting_percussion_cymbals, delay=delay, channel='ATTACKING-ACCEPTING PERCUSSION Cymbals')

# The game starts here.

label start:

    $ options = 0
    $ entropy = 0
    $ ending = 0

    play music bg_music

    jump intro