# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define blondie = Character('Blondie', color="#e1e823")
define glasses = Character('Glasses', color="#785f24")
define raven = Character('Raven', color="#6b4b64")
define birthday = Character('Brown Haired Birthday Girl', color="#2e0c85")
define homely = Character('Homely', color="#d62d2d")
define sb = Character('Storybro', color="#055000")
define Me = Character('Me', color="#005500")

# Declare Images used by this game.
image bg sleepy = "overslept.jpg"
image woody girl = "Princess Woody.jpg"
image woody boy = "the lewd king.jpg"
image heart = "Heart.png"
image frogbro = "forever.jpg"

# The game starts here.
label start:
    scene bg sleepy
    sb "Yikes! you overslept!"
    sb "Hello! sorry to keep you waiting!"
    sb "Welcome to the world of magically lewd adventures!"
    sb "My name isn't important, but people call me the Story Bro"
    sb "This world is inhabited by creatures that we call 'Women'"
    sb "People and Women live together by supporting each other."
    sb "Some people play with Women"
    sb "Some Battle with them"
    sb "But we don't know everything about Women yet."
    sb "There are still many mysteries to solve."
    sb "That's why i study Women every day."
    sb "Now Tell me, are you a boy? Or are you a girl?"
    
    menu:
        "BOY":
            jump startboy
        "GIRL":
            jump startgirl

            
            
            
label startboy:
    show woody boy
    sb "Now, what did you say your name was?"
    
    menu:
        "RED":
            jump startred
        "BLUE":
            jump startblue
        "YELLOW":
           jump startyellow
        "DICKS":
           jump startdicks
           
           
label startred:
    sb "RED, are you ready?"
    jump startm2
    
label startblue:
    sb "BLUE, are you ready?"
    jump startm2
    
label startyellow:
    sb "YELLOW, are you ready?"
    jump startm2
    
label startdicks:
    sb "DICKS, are you ready?"
    jump startm2

    
    
    
label startgirl:
    show woody girl
    sb "Now, what did you say your name was?"
    
    menu:
        "RED":
            jump startfred
        "BLUE":
            jump startfblue
        "YELLOW":
           jump startfyellow
        "CUNTS":
           jump startcunts
           
           
label startfred:
    sb "RED, are you ready?"
    jump startf2
    
label startfblue:
    sb "BLUE, are you ready?"
    jump startf2
    
label startfyellow:
    sb "YELLOW, are you ready?"
    jump startf2
    
label startcunts:
    sb "CUNTS, are you ready?"
    jump startf2
 
 
label startm2:
    sb "Your very own 'Women' story is about to unfold"
    sb "You'll face fun times, and tough challenges"
    sb "A world of dreams and adventures with Women awaits! Let's Go!"
    jump startm3

label startf2:
    sb "Your very own 'Women' story is about to unfold"
    sb "You'll face fun times, and tough challenges"
    sb "A world of dreams and adventures with Women awaits! Let's Go!"
    jump startf3
    


label startm3:
    sb "You grew up as an awkward. Somewhat nerdy, but generally likeable guy"
    sb "Unluckily, you're not much of a hit with men, you've grown up around women your entire life"
    sb "Not that you mind"
    sb "Early teenage years, this came with its perks. You ended up in an anime/video games club"
    sb "The two always went together back then, and in your early teenage years you spent most of your lunchtime watching naruto and playing smash all day"
    sb "Which was pretty awesome at the time"
    sb "One of them, decides to throw a birthday party and invite everyone"
    sb "Yes, that includes you!"
    sb "She rents a limo, it's five girls in the car, another guy and you."
    sb "You all pretty much spend the day eating delicious food, driving around town, playing vidya on the limo's TV and just generally do cool shit all day"
    sb "End of the day comes though"
    sb "The girls are planning a sleepover"
    sb "Lucky for you, your best friend (Female) is in the car, and she's decided you're invited"
    sb "Well, it had a good amount of begging and pleading with the birthday girl, but eventually she turns to you"
    birthday "If your best friend vouches for you, you can hang out the night if you want?"
    birthday "As long as you can get your parents to agree?"
    birthday "What do you say?"
    
    menu:
        "Sure! I'd love to join ya'll":
            jump startm4
        "I'd better not, my parents want me home for dinner":
            jump FROG_END
            
label startf3:
    sb "You grew up as an awkward. Somewhat nerdy, but generally likeable gay"
    sb "Unluckily, you're not much of a hit with men, you've grown up around women your entire life"
    sb "Not that you mind"
    sb "Early teenage years, this came with its perks. You ended up in an anime/video games club"
    sb "The two always went together back then, and in your early teenage years you spent most of your lunchtime watching naruto and playing smash all day"
    sb "Which was pretty awesome at the time"
    sb "One of them, decides to throw a birthday party and invite everyone"
    sb "Yes, that includes you!"
    sb "She rents a limo, it's five other girls in the car, another guy and you."
    sb "You all pretty much spend the day eating delicious food, driving around town, playing vidya on the limo's TV and just generally do cool shit all day"
    sb "End of the day comes though"
    sb "The girls are planning a sleepover"
    sb "You're invited"
    birthday "Come on! It wouldn't be the same without you staying over!"
    birthday "Your parents are sure to agree!"
    birthday "What do you say?"
    
    menu:
        "Sure! I'd love to join ya'll":
            jump startf4
        "I'd better not, my parents want me home for dinner":
            jump FROG_END
    
            
label FROG_END:
    scene frogbro
    sb "You say your goodbyes, smile and wave to the girls as you step out of the car"
    sb "Your mother will be here in fifteen minutes to pick you up"
    sb "You're having spaghetti for dinner"
    sb "I hope it's worth it"
    "FROG_END"
    return


    
label startf4:
    sb "You agree to the sleepover, why not right?"
    sb "Friends are more important than spaghetti anyway"
    sb "plus it's been ages since you've been to a sleepover"
    sb "However... one problem"
    sb "Your best friend, the blonde haired boy..."
    sb "well it might be awkward to bring him to an ALL GIRLS sleepover"
    sb "But then again he does everything with you, and he's quite harmless"
    sb "You've known him for six years and he's never made much of a move on anyone, he has to be right?"
    sb "Begging and pleading, you manage to convince the birthday girl that he is a MUST HAVE and it wouldn't be the same without him"
    sb "The others seem to agree, and he's quickly roped into your sleepover plans"
    sb "You figure you can just tell the birthday girl's parents he's gay. That always works"
    jump female_end

label startm4:
    sb "You agree to the sleepover, why not right?"
    sb "The other guy doesn't seem to think so, he's either not invited or he has to go home for dinner"
    sb "Friends are more important than spaghetti anyway"
    sb "plus it's been ages since you've been to a sleepover"
    sb "Your best friend, the black haired girl. She pretty much convinces them you have to come with"
    sb "So this'll be interesting you think, as the limo pulls up to the lawn of the birthday girl's house"
    jump male_end
            
label female_end:
    scene heart
    "THE RIDE NEVER ENDS, except here... M'lday"
    
label male_end:
    scene heart
    "THE RIDE NEVER ENDS, except here"