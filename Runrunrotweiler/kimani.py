import random

while True:
    person = input("What is your name? ")

    if person.lower() == "kimani":
        print("Nice try. But I cannot insult my creator you fool!")
    else:
        break

bad_guys_list = ["widow maker", "dragon hunter", "flesh pounder", "soul reaper", "darkstalker"]
bodyparts_list = ["Head", "heart", "Brain", "spleen"]
insults_list = ["dirty pickle", "brainless fool", "wannabe superhero", "pumpkin pie haircutted freak"]

bad_guy = random.choice(bad_guys_list)
body_part = random.choice(bodyparts_list).lower()
insult = random.choice(insults_list)

print(
    f"Well hello there {person}, I've been waiting for someone to stumble into my lair. I am {bad_guy}. I will rip out your {body_part}. Good luck trying to survive after that, you little {insult}.")
