# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define rm = Character("Random man")
define rg = Character("Random girl")
define rl = Character("Random lady")
define t = Character("Teacher")
define rbm = Character("Rich business man")
define cm = Character("Crew member")
define m = Character("Mother")
define b = Character("Baby")
define fa = Character("Flight attendant")
define c = Character("Captain")


define unknown = Character("???")


# The game starts here.

label start:

    "Your nearest Daydream event is starting tomorrow. You’re all packed, and now you just need to get to your flight."

    "Unfortunately, the venue is extremely far away. Your local airport doesn’t offer direct flights to the location, so you now must embark on an irritatingly long journey."

    "The first stop? The trolley."

    scene bg bedroom

    play sound "audio/alarm.mp3"

    y "Shoot. My alarm was an hour late… I’ve got to hurry."

    stop sound

    "You throw in your airpods and get ready for your day."

    scene black with fade

    pause 1.0

    scene bg trolleystop

    y "Where’s the schedule? Ugh… I might miss my flight at this rate."

    unknown "Help!!"

    "You peer down to see the tracks."

    rm " I’ve been tied to the tracks - a trolley is coming soon. Go get help! QUICK!"

    y "Well uhh, I don’t know man. I’ve got to catch that trolley, you know?"

    rm "PLEASE! Please help!"

    y "Um… okay, hold on, let me think."

    unknown "No! What are you doing?"

    unknown "Yeah! Help US!"

    "You slowly turn to see the other branch of the train track. And there lies… five people."

    y "Alright, what the flip."

    "Well well well. NOW what will you do?"

    rg "There’s a lever there! Right to your left!"

    rl "HURRY UP!!"

    y "Okay, okay, I get it! Gosh."

    "You turn. Currently, the trolley is on track to kill the five people."

    y "Uh. I’ve got some really bad news for you guys."

    rm "Please!! Don't pull the lever! I’m begging you… I have a family… They need me."

    rl "NO! We have lives too!! Please redirect it! I have six… wait, no, seven mouths to feed at home."

    y "Haha… like… six seven?"

    y "Well, I think I should hear all of you out…"

    "You walk to see each one of them. That seems like the right thing to do. You wouldn’t want to save a bad person, would you?"

    t "Come on, man. One person is a small sacrifice to make… just be logical…"

    rl "Please… think of my kids… they need me."

    "The random girl appears to have passed out from fear. Not really helping her case."

    rbm "My company is working to develop a cure for a highly contagious disease. If I die, things will fall apart..."

    y "Okay, convincing. Now, your turn. Why do you think I SHOULD switch the lever?"

    rm "My daughter… She's my whole world. Please. I don’t want to die…"

    y "Hm, this is lowkey kind of difficult to decide."

    "The sounds of the trolley are getting closer and closer."

    "Will you push the lever?"

menu: 

    "Yes":
        jump mandies

    "No":
        jump fivedies

label mandies:

    "You don’t touch the lever."

    "Five people have lost their lives."

    "Your trolley arrives, finally. You’re not even late! #vacationgoals"

    scene black with fade

    jump lifeboat

label fivedies:

    "You pull the lever."

    "Five people have been saved, at the cost of one precious human life."

    "Your trolley arrives, finally. You’re not even late! #vacationgoals"

    scene black with fade

    jump lifeboat

label lifeboat:

    "You must now take a ship to reach your flight"

    scene bg roomonship

    "You set your stuff down, and take a nap."

    scene black with fade

    scene bg roomonship

    "It has been an hour, and you hear people shouting."

    scene black with fade

    scene bg boatoutside

    "You go outside. People are yelling, water is rising below your feet."

    scene bg safetyboat

    cm "There is one safety boat, it holds five people, and we are seven. We are too far from the shore for anyone to swim back, and help will be here in an hour. The water is too cold to be in for that long."

    "You are faced with a choice. Two people will lose their lives. It is your choice who loses their lives."

menu:

    "Save one person":
        jump saveperson

    "Save yourself":
        jump saveyourself

label saveperson:

    scene black with fade

    scene bg underwater

    "Your bravery has helped one person reach their loved ones safely. On the other hand, you do not know how to swim, so you lose your life with water in your lungs."
    
    "So... yeah. You're not getting to Daydream."

    jump death

label saveyourself:

    scene black with fade

    scene bg onthelifeboat

    "You get on the lifeboat, and two people have lost their lives."

    cm "Help is on the way, remain where you are."

    jump airport

label airport:

    scene black with fade

    scene bg airport

    "You get help, and reach where you were going just in time to catch your flight."

    scene black with fade

    scene bg airplane

    "Oh my goodness why is my seat next to a kid?? If it starts crying… I might not make it to DayDream… or home …. for a while…"

    m "I have to use the restroom. Can you please look after him? It will be less than 5 minutes, I promise."

    y "Yeah, sure!"

    "Two minutes have passed, and she is still in the restroom."

    "The cabin is filled with smoke."

    fa "Everyone please remain calm. As instructed before, all adults please help yourself to a mask, then help children and others around you."

    y "Where is this thing’s mom?"

    y "What do I do with it?"

    y "Good now it’s crying."

menu:

    "Help the child":
        jump maskchild

    "Help yourself":
        jump maskyourself

label maskchild:

    "Your brave act has saved the child, but you have lost your life in the process."

label maskyourself:

    "When you turn to help the child, you find that it is too late."

    "They have both died of smoke inhalation."

    fa "The cabin has been cleared of smoke, and we will continue with our flight as usual."

    c "We have successfully landed. Thank you for choosing Air Hackclub."

    scene black with fade

    scene bg daydreamcity

    "You have made it to the city where your DayDream is hosted. You now leave to make it there on time."

    scene bg daydreamvenue

    "But you have made some bad choices."

label death:

    scene black with fade

    return

