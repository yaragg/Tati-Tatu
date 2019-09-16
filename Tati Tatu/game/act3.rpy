label not_save_yara:

    scene forest_day_bg
    show tati scared at left

    tati "I better run!!!!"
    tati @ upset "(i’m sorry…)"
    play sound fast_steps
    jump back_to_tribe
    return

label back_to_tribe:
    play ambience forest_day_ambience

    scene forest_day_bg
    show tati upset at left

    tati "I should go back to my tribe maybe… Maybe I should never have left…"

    show tuco neutral at right

    tuco @ scared "tati, oh dear! did you see the fire?!"
    tati "Yes!! I just ran from there! That was so scary!"
    tuco @ scared "indeed it was. i almost got fried up myself! "
    tati @ upset "oh no… the wilds… it’s so scary around here. how do you manage to live in such a perilous place? "
    tuco "Well, Tati, it’s a matter of experience and independence."
    tuco "Anywhere and in any place, there will be hardships."
    tuco "The difference is in what you decide to do about it. That’s when you start to know yourself. "
    tati "I understand…"
    tati "I think I wanna go back to my tribe. I’ve had enough of adventures myself. "
    tati "There, I can try and teach them about all I learned on this journey, and maybe I'll change them for the best."
    tuco @ happy "that is very noble of you, tati. "
    tuco "Do want any company on your way back? "
    tati @ neutral "that would be lovely! "

    stop music fadeout 0.3
    play ambience forest_night_ambience
    tati @ neutral "(it’s almost night time though…)"
    tati @ neutral "(should i stop to sleep before heading back?)"

    menu:
        "It’d be safer to wait ‘til morning.":
            jump bad_ending
        "The sooner I get out of here, the better.":
            jump neutral_ending



    return

label neutral_ending:
    scene forest_day_bg
    show tati neutral at left
    show tuco neutral at right

    tati "We should get going then! It’s a long walk back. "
    tuco "For you, maybe. I’ll make good use of my wings, thank you very much."
    tati @ happy "oh, you! "

    scene village1
    show tati neutral at left

    play music menu_theme_ingame

    tati "Well, here I am. "
    tati "Time to try and open up the minds of these people."
    tati "In the end, I’m really grateful for what I have learned."
    tati "If I try and reach them, maybe then for my next adventure I’ll not be alone."
    tati "And each time we will be able to venture forward…"
    tati @ happy "...towards a brand new tomorrow for our tribe. "

    stop music fadeout 1

    $ renpy.pause(1)
    window hide
    show text "NEUTRAL END"
    $ renpy.pause(2)
    scene black with longfade

    return

label bad_ending:
    play ambience forest_night_ambience

    scene forest_day_bg
    show tati neutral at left
    show tuco neutral at right

    tati "But it’s getting dark!"
    tati "I think I’ll sleep somewhere around here and then we can meet in the morning and go. Sounds good?"
    tuco "Of course! We meet tomorrow then. See you, dear. "
    tati "See you, my friend. "

    scene forest_night_bg
    show tati neutral at center

    stop music
    stop ambience
    play music bad_end noloop

    tati "(This feels like a good place to lie down and rest)."
    tati "(And it’s sufficiently distant from the fire, as far as I can see)."
    tati "(I laid down on the ground, hid myself a little between leaves and bushes)."
    tati "(But… it just occurred to me… why did I decide to sleep here?)"
    tati "(I was afraid of the jungle, all I wanted was to head home the fastest I could)."
    tati "(Why… did I even make this decision?)"

    

    tati "(Am I… Am I making my own decisions…?)"

    menu:
        "Yes.":
            jump bad_ending1
        "Yes.":
            jump bad_ending1



    return

label bad_ending1:

    tati "(I… I’m probably going crazy…)"
    tati "(No, No… That was not what I thought..! No, I’m definitely being controlled!)"
    tati "(How do I end this? Why are you controlling me??)"

    menu: 
        "Go to sleep.":
            jump bad_ending2
        "Go to sleep.  ":
            jump bad_ending2



    return

label bad_ending2:

    tati "(I should sleep…?)"
    tati "(I don’t want to sleep… but I’m suddenly so tired…)"
    tati "(…)"

    scene forest_night_bg
    # Hide characters, show only dialog. 

    tati "(...)"
    tati "(Why is everything dark…? Am I dreaming? I probably am.)"
    tati "(My, what a day I’ve had.)"
    tati "(There was a jaguar… a toucan…)"
    tati "(A fire…!)"
    tati "(I’m so horrible… I couldn’t save that girl… )"
    tati "(Why? Why am I like this?)"
    tati "(What… What am I?! WHO AM I?!) "
    tati "(That girl is probably dEAD) "
    tati "(BECAUSE OF mE)"
    tati "(BUT AM I ME? OR AM I… YOU?)"
    tati "(THat GIRL IS-)"

    show cutscene_badending1

    tati "DEAD!!!!!!!"
    #shaking screen
    tati "DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD"
    #shaking screen blinking red
    tati "(and it’s all because of… me)"
    tati "(but…)"
    tati "(w h o  a m  I?)"

    $ renpy.pause(1)
    window hide
    show text "BAD END"
    $ renpy.pause(2)
    scene black with longfade