from time import sleep


def print_not_fast(txt, n):
    for x in txt:
        print(x, end="", flush=True)
        sleep(n)


print("----------------------------------------------------------------------------")
print("""
▒█▀▀█ █▀▀█ █▀▀█ █░░░█ █▀▀▄ 　 █▀▀█ █▀▀ 　 ▒█▀▀█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀█ █▀▀▄ 
▒█░░░ █▄▄▀ █░░█ █▄█▄█ █░░█ 　 █░░█ █▀▀ 　 ▒█░░░ █▄▄▀ █▀▀ █▄▄█ ░░█░░ ▀█▀ █░░█ █░░█ 
▒█▄▄█ ▀░▀▀ ▀▀▀▀ ░▀░▀░ ▀░░▀ 　 ▀▀▀▀ ▀░░ 　 ▒█▄▄█ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀▀ ▀░░▀""")
print("----------------------------------------------------------------------------")

name = input("What is your name? ")

print_not_fast("""
You wake up, mind blank and not a thought in your head and observe your surroundings.
A dark, ashen desert streches as far as the eye can see.
You start walking until you can't feel your legs, manouvering yourself through darkened
caverns and avoiding vultures circling around you, knowing your imminent death
Just as you're on the brink of giving up, you see something in the distance, a large gate blocks
the entrance to The Midland of Karst, a place you once called home, and suddenly all the memories start rushing back.
You were once the Army General of this decayed country, fighting in wars that killed hundreds
but ensured your success a society, until one day a threat came that you couldn't beat...
    
""", 0.01)

print_not_fast("""The Harbinger of Death, the name rings in your head like a migrain.
How can such evil exist in the world, you think to yourself.
All was well in the Midland, no new wars in just shy of 8 years, then, a figure came from the ominous ravine at the edge of town.
At first he was accepted, made one of our own, but the second he laid eyes on the Crown of Creation,
obsession overpowered him and we found out he wasn't here to make friends
               
""", 0.01)

print_not_fast("""You see a gate in the distance, tall and grand, you know this is your way back home.
You begin to walk towards it but there's a guard
               
""", 0.01)

print_not_fast("What will you do?", 0.1)

choices = int(input("""
                What do you want to do?
                1. Tell them who you used to be
                2. Attempt to fight them (You are severely weakened)
                3. Steal their rations and gain strength
                Choose either 1, 2 or 3: """))

if choices == 1:
    print_not_fast(f"""You walk up to the guards and introduce yourself in a weakened voice.
I am {name} and I used to be the Army General of Karst. 
What happened to this great land and why am I outcast into the shadows?
I demand to know what happened.

Guard: Your time is over, OLD MAN! A new generation has blossomed.
*The guard stabs you and you die*
""", 0.01)
    
if choices == 2:
    print_not_fast(f"""Hello, young man, I am the great Army General {name} and I must slay you.
Prepare for your imminent doom!

*You pull a weathered and dull knife from your boot*

Guard: You foolish old man, you think you can beat me? Ha!
Maybe if you weren't so weakened and puny, you'd stand a chance!

*He unsheaths a longsword and plunges it into your heart*
""", 0.01)

if choices == 3:
    print_not_fast(f"""*You remember when you were taught Sneak 101 in army school*
*You wait until the guard is distracted by a pack of wolves*
Ha, fool, these young'ns need to keep their post instead of being distraced by stupid wolves
*You take his food and water and regain your strength*
""", 0.01)