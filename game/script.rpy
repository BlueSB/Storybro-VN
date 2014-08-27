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
define glasses = Glasses('Glasses', color="#785f24")
define raven = Raven('Raven', color="#6b4b64")
define birthday = Birthday('Brown Haired Birthday Girl', color="#2e0c85")
define homely = Homely('Homely', color="#d62d2d")
define sb = Character('Storybro', color="#055000")

# Declare Images used by this game.
image bg sleepy = "overslept.jpg"
image woody girl = "Princess Woody.jpg"
image woody boy = "the lewd king.jpg"
image heart = "Heart.png"
image frogbro = "forever.jpg"

# The game starts here.
label start:
    scene bg sleepy
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
    $ player.gender = boy
    show woody boy
    sb "Now, what did you say your name was?"
    
    menu:
        "RED":
            $ player.chosen_name = "RED"
        "BLUE":
            $ player.chosen_name = "BLUE"
        "YELLOW":
           $ player.chosen_name = "YELLOW"
        "DICKS":
           $ player.chosen_name = "DICKS"
    jump truestart

label startgirl:
    $ player.gender = girl
    show woody girl
    sb "Now, what did you say your name was?"
    
    menu:
        "RED":
            $ player.chosen_name = "RED"
        "BLUE":
            $ player.chosen_name = "BLUE"
        "YELLOW":
           $ player.chosen_name = "YELLOW"
        "CUNTS":
           $ player.chosen_name = "CUNTS"
    jump truestart
    
label truestart:
    # Inserting a variable in brackets will do text substitution
    sb "So, [player.chosen_name], are you ready?"

    sb "Your very own 'Women' story is about to unfold"
    sb "You'll face fun times, and tough challenges"
    sb "A world of dreams and adventures with Women awaits! Let's Go!"
    
    # unfortunately, I didn't see a way to do string concatentation with python statements,
    # so for cases where we want to query a variable and change text we have to use the python-equivalent
    # calling method
    # The statement (x if condition else y) is called ternary if; if condition evaluates to something truthy it returns the first
    # value, otherwise it returns the second value.
    $ sb("You grew up as an awkward. Somewhat nerdy, but generally likeable " + ("guy" if player.gender is boy else "gay") + ".")
    $ sb(("Unluckily," if player.gender is boy else "Possibly because") + "you're not much of a hit with men, so you've grown up around women your entire life")
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
            if player.gender == "boy":
                jump sleepover_male
            else:
                jump sleepover_female
        "I'd better not, my parents want me home for dinner":
            jump FROG_END
  
label FROG_END:
    scene frogbro at truecenter # centers image horizontally and vertically
    sb "You say your goodbyes, smile and wave to the girls as you step out of the car"
    sb "Your mother will be here in fifteen minutes to pick you up"
    sb "You're having spaghetti for dinner"
    sb "I hope it's worth it"
    "FROG END"
    return

label sleepover_female:
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
    jump end

label sleepover_male:
    sb "You agree to the sleepover, why not right?"
    sb "The other guy doesn't seem to think so, he's either not invited or he has to go home for dinner"
    sb "Friends are more important than spaghetti anyway"
    sb "plus it's been ages since you've been to a sleepover"
    sb "Your best friend, the black haired girl. She pretty much convinces them you have to come with"
    sb "So this'll be interesting you think, as the limo pulls up to the lawn of the birthday girl's house"
    jump end # this is not strictly necessary, as control will fall through to the next label (I think), but good for organization
            
label end:
    scene heart
    # the following are equivalent:
    #     "THE RIDE NEVER ENDS"
    #     narrator "THE RIDE NEVER ENDS"
    # use this to apply the previous python equivalency to use text concatentation
    $ narrator("THE RIDE NEVER ENDS, except here" + (", M'lady" if player.gender is girl else ""))
    return