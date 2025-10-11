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
define b = Character("Child")
define fa = Character("Flight attendant")
define c = Character("Captain")
define ssd = Character("Ship victim")
define unknown = Character("???")

image bg whale = im.Scale("images/whale.png", 1920, 1080)
image bg outsideboat = im.Scale("images/outsideboat.png", 1920, 1080)
image bg roomonship = im.Scale("images/roomoneship.png", 1920, 1080)
image bg venuedoors = im.Scale("images/venuedoors.png", 1920, 1080)
image bg airport = im.Scale("images/airport.png", 1920, 1080)
image bg daydreamcity = im.Scale("images/daydreamcity.png", 1920, 1080)
image bg lifeboat = im.Scale("images/lifeboat.png", 1920, 1080)
image bg boardinglifeboat = im.Scale("images/boardinglifeboat.png", 1920, 1080)
image bg bedroom = im.Scale("images/bedroom.png", 1920, 1080)
image bg airplane = im.Scale("images/airplane.png", 1920, 1080)
image bg rm1 = im.Scale("images/rm1.png", 1920, 1080)
image bg trolley = im.Scale("images/trolley.png", 1920, 1080)
image bg rm2 = im.Scale("images/rm2.png", 1920, 1080)
image bg rl2 = im.Scale("images/rl2.png", 1920, 1080)
image bg rg2 = im.Scale("images/rg2.png", 1920, 1080)

image bg t2 = im.Scale("images/t2.png", 1920, 1080)
image bg rbm2 = im.Scale("images/rbm2.png", 1920, 1080)
image bg cm1 = im.Scale("images/cm1.png", 1920, 1080)
image bg cm2 = im.Scale("images/cm2.png", 1920, 1080)

image bg mb1 = im.Scale("images/mb1.png", 1920, 1080)
image bg mb2 = im.Scale("images/mb2.png", 1920, 1080)

image bg b1 = im.Scale("images/b1.png", 1920, 1080)
image bg b2 = im.Scale("images/b2.png", 1920, 1080)

default choice = "mandies"

label start:

    stop music fadeout 1.0

    "Your nearest Daydream event is starting tomorrow. You’re all packed, and now you just need to get to your flight."

    "Unfortunately, the venue is extremely far away. Your local airport doesn’t offer direct flights to the location, so you now must embark on an irritatingly long journey."

    "The first stop? The trolley."

    scene bg bedroom

    play music "audio/alarm.mp3"

    y "Shoot. My alarm was an hour late… I’ve got to hurry."

    stop music fadeout 1.0

    "You throw in your airpods and get ready for your day."

    play music "yippee.mp3"

    scene black with fade

    pause 1.0

    scene bg trolley

    y "Where’s the schedule? Ugh… I might miss my flight at this rate."

    unknown "Help!!"

    "You peer down to see the tracks."

    scene bg rm2

    rm " I’ve been tied to the tracks - a trolley is coming soon. Go get help! QUICK!"

    y "Well uhh, I don’t know man. I’ve got to catch that trolley, you know?"

    rm "PLEASE! Please help!"

    y "Uhh… okay, hold on, let me think."

    unknown "No! What are you doing?"

    unknown "Yeah! Help US!"

    "You slowly turn to see the other branch of the train track. And there lies… four people."

    y "Alright, what the flip."

    "Well well well. NOW what will you do?"

    scene bg rg2

    rg "There’s a lever there! Right to your left!"

    scene bg rl2

    rl "HURRY UP!!"

    y "Okay, okay, I get it! Gosh."

    "You turn. Currently, the trolley is on track to kill the man."

    y "Uh. I’ve got some really bad news for you."

    rm "Please!! Pull the lever! I’m begging you… I have a family… They need me."

    rl "NO! We have lives too!! Please don't redirect it! I have six… wait, no, seven mouths to feed at home."

    y "Haha… like… six seven?"

    y "Well, I think I should hear all of you out…"

    "You walk to see each one of them. That seems like the right thing to do. You wouldn’t want to save a bad person, would you?"

    scene bg t2

    t "Come on... One person is a small sacrifice to make… just be logical…"

    scene bg rl2

    rl "Please… think of my kids… they need me."

    scene bg rg2

    "The random girl appears to have passed out from fear. Not really helping her case."

    scene bg rbm2

    rbm "My company is working to develop a cure for a highly contagious disease. If I die, things will fall apart..."

    scene bg trolley

    y "Okay, convincing. Now, your turn. Why do you think I SHOULD switch the lever?"

    scene bg rm2

    rm "My daughter… She's my whole world. Please. I don’t want to die…"

    y "Hm, this is lowkey kind of difficult to decide."

    "The sounds of the trolley are getting closer and closer."

    "If you don't push the lever, one man dies. If you do not, four people die. Will you push the lever?"

menu(time=7, timeout="mandies"): 
    "No":
        jump mandies

    "Yes":
        jump fivedies
        $ choice = "fivedies"


label mandies:

    scene bg trolley

    "You don’t touch the lever."

    "Four people have been saved, at the cost of one precious human life."

    "Your trolley arrives, finally. You’re not even late! #vacationgoals"

    scene black with fade

    jump lifeboat

label fivedies:

    scene bg trolley

    "You pull the lever."

    "Four people have lost their lives."

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

    scene bg outsideboat

    "You go outside. People are yelling, water is rising below your feet."

    scene bg cm1

    cm "There is one safety boat, it holds five people, and we are seven. We are too far from the shore for anyone to swim back, and help will be here in an hour. The water is too cold to be in for that long."

    "You are faced with a choice. Two people will lose their lives. It is your choice who loses their lives."

menu(time=7, timeout="savednoone"):

    "Save one person":
        jump saveperson

    "Save yourself":
        jump saveyourself

label savednoone:

    scene black with fade

    scene bg whale

    "You did nothing, and drowned."

    jump death 

label saveperson:

    scene black with fade

    scene bg whale

    "Your bravery has helped one person reach their loved ones safely. On the other hand, you do not know how to swim, so you lose your life with water in your lungs."
    
    "So... yeah. You're not getting to Daydream."

    jump death

label saveyourself:

    scene black with fade

    scene bg lifeboat

    "You get on the lifeboat, and two people have lost their lives."

    show cm2

    cm "Help is on the way, remain where you are."

    hide cm2

    jump airport

label airport:

    scene black with fade

    scene bg airport

    "You get help, and reach where you were going just in time to catch your flight."

    scene black with fade

    scene bg mb1

    "Oh my goodness why is my seat next to a kid?? If it starts crying… I might not make it to Daydream… or home …. for a while…"

    m "I have to use the restroom. Can you please look after him? It will be less than 5 minutes, I promise."

    y "Yeah, sure!"

    scene bg b1

    y "Good now it’s crying."

    scene black with fade

    scene bg b1

    "Two minutes have passed, and she is still in the restroom."

    "The cabin is filled with smoke."

    fa "Everyone please remain calm. As instructed before, all adults please help yourself to a mask, then help children and others around you."

    y "Where is this thing’s mom?"

    y "What do I do with it?"

menu(time=7, timeout="masknoone"):

    "Help the child":
        jump maskchild

    "Help yourself":
        jump maskyourself

label masknoone:

    "You didn't help yourself or the child with your masks. You both died because of the smoke."

    jump death

label maskchild:

    "Your brave act has saved the child, but you have lost your life in the process."

    jump death

label maskyourself:

    scene bg b2

    "When you turn to help the child, you find that it is too late."

    "They have died of smoke inhalation."

    scene bg mb2

    m "*screams*"

    fa "The cabin has been cleared of smoke, and we will continue with our flight as usual."

    c "We have successfully landed. Thank you for choosing Air Hackclub."

    scene black with fade

    scene bg daydreamcity

    "You have made it to the city where your DayDream is hosted. You now leave to make it there on time."

    scene bg venuedoors

    "..."

    "But you have made some tragic choices."

    jump end

label end:

    scene black

    scene bg idk

    play music "audio/ending.mp3"

    scene black with fade

    if choice == "mandies":

        rm "My daughter had such a bright future that I wished I could’ve seen. Maybe she could have been an artist, pilot, engineer, chef, or scientist. All I can hope is that the family that adopts her is good to her."

    elif choice == "fivedies":

        rg "My parents never cared much for me and my siblings. As the eldest, I was the one who took care of them. Because I never came home, they’re now stuck in that household with no one to take care of them for another decade."

        rl "We never got to celebrate our first anniversary… it had always been my dream to start a family. Maybe it wasn’t meant to be."

        t "My students were going to give me a goodbye party because I have deadly cancer. Now they will never see me for the last time to say their last goodbyes."

        rbm "Thousands of elderly people worldwide could have benefitted from the cures we were working on. But now… there’s not much that can be done."

    ssd "With your selfish choice, I was eaten by a whale. I now cannot go home to start college. My parents also lost their only child, who they gave everything to give an education to."

    m "My husband has committed suicide because he lost me and his son in the same flight. His parents now suffer in the retirement home because there is no one to help them survive financially."

    b "I was going to find out how we stop pollution worldwide, saving many in large cities from dying of air pollution."

    "Well."

    "That's really something, isn't it?"

    "Our actions really do have consequences, don't they?"

    jump death

label death:

    stop music fadeout 1.0

    scene black with fade

    play music "audio/shouldn't you be asleep.mp3"

    "Thank you for playing."

    scene black with fade

    return


