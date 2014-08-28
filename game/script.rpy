# You can place the script of your game in this file.

# Declare classes and persistant data
init python:
    # Subclass the internal character object to be able to store state and use the same object for
    # renpy commands.
    # The advantage of this is it allows you to reuse the same name for both say statements and
    # state; you can use both of these statements:
    #    player "Wow, sure is dark in here"
    #    $ player.scared = True
    #
    # The Character function is very simple, although it includes a lot of documentation; its
    # contents can be viewed here. https://github.com/renpy/renpy/blob/master/renpy/character.py#L871
    # The main disadvantage to this technique is loss of the ability to base characters on each other
    # through the "kind" parameter, but that's alright. We don't need it anyway.
    from renpy.character import ADVCharacter
    # define constants for boy and girl, these will be used a lot
    # because they are strings, this allows us to do things like "if player.gender is boy", which is very nice and python-y
    boy = "boy"
    girl = "girl"
   
    
    class Player(ADVCharacter):
        # **kwargs in this context means "pass keyword arguments through"
        # for more information, see http://stackoverflow.com/questions/3394835/args-and-kwargs
        def __init__(self, name, **kwargs):
            # usually, you would do super(Player, self).__init__(...), but for some reason, in this context,
            # this breaks everything. Directly using the base type works, though.
            ADVCharacter.__init__(self, name, kind=renpy.store.adv, **kwargs)
            # add state here
            self.chosen_name = "No name Jenkins" # self.name is taken for the display name
            self.gender = "???"
            
    
    class Blondie(ADVCharacter):
        def __init__(self, name, **kwargs):
            ADVCharacter.__init__(self, name, kind=renpy.store.adv, **kwargs)
            self.reputation = 0
            
    class Glasses(ADVCharacter):
        def __init__(self, name, **kwargs):
            ADVCharacter.__init__(self, name, kind=renpy.store.adv, **kwargs)
            self.reputation = 0
    
    class Raven(ADVCharacter):
        def __init__(self, name, **kwargs):
            ADVCharacter.__init__(self, name, kind=renpy.store.adv, **kwargs)
            self.reputation = 0
            
    class Birthday(ADVCharacter):
        def __init__(self, name, **kwargs):
            ADVCharacter.__init__(self, name, kind=renpy.store.adv, **kwargs)
            self.reputation = 0
            
    class Homely(ADVCharacter):
        def __init__(self, name, **kwargs):
            ADVCharacter.__init__(self, name, kind=renpy.store.adv, **kwargs)
            self.reputation = 0

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define player = Player('Me', color="#005500")
define blondie = Blondie('Blondie', color="#e1e823")
define gla = Glasses('Glasses', color="#785f24")
define raven = Raven('Raven', color="#6b4b64")
define birthday = Birthday('Brown Haired Birthday Girl', color="#2e0c85")
define homely = Homely('Homely', color="#d62d2d")
define sb = Character('Storybro', color="#055000")

# Declare Images used by this game.
#Images are no longer declared. They are now automatically parsed into assets from any jpg/png you place in the game folder.


# The game starts here.
label start:
   scene bg Overslept
   sb ">You, being the lazy bastard that you are {p}>Decide that sleep is for the weak and engage in all-night activities on your laptop {p}>Carefully taking the time to forget what day it is tomorrow  {p}>You idiot"
   show Glasses G19
   gla "!!!"
   show Glasses G2
   gla "Hey! What are you still doing in bed?"
   show Glasses G1
   gla "Don't give me that kind of look! {p} You KNEW we were going to hang out today!"
   show Glasses G3
   gla "What! Am i not important or something? {p} Get dressed already!"
   menu:
        "Get Dressed":
            $ var_blowoff = 0
            jump dressed
        "Blow her off":
            $ var_blowoff = 1
            jump blowoff
            
label dressed:
    show Glasses G11
    sb "'Fine! Fine!' {p}>You exhale as you tumble out of bed"
    show Glasses G12
    sb ">She breaks into a smile {p}... obviously glad you aren't your usual, lazy self"
    sb ">You start the long tedious process of dressing"
    sb ">So you're pretty much searching your mess of a room for anything clean to wear {p}... Which would be far easier if your room wasn't a big pile of clothing"
    show Glasses G17
    sb ">Glasses is just watching {p}...a funny little smile as she enjoys your futile search {p}... that is until you catch her eyes with yours"
    show Glasses G9
    gla "'You're such a slob!' She exclaims with laughter {p}...'One of these days we'll get blondie to teach you how she keeps her room so neat'"
    sb "You could probably ask her to help you find some pants or something if you wanted"
    
    menu:
        "Stop grinning and help me find some clean pants!":
            $ var_cleanpants = 1
            jump cleanpants
        "Continue searching quietly":
            $ var_cleanpants = 0
            jump cleanpantsquietly
    
    
    
label blowoff:
    show Glasses G4
    sb "'I don't wanna' {p}...You whine{p}...wrapping the blankets around yourself tighter"
    show Glasses G5
    sb ">Glasses Frowns {p}...You worry you might have hurt her feelings {p}...She had set aside today to spend time with you after all {p}...Worried you were both growing distant after that 'sleepover' incident"
    sb ">And you just blew the night before playing some crappy korean MMO that wasn't even that fun"
    sb ">Usually that kind of thing would be fine in Glasses' book, she would have joined and wasted time with you"
    sb ">But uhh... {p}...You kind of forgot {p}...To invite her..."
    show Glasses G21
    gla "You were up all night weren't you?"
    sb ">She caught you {p}...so you nod {p}...guiltily"
    show Glasses G23
    gla "But you were supposed to SLEEP so we could go out today!"
    show Glasses G7
    gla "I even got my mom to let me borrow the car later!"
    gla "Come on! Let's go"
    sb ">She yells while trying to pull the blankets away from you"
    sb ">You could probably resist her, you're stronger anyway, or go off to do whatever it is she wants you to do {p}...probably shopping {p}...why women think that's a male bonding experience you'll never know"
    
    menu:
        "RESIST ARREST":
            jump resistarrest
        "GO TO JAIL":
            jump paythefine

label resistarrest:
    show Glasses G22
    sb ">She struggles with you for nearly four minutes, but your superior male physique wins out"
    sb ">With a sigh, she plops her butt down near your legs in defeat"
    show Glasses G21
    sb ">She's got somewhat of a blank face on, thinking for a moment"
    show Glasses G19
    gla "Fine! Then!"
    gla "If you don't want to leave your bed, then we're still hanging out!"
    show Glasses GlassesThought
    gla "I'll just have to join you..."
    show Glasses G13
    gla "Scoot over!"
    jump end
    
label paythefine:
    show Glasses G9
    sb ">You let her win the blanket fight{p}...Not that you couldn't have won if you had tried{p}...Oh who are you kidding{p}...She's way stronger than you"
    show Glasses G8
    sb ">And now she's gloating"
    show Glasses G2
    sb ">Well until she realizes underneath the blanket it was just you and a pair of boxers {p} also you have morning wood"
    gla "'I... uh sorry!' {p} 'I didn't know, why didn't you say something!' {p}...She's beyond embarassed"
    show Glasses G20
    gla "I'll uhh, leave you alone for a while to deal with that {p} and then we can go ... ok?"
    show Glasses G6
    sb ">She walks out, lips prim {p}...you feel like that could have gone better"
    jump end
    
    
label cleanpants:
    show Glasses G17
    sb ">She quickly begins helping you find the cleanest pair of lower garments in the room"
    sb ">Which doesn't take her long as she holds it up"
    show Glasses G13
    Gla "How about this? It's the only thing that doesn't smell like you've worn it twice"
    sb "She's holding up one of Raven's skirts {p}... coincidentally she is right {p}...it's probably the cleanest thing in the room"
    show Glasses G27
    gla ""So?" She Asks, holding it up to her waist"
    sb ">Of course shes asking how it would look on her, not you"
    jump end
label cleanpantsquietly:
    sb ">You figure glasses probably won't help very much anyway with finding clothes"
    sb ">Plus, most the pants on the floor are actually clean, you just had a slight...{p}...explosion{p}... in your closet over the weekend"
    sb "Blame birthday, she needed boys clothes for some reason, and you hadn't sorted them back yet"
    jump end
    
    

    jump end # this is not strictly necessary, as control will fall through to the next label (I think), but good for organization
            
label end:
    scene bg heart
    sb "The Ride Never Ends... Except here"
    return