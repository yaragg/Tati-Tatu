image ritual_chars:
    contains:
        "images/character/tuco ritual.png"
        xalign 0.2
        linear 0.5 xalign 0.1
        linear 0.9 xalign 0.3
        linear 0.5 xalign 0.2
        repeat

    contains:
        "images/character/tati ritual.png"
        xalign 0.5
        linear 0.5 xalign 0.4
        linear 0.9 xalign 0.6
        linear 0.5 xalign 0.5
        repeat

    contains:
        "images/character/yara ritual.png"
        xalign 0.8
        linear 0.5 xalign 0.7
        linear 0.9 xalign 0.9
        linear 0.5 xalign 0.8
        repeat

label forest_fire:
    scene forest_day_bg 
    # Tati smells the air and looks confused.

    show tati confused at center
    play ambience forest_fire_ambience
    tati "(Sniff, sniff… What’s this smell? It’s like lightning struck a tree.)"
    tati @ surprised "(But… worse.)"

    # Move Tati sprite to the right across the screen. Fade out screen.

    show tati neutral at center
    tati "(I can smell it. It’s right…)"
    show tati horrified
    tati "(...There.)"

    scene forest_fire_bg
    stop ambience
    stop music
    play music forest_fire
    play ambience heavy_fire_ambience
    show tati scared at left
    tati "Oh… Oh no. Oh no."
    tati "It’s on fire! I… I gotta run!"

    show tati scared
    # Make Tati face left of screen. Move slightly to the left as if she were leaving, then stop just at the edge of the screen.

    yara "Wait!"
    tati "What was that?!"
    # Make Tati face right.
    yara "Over here! I’m stuck! I-I need help! Please!!"

    scene fire_bg_with_yara1
    tati "Oh no! I’ll help, hold on!"
    # Move Tati towards the right of the screen, but stop. Flash screen white and red, shake screen.
    #play sound log_falling
    tati "Ahhh!!"
    show tati ball at left 
    tati "(That burning log almost landed on me! I almost {i}died!{/i})"
    tati "(I gotta run, I gotta run!)"
    tati "(What am I even doing here? We armadillos only ever run. We don’t fight, that just gets you killed. What can I even do against a wildfire?)"
    tati "(It’s the way it’s always been. Curl up, run, burrow. I need to go before the fire gets me too!)"
    tati "(But…)"
    yara "Heeeelp! It’s closing in!"
    # shake screen
    tati "(She’ll die if I leave her! But if I stay I’ll die too! What do I do?!)"

    menu:
        "Try to save her and risk it all":
            jump save_yara
        "Run and save yourself":
            jump not_save_yara






    return

label save_yara:
    show tati confused
    tati "(I have to save her! What kind of girl am I if I just run and save myself?)"
    tati "(Running is what people back home would do. I left so I could be my own self!)"
    tati "(Okay... Let's cross the fire and get to her!)"


    tati "Yaaaaaaahhh!!"
    # Quickly move Tati across screen.
    show tati neutral
    tati "(I did it! I made it without getting hit by anything!)"
    tati "(Hey, you! What happened?!)"
    yara "I was running but then this tree fell and I--I--Gmmrg! I can’t get my paw free!"
    tati @ surprised "Alright... My, my, what can I do?!!"
    tati "(Aha! Maybe I can dig a hole under the tree and get her free that way!)"

    # Move Tati back and forth like she’s digging.
    tati "There you go!"
    # Move Yara up like she’s springing free.

    yara "Oh my ancestors I thought I was gonna die thank you thank you so much--"
    # Flash screen red and shake again.
    tati @ ball "Eep! Come on, we need to leave!"
    # Move Yara and Tati left out of the screen.
    
    scene forest_fire_bg
    show tati surprised at left
    tati "Look at all those flames… It’s awful. Is it just going to keep spreading?"
    show yara scared at right
    yara "Probably. I hope it won’t reach my village…"
    tati @ upset "(That’s right! What if it reaches home? Oh no…)"
    tati "We have to put the fire out!"

    yara @ surprised "What? But how?"
    tati "Fire needs wood to spread, right? What if we cut down the trees around it so it can’t spread?"

    show yara neutral
    yara "That’s pretty crazy…"
    tati @ neutral "We have to try!"

    # Move Tati back and forth.
    #play sound shoving
    tati "Mmmmmmrmrrgh! I… can’t…! Why is this thing so sturdy?!"
    yara "We’re not going to pull this off. We’re not big or strong enough…"
    tati "But… But we can’t just do nothing! "
    tati "(But she’s right, we’re not strong enough. Is there some other way we can do this? What do we do…?)"

    tuco "Tati! "
    # Move Tati like she jumped in surprise.
    tati @ surprised "Ahh! What? Who?"
    tati @ happy "Oh! it’s you!"

    show yara at center
    show tuco scared at right
    tuco "What in the world are you doing here? It’s dangerous!"
    tati "We’re trying to put out the fire. But I don’t know what to do!"
    tuco @ surprised "Ah. That’s…"

    show tuco neutral
    tuco "Alright. There are three of us… Perhaps we can make this work."
    tuco "I know of an old ritual for calling rain from the heavens."
    tati @ surprised "What?! That’s amazing! Tuco, we need to do this!"
    tuco "Calm yourself, child. First, we need to go the highest spot we can find around here."

   
    show yara happy
    yara "Oh! I know where! There’s a hill right over there."
    tati "Alright, let’s go!"

    stop music fadeout 3
    stop ambience fadeout 3

    scene black with mediumfade

    # Fade out screen.
    # Fade in forest bg
    scene forest_day_bg with mediumfade
    play music forest_day_ambience
    show tuco talking at right
    show yara happy at center
    show tati neutral at left
    tuco "Now, let’s do as I said. You both remember the dance, yes?"
    tati "Yeah!"
    yara "Let’s do this!"
    hide tuco
    hide yara
    hide tati
    # show tati ritual at left
    # show tuco ritual at center
    # show yara ritual at right
    play music ritual
    show ritual_chars
    
    $ renpy.pause(5)
    hide ritual_chars with dissolve
    play ambience rain_ambience

    # Animate all three of them swaying back and forth
    # Wait a while
    #play sound rain
    # Flash screen light blue twice
    show rain with dissolve
    show tati surprised at left with dissolve

    tati "We… We did it. It actually worked!"
    show tuco neutral at right 
    tuco "Of course it did. When have I ever led you astray?"
    show yara happy at center
    yara "Oh, look! Down there! The flames are dying down!"

    stop music

    show tati neutral
    tati "This is amazing. We really saved the woods!"
    
    play music menu_theme_ingame
    tati "(This… feels good. I like this. I like the person I’m becoming.)"

    yara @ surprised "Hey… I didn’t get the chance to ask before, but why are you wearing a mask?"
    tati @ surprised "Eh? Mask? what are you talking about?"
    yara @ neutral "Nevermind. I think you’ll understand what I mean someday."

    tuco @ talking "Tati, Yara, what you two did was very brave. The fire could have reached any village around here… So many people could have been killed."

    show tati neutral
    tati "I know. I… I wanted to run, at first. That’s what my people have always done. But… I’m glad I didn’t. Maybe running really isn’t always the answer."
    tati "(Maybe… Maybe not everything I learned back home is right.)"
    tati "(I did my own thing, for once. And it worked out. It was a huge risk, but I’m happy I took it.)"
    tati @ happy "Oh! but you helped out lots too, tuco. Thank you so much for the ritual!"
    tuco @ happy "I’m just glad we managed to make it work. I honestly don’t think I would have faced the flames by myself… you inspired me, tati. i saw how you helped yara here."
    tati @ happy "Thank you…"
    tati @ happy "(I’m so embarrassed I don’t even know what to say. He’s so wise. Did I really inspire him?)"
    tuco "Yara, I will fly you--well, walk you back to your village. Tati, do you know where you’re headed?"
    tati @ happy "Yeah! That way, right? "
    tuco "Yes. You have a good sense of direction. Well then… Good luck, dear. I’m sure you will find what you’re looking for."
    tati @ neutral "Yeah… I hope so."

    stop music fadeout 3
    stop ambience fadeout 3
    scene black with mediumfade

    # Fade out
    # Fade in
    scene forest_day_bg with mediumfade
    show tati neutral at left
    play ambience forest_day_ambience

    tati "(It’s probably around here somewhere. I should be alright.)"

    show xeni neutral at right with dissolve
    # Xeni slides on the scene 

    tati "(...or not)"

    play music xeni_theme

    xeni "Hey… Hello. "
    tati "Hi. "
    tati "(Wow. She’s trying to be nice for once)."
    xeni "I was passing by and I saw you with those two. I saw what you did for the forest."
    xeni "It was very brave of you. And I should say… I’m sorry. For what I said earlier. "
    tati "Oh. It’s okay…"
    xeni "No it isn’t. I projected myself on you and for that I’m sorry."
    xeni "I once was just like you… I still had a mask on, started roaming the wilds by myself, didn’t have much on my mind. And it cost me my eye. "
    tati "No way! I’m sorry to hear that… Must have been hard."
    xeni "It was… The wilds are dangerous. It’s an act of sheer courage to decide living here and discovering the world around us. "
    xeni "Anyways… I misjudged you. You’re not weak nor incapable. You did even more than I ever dared doing. "
    tati "That’s really kind of you...Mrs.?"
    xeni "Call me Xeni. "
    tati "Xeni, then. When I decided to leave the village I never thought I’d get this far. I made friends, I learned a lot. It’s risky... but I feel like it’s worth it. "
    xeni "It sure is. I’m living proof of it."

    show xeni happy
    xeni "Are you still looking for that village? It’s just around here. I can go with you if you want and show you the way."
    tati "Yes!!! Thanks Xeni! I’m really excited to get there! "
    xeni "Haha! Let’s go then!"
    hide xeni with dissolve
    tati "(That was really nice of her. And the things she said about me... I’m very happy. I think I never thought of myself as brave or anything like it... )."

    stop music fadeout 3

    # fade out screen and characters
    # fade in floresta_densa_dia

    show xeni happy at right
    xeni "Well, we’re almost there. I’ll leave you to it, since I don’t think they will see a scarred eye jaguar as a friendly neighbor."
    tati "No worries! Thanks for coming… let’s meet again soon!"
    xeni "Sure! See you around. "

    hide xeni with dissolve
    #sllide xeni out

    tati "Well, here I go! "

    # fade in aldeia 2
    scene village2 with dissolve
    show tati confused at left

    tati "…"
    tati "Oh… That is… Familiar…"
    tati @ mask "So this is where you belong little mask. This is the place. "
    tati "Well, what was I even expecting? It’s seems just like my village. Except for the roofs' shape. "
    tati "Even people: they have the same faces. The same… bored and conformed faces."
    tati "Do I still belong in a place like this…? "
    tati "…No."
    tati @ surprised "I don’t want this anymore. "
    tati "I’m a different person now. I feel like I know who I am…"
    tati "I feel like I’m able to rattle the stars if I wanted to… "
    tati "I finally understand what Tuco, Xeni and Yara said."

    #fade out screen 

    # scene mirror_cutscene with slidedown
    # show mirror_cutscene:
    #     xpos 0
    #     ypos 0
    #     linear 5.0 ypos 
    scene black with shortfade

    window hide
    $ renpy.pause(0.3)


    show mirror_cutscene with shortfade:
        yalign 0.0
        linear 8.0 yalign 1.0
    play music good_end
    $ renpy.pause(9.0)

    # hide characters
    #slide down cutscene

    tati "This is me. The real me. "
    tati "After all I’ve been through, all I shared and achieved, today and even all the other days, this is what I’ve become. "
    tati "And I…"
    tati "I really love it. "
    $ renpy.pause(1)
    window hide
    show text "GOOD END"
    $ renpy.pause(2)
    scene black with longfade
