name1 = input("What is the first name: ").lower()
name2 = input("What is the second name: ").lower()

t_count = 0
l_count = 0
for name in [name1, name2]:
    for char in name:
        if char in ['t', 'r', 'u', 'e']:
            t_count += 1
        if char in ['l', 'o', 'v', 'e']:
            l_count += 1

love_score = f"{t_count}{l_count}"

print(love_score)

