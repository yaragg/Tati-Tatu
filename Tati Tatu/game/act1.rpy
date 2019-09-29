image villagers_animated:
        "images/bg/aldeoes.png"
        xtile 5
        parallel:
            xanchor 1.0
            linear 120.0 xanchor 0.0
            repeat
        parallel:
            xpos 0.0
            linear 120.0 xpos 1.0
            repeat


label beginning:
 
    #fade in village1
    stop music
    play ambience forest_day_ambience
    scene village1
    show tati upset at left


    tati "Yet another day like all the others..."


    #play sound steps


    tati "Waking up, harvest some fruits, fetching water, cleaning up stuff. The same routine, every. single. Day."
    # a word per line 
    tati "I don’t know how I can stand it, believe me."
    tati "Everything around here is so boring. Nothing ever happens, everyone stays the same, following the same guidelines. "
    tati "No new knowledge, no excitement, nothing. "
    tati "Even the sounds are the same..."
    tati "If they could ever agree on questing outside this clearing… maybe things would change. But well, who am I? I can’t even tell for sure if there’s life out of here. "
    tati "I’m just the simple Tati stuck on her boring life. Just another one among these dozens."
    tati "(Ugh, I should just stop complaining and pick the berries already…)"
 
    #play sound steps
    play sound steps
    $ renpy.pause(1.5)
 
    show tati surprised at left
 
    tati "Oh, what’s that?"


    show tati mask at left
 
    tati "Oh my, what do we have here… This is new!"
    tati "Ha! Who said that complaining leads to nothing? This is a miracle! "
    tati "This surely isn’t from my tribe! Which means that there really is a world unknown to me behind these wooden bars…"
    tati @ upset "A world I’ve been deprived of, for my whole life, out of the fear of the people who came before me. "
    tati "A world these people taught me it never existed. Now I can prove them wrong… I knew it! "
    tati surprised "Where are my friends?! I need to tell them! "
    hide tati with easeoutright
 
    # fade out screen
    # fade in village1
    scene black with shortfade
    scene village1 with shortfade

    show villagers_animated
    show tati surprised at Position(xpos = 0.13, xanchor = 0.5) with dissolve
    # show villagers at right
 
    tati "Oh, there they are!"
 
    # slide tati to center
 
    show tati mask
    tati "Hey, take a look at this! I found it lying on the forest entrance and-"
 
    #shake villagers
    show villager1 at center with dissolve
    hugo "What the heck is this, Tati?! Throw it out!!! It might be poisonous!!!"

    show villager2 at right with dissolve
    iago "You shouldn’t be seeking out stuff like that! I’m gonna tell the chief!!"

    hide villager2 with easeoutright
    hide villager1 with easeoutright
 
    #slide villagers out
    tati "But…"
    show tati at left with MoveTransition(0.8)
    $ renpy.pause(0.5)

    show tati upset

    tati "(Huh. Why did I have hope they would react any different?)"
    tati "(Fine then, I’ll try discovering about it by myself…)"
    tati @ neutral "(This is my chance to finally explore the unknown. I won’t blow it.) "
    tati "(I’ll have to sneak out of the village. Telling my parents is a no - they will react if not worse, the same as Hugo and Iago)"
    
    show tati confused at left
    tati "(Should I wait for night time? Or maybe go right now?)"


    menu:
        "Explore during the day":
            jump tuco_presentation_day
        "Wait for the night to sneak out":
            jump tuco_presentation_night




    return

label tuco_presentation_day:
 
    show tati neutral
 
    tati "(I think if I go right now while everyone’s busy, no one will notice me…!)"
    tati "(Let’s go!!) "
 
    #slide tati out really fast
    #fade out
    hide tati with easeoutright
 
    scene forest_day_bg with shortfade
    play ambience forest_day_ambience
    show tati neutral at left with dissolve
    show tati neutral at center with MoveTransition(0.8) 
 
    tati "Wow… This is scary - and exciting! "
    tati "Ok… Where do I begin? Where do I even go… "
    tati @ mask "So, if I found it near here, it must be this way-"
    stop music
    #slide Tuco in
    play music tuco_theme
 
    show tuco neutral at right with easeinright
    tuco "Greetings, my dear child!"

 
    show tati surprised at left with MoveTransition(0.3)
    tati "Wah!! You scared me!!"
    tuco "Oh, forgive me! It wasn’t my intention to startle you!"
    tuco "What are you looking for, walking alone in the forest? What is it you have on your hands?"

    show tati neutral
    tati "Oh, I’m just curious! I’m from a tribe not very far from here. I found this mask and I don’t know what it means…"
    tuco "I see... First time questing through the wilds, if I dare to presume? Judging by the mask you wear, I mean."
    tati @ surprised "(The mask i wear? what is he talking about?)"
    tati "Yeah… I don’t know where to start to be honest. Just thought of returning this mask I found back to where it belongs."
    tuco @ talking "Then let me tell you something, my dear…"
    tuco @ talking "There are many lives and forms to be discovered around here and too many places to be explored… Know that if you be brave, nothing can ever stop you."
    tuco @ talking "The place you seek is far ahead, through the woods. It’s very well hidden."
    tati @ surprised "(This bird seems very wise! I’m happy he’s helping me out!)"
    tati "So I just need to go that way? I hope I don’t get lost though..."
    tuco "Don’t worry dear…"
    tuco @ talking "Like I said, courage will keep you on track."
    tuco "I’m sure you will find the answers you seek once you get there. "
    tati "(The answers I seek…)"
    tati "Thank you! How should I call you Mr.?"
    tuco "I’m Tuco, a pleasure to meet you, my dear. But now I should be going. I need to meet with my family soon!"
    tati @ neutral "That’s fine! Thank you for the advice!! Hope we meet again!"
    tuco "Me too! ~"
 
    stop music fadeout 2

    hide tuco neutral with easeoutright
 
 
    tati @ neutral "What a nice guy… I feel so much better now. Let’s head on through the forest!"
 
    #play sound steps
 
    #fade out screen 
    #fade in screen
    scene black with shortfade
    scene forest_day_bg with shortfade
    show tati neutral at left with dissolve

    tati @ neutral "This is so cool! Look at all these new fruits! Flowers! Leaves! Even that weird looking flying guy! "
    tati @ neutral "Oh…! "
 
    jump first_jaguar
    return

label tuco_presentation_night:
 
    show tati neutral
 
    tati "(Okay, I’ll wait ‘til it’s nightime. It’s probably better since everyone will be sleeping!)"
 
 
    #slide tati out really fast
    #fade out
 
    scene forest_night_bg with shortfade
    play music forest_day_ambience
    show tati neutral at left with dissolve
    show tati neutral at center with MoveTransition(0.8) 
    
 
    tati "Wow… This is scary - and exciting! "
    tati "Ok… Where do I begin? Where do I even go… "
    tati @ mask "Hmmm, if I found it near here, it must be this way-"

    #slide Tuco in
 
    play music tuco_theme

    show tuco neutral at right
    show tati neutral at left

    show tuco neutral at right with easeinright
    tuco "Greetings, my dear child!"

 
    show tati surprised at left with MoveTransition(0.3)
    tati "Wah!! You scared me!!"
    tuco "Oh, forgive me! It wasn’t my intention to startle you!"
    tuco "What are you looking for, walking alone in the forest? What is it you have on your hands?"

    show tati neutral
    tati "Oh, I’m just curious! I’m from a tribe not very far from here. I found this mask and I don’t know what it means…"
    tuco "I see... First time questing through the wilds, if I dare to presume? Judging by the mask you wear, I mean."
    tati @ surprised "(The mask i wear? what is he talking about?)"
    tati "Yeah… I don’t know where to start to be honest. Just thought of returning this mask I found back to where it belongs."
    tuco @ talking "Then let me tell you something, my dear…"
    tuco @ talking "There are many lives and forms to be discovered around here and too many places to be explored… Know that if you be brave, nothing can ever stop you."
    tuco @ talking "The place you seek is far ahead, through the woods. It’s very well hidden."
    tati @ surprised "(This bird seems very wise! I’m happy he’s helping me out!)"
    tati "So I just need to go that way? I hope I don’t get lost though..."
    tuco "Don’t worry dear…"
    tuco @ talking "Like I said, courage will keep you on track."
    tuco "I’m sure you will find the answers you seek once you get there. "
    tati "(The answers I seek…)"
    tati "Thank you! How should I call you Mr.?"
    tuco "I’m Tuco, a pleasure to meet you, my dear. But now I should be going. I need to meet with my family soon!"
    tati @ neutral "That’s fine! Thank you for the advice!! Hope we meet again!"
    tuco "Me too! ~"

    stop music fadeout 2

    hide tuco neutral with easeoutright
 
    tati @ neutral "What a nice guy… I feel so much better now. Let’s head on through the forest! It’s a long way."
 
    #play sound steps
    scene black with shortfade
    #fade out screen 
    # fade in 
 
    scene forest_day_bg with shortfade

    show tati neutral at left with dissolve
 
    tati "This is so cool! Look at all these new fruits! Flowers! Leaves! Even that weird looking flying guy! "
    tati @ surprised "Oh…!"
 
    jump first_jaguar
    return

label first_jaguar:
 
    # scene forest_day_bg with shortfade
    play ambience forest_day_ambience
    play music xeni_theme
    #slide tati to left
    show tati neutral at left
    show xeni neutral at right with dissolve


    tati @ surprised "(Oh my! She’s fierce! She’s staring at me though…) "
    xeni "What do you want? "
    tati @ surprised "Oh, nothing. I’m just passing by…"
    tati "(Geez… She’s not in a good humour maybe…)"
    xeni "Passing by, huh? Can I give you some advice? "
    tati "Of course! I just met this guy who also advi- "
    

    #flash screen
    show xeni angry with flash
    xeni "Give up."
    tati @ surprised "...What?"
    xeni "I know what you’re trying to do. Been there, done that. You’re weak. Go back home."
    tati upset "I’m weak…?"
    xeni "Trust me, you’ll be glad you did. "
    #slide xeni out
    hide xeni with easeoutright

    stop music fadeout 2 #esse fade out n ta funcionando

    play ambience forest_day_ambience

    show tati upset at left

    tati "That was… really rude of her…"
    tati "So I’m not gonna make it? Should I go home and just give up…?"
    tati "I’m really just the boring little me after all…"

    menu:
        "Keep going!":
            jump keep_going
        "Return home.":
            jump return_home



    return

label keep_going:

    scene forest_day_bg
    play ambience forest_day_ambience
    show tati neutral at left

    tati "No… I shouldn’t think about that girl. "
    tati "I’ll keep Tuco’s words in mind. He said I just needed to be brave. That’s what I’ll do."

    jump forest_fire
    return

label return_home:

    scene forest_day_bg
    play ambience forest_day_ambience
    show tati upset at left

    tati "Yeah...I think it’s better for me to head back home. "
    tati "She’s right after all… I’m scared and weak. I shouldn’t even have left my home…"
    tati "Let’s just go back… "


    scene black with shortfade
    scene forest_day_bg with shortfade
    # fade out
    # fade in 
    show tati upset at left with dissolve
    tati @ surprised "I’m… lost!!! "
    tati "Everything is the same around here, how will I ever find my way home?"
    tati "Ugh, why did I decide to leave the village at all?!"
    #shake screen 
    jump forest_fire
