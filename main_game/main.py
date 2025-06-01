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

choices = int(input("""
                What do you want to do?
                1. Tell them who you used to be
                2. Attempt to fight them (You are severely weakened)
                3. Steal their rations and gain strength"""))

if choices == 1:
    print(f"""You walk up to the guards and introduce yourself in a weakened voice.
          I am {name}""")