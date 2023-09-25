
with open("testing2/story.txt") as file:
    text = file.read()
    words = text.split(" ")
    file.seek(0)
    lines = file.readlines()
stats = {"text": len(text), "words": len(words), "lines": len(lines)}

print(stats)
