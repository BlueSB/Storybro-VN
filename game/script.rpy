# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define blondie = Character('Blondie', color="#e1e823")
define glasses = Character('Glasses', color="#785f24")
define raven = Character('Raven', color="#6b4b64")
define birthday = Character('Birthday', color="#2e0c85")
define homely = Character('Homely', color="#d62d2d")
define storybro = Character('Storybro', color="#000000")

# The game starts here.
label start:
    storybro "Which girl should I pick?"
    
    menu:
        "Best girl":
            jump best
        "Worst girl":
            jump worst
            
label best:
    homely "I knew you'd pick me!"
    jump bad_end
    
label worst:
    raven "I knew you'd pick me!"
    jump bad_end
    
label bad_end:
    "BAD END"
    return
