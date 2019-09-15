label not_save_capy:

    show forest_bg1
    show taty_scared at left

    tati "I better run!!!!"
    tati @ sad "(i’m sorry…)"
    play sound fast_steps

    return

label back_to_tribe:
    play music sc_forest01

    show forest_bg2
    show taty_sad at left

    tati "I should go back to my tribe maybe… Maybe I should never have left…"

    show toucan_neutral at right

    tuco @ scared "tati, oh dear! did you see the fire?!"
    tati "Yes!! I just ran from there! That was so scary!"
    tuco @ scared "indeed it was. i almost got fried up myself! "
    tati @ sad "oh no… the wilds… it’s so scary around here. how do you manage to live in such a perilous place? "
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
    play music forest_night
    tati @ neutral "(it’s almost night time though…)"
    tati @ neutral "(should i stop to sleep before heading back?)"

    menu:
        "It’d be safer to wait ‘til morning.":
            jump bad_ending
        "The sooner I get out of here, the better.":
            jump neutral_ending



    return

label neutral_ending:
    play music forest_night

    show forest_bg2
    show tati_neutral at left
    show toucan_neutral at right

    tati "We should get going then! It’s a long walk back. "
    tuco "For you, maybe. I’ll make good use of my wings, thank you very much."
    tati @ happy "oh, you! "

    show tribe_bg
    show tati_neutral at left

    play music WGJ_Menu Theme_TR PROD

    tati "Well, here I am. "
    tati "Time to try and open up the minds of these people."
    tati "In the end, I’m really grateful for what I have learned."
    tati "If I try and reach them, maybe then for my next adventure I’ll not be alone."
    tati "And each time we will be able to venture forward…"
    tati @ happy "...towards a brand new tomorrow for our tribe. "

    stop music fadeout 1

[NEUTRAL ENDING]

    return

label bad_ending:
    play music forest_night

    show forest_bg2
    show tati_neutral at left
    show toucan_neutral at right

    tati "But it’s getting dark!"
    tati "I think I’ll sleep somewhere around here and then we can meet in the morning and go. Sounds good?"
    tuco "Of course! We meet tomorrow then. See you, dear. "
    tati "See you, my friend. "

    show forest_bg1
    show tati_neutral at center

    tati "(This feels like a good place to lie down and rest)."
    tati "(And it’s sufficiently distant from the fire, as far as I can see)."
    tati "(I laid down on the ground, hid myself a little between leaves and bushes)."
    tati "(But… it just occurred to me… why did I decide to sleep here?)"
    tati "(I was afraid of the jungle, all I wanted was to head home the fastest I could)."
    tati "(Why… did I even make this decision?)"

    stop music
    play music bad_end

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

    show forest_bg2
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

    show badending_cutscene

    tati "DEAD!!!!!!!"
    #shaking screen
    tati "DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD DEAD"
    #shaking screen blinking red
    tati "(and it’s all because of… me)"
    tati "(but…)"
    tati "(w h o  a m  I?)"