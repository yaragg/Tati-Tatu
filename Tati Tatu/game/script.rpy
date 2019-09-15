# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image black = "#000"
image tati neutral = "images/tati neutral.png"
image tati sad = "images/tati sad.png"
image tati happy = "images/tati happy.png"
image tati curious = "images/tati curious.png"
image tati mask = "images/tati curious.png"
image tati horrified = "images/tati horrified.png"
image tati ritual = "images/tati ritual.png"
image tati scared = "images/tati upset.png"
image tati upset = "images/tati upset.png"
image tati ball = "images/tati ball.png"
image tati confused = "images/tati confused.png"
image tati surprised = "images/tati surprised.png"



image tuco neutral = "images/tuco neutral.png"
image tuco happy = "images/tuco talking.png"
image tuco talking = "images/tuco talking.png"
image tuco ritual = "images/tuco ritual.png"
image tuco scared = "images/tuco scared.png"
image xeni neutral = "images/xeni neutral.png"
image xeni happy = "images/xeni happy.png"
image xeni angry = "images/xeni angry.png"

image villager1 = "images/villager1.png"
image villager2 = "images/villager2.png"
image villagers = "images/aldeoes.png"


image yara neutral = "images/yara neutral.png"
image yara surprised = "images/yara surprised.png"
image yara happy = "images/yara happy.png"
image yara dead = "images/yara dead.png"
image yara neutral = "images/yara neutral.png"
image yara ritual = "images/yara ritual.png"
image yara scared = "images/yara scared.png"

image tribe_bg = "images/aldeia1.jpg"
image aldeia1 = "images/aldeia1.jpg"
image aldeia2 = "images/aldeia2.jpg"
image aldeoes = "images/aldeoes.png"
image chuva = "images/chuva.png"
image floresta_densa_dia = "images/floresta_densa_dia.jpg"
image forest_day_bg = "images/floresta_densa_dia.jpg"
image floresta_densa_noite = "images/floresta_densa_noite.jpg"
image chuva = "images/chuva.png"
image forest_fire_bg = "images/forest_fire.png"
image fire1 = "images/fogo1.png"
image fire2 = "images/fogo2.png"
image fire3 = "images/fogo3.png"
image cutscene_mirror = "images/cutscene_espelho.jpg"
image cutscene_reflexo = "images/cutscene_espelho.jpg"






define tati = Character("Tati")
define xeni = Character("Xeni")
define villagers = Character("Villager")
define tuco = Character("Tuco")
define yara = Character("Yara")

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define longfade = Fade(2.0, 0.0, 0.5, color="#000")
define right = Position(xpos = 0.75, xanchor = 0.5)
define left = Position(xpos = 0.23, xanchor = 0.5)

define audio.forest_ambience = "sound/bgm/forest_day.wav"
define audio.forest_day = "sound/bgm/forest_day.wav"

define audio.mu_onca = "sound/bgm/xeni_theme.wav"
define audio.sc_forest01 = "sound/bgm/forest_day.wav"
define audio.sc_forest = "sound/bgm/forest_day.wav"
define audio.mu_tucano = "sound/bgm/tuca_theme.wav"
define audio.sc_forest_night = "sound/bgm/forest_night.wav"
define audio.forest_fire = "sound/bgm/forest_fire.wav"
define audio.good_end = "sound/bgm/good_end.wav"
define audio.bad_end = "sound/bgm/bad_end.wav"
define audio.menu_theme = "sound/bgm/menu_theme.wav"
define audio.ritual = "sound/bgm/ritual.wav"
define audio.tuca_theme = "sound/bgm/tuca_theme.wav"
define audio.xeni_theme = "sound/bgm/xeni_theme.wav"

define audio.steps = "sound/sfx/placeholder.mp3"
define audio.fast_steps = "sound/sfx/placeholder.mp3"
define audio.bird_flying_away = "sound/sfx/placeholder.mp3"
define audio.fire_burning = "sound/sfx/placeholder.mp3"
define audio.log_falling = "sound/sfx/placeholder.mp3"
define audio.shoving = "sound/sfx/placeholder.mp3"
define audio.rain = "sound/sfx/placeholder.mp3"




# The game starts here.

label start:

    # jump forest_fire
    jump beginning
    return
