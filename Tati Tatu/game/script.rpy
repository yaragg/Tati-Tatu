# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image black = "#000"

define tati = Character("Tati")
define xeni = Character("Xeni")
define villagers = Character("Villager")
define tuco = Character("Tuco")
define yara = Character("Yara")

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define longfade = Fade(2.0, 0.0, 0.5, color="#000")
define right = Position(xpos = 0.75, xanchor = 0.5)
define left = Position(xpos = 0.23, xanchor = 0.5)


# The game starts here.

label start:

    jump beginning

    return
