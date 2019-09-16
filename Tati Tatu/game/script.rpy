# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image black = "#000"
image tati neutral = "images/character/tati neutral.png"
image tati sad = "images/character/tati sad.png"
image tati happy = "images/character/tati curious.png"
image tati curious = "images/character/tati curious.png"
image tati mask = "images/character/tati curious.png"
image tati horrified = "images/character/tati horrified.png"
image tati ritual = "images/character/tati ritual.png"
image tati scared = "images/character/tati upset.png"
image tati upset = "images/character/tati upset.png"
image tati ball = "images/character/tati ball.png"
image tati confused = "images/character/tati confused.png"
image tati surprised = "images/character/tati surprised.png"

image tuco neutral = im.Flip("images/character/tuco neutral.png", horizontal=True)
image tuco happy = im.Flip("images/character/tuco talking.png", horizontal=True)
image tuco talking = im.Flip("images/character/tuco talking.png", horizontal=True)
image tuco ritual = im.Flip("images/character/tuco ritual.png", horizontal=True)
image tuco scared = im.Flip("images/character/tuco neutral.png", horizontal=True)
image xeni neutral = im.Flip("images/character/xeni neutral.png", horizontal=True)
image xeni happy = im.Flip("images/character/xeni happy.png", horizontal=True)
image xeni angry = im.Flip("images/character/xeni angry.png", horizontal=True)

image villager1 = "images/character/villager1.png"
image villager2 = "images/character/villager2.png"
image villagers = "images/bg/aldeoes.png"


image yara neutral = im.Flip("images/character/yara neutral.png", True)
image yara surprised = im.Flip("images/character/yara surprised.png", True)
image yara happy = im.Flip("images/character/yara happy.png", True)
image yara dead = im.Flip("images/character/yara dead.png", True)
image yara neutral = im.Flip("images/character/yara neutral.png", True)
image yara ritual = im.Flip("images/character/yara ritual.png", True)
image yara scared = im.Flip("images/character/yara scared.png", True)

image village1 = "images/bg/aldeia1.jpg"
image village2 = "images/bg/aldeia2.jpg"
image rain = "images/bg/chuva.png"
image forest_day_bg = "images/bg/floresta_densa_dia.jpg"
image forest_night_bg = "images/bg/floresta_densa_noite.jpg"
image forest_fire_bg = "images/bg/forest_fire.png"
image fire1 = "images/bg/fogo1.png"
image fire2 = "images/bg/fogo2.png"
image fire3 = "images/bg/fogo3.png"
image mirror_cutscene = "images/bg/cutscene_espelho.jpg"
image fire_bg_with_yara1 = "images/bg/cutscene_incendio_yara1.jpg"
image fire_bg_with_yara2 = "images/bg/cutscene_incendio_yara2.jpg"
image fire_bg_with_yara3 = "images/bg/cutscene_incendio_yara3.jpg"

image cutscene_badending1 = "images/bg/cutscene_badending1.jpg"
image cutscene_badending2 = "images/bg/cutscene_badending2.jpg"
image cutscene_badending3 = "images/bg/cutscene_badending3.jpg"


define tati = Character("Tati")
define xeni = Character("Xeni")
define villagers = Character("Villager")
define tuco = Character("Tuco")
define yara = Character("Yara")

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define longfade = Fade(2.0, 0.0, 0.5, color="#000")
define mediumfade = Fade(1.0, 0.0, 0.5, color="#000")
define shortfade = Fade(0.5, 0.0, 0.5, color="#000")
define right = Position(xpos = 0.75, xanchor = 0.5)
define left = Position(xpos = 0.23, xanchor = 0.5)

define audio.forest_day_ambience = "sound/ambience/forest_day.wav"
define audio.forest_night_ambience = "sound/ambience/forest_night.wav"
define audio.forest_fire_ambience = "sound/ambience/forest_fire.wav"
define audio.heavy_fire_ambience = "sound/ambience/heavy_fire.wav"
define audio.rain_ambience = "sound/ambience/rain.wav"

define audio.forest_fire = "sound/bgm/forest_fire.wav"
define audio.good_end = "sound/bgm/good_end.wav"
define audio.bad_end = "sound/bgm/bad_end.wav"
define audio.menu_theme = "sound/bgm/menu_theme.wav"
define audio.menu_theme_ingame = "sound/bgm/menu_theme_ingame.wav"
define audio.ritual = "sound/bgm/ritual.wav"
define audio.tuco_theme = "sound/bgm/tuco_theme.wav"
define audio.xeni_theme = "sound/bgm/xeni_theme.wav"


define audio.steps = "sound/sfx/walking.wav"
define audio.fast_steps = "sound/sfx/running.wav"
define audio.log_falling = "sound/sfx/tree_falling.wav"
define audio.shoving = "sound/sfx/shoving.wav"
define audio.click = "sound/sfx/click.wav"


init python:
    renpy.music.register_channel("ambience", mixer="music", loop=True, stop_on_mute=True, tight=True)




# The game starts here.

label start:

    # jump forest_fire
    jump beginning
    return
