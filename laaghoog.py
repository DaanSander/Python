import random
i = -1
awnser = random.randint(0, 50)
while i != awnser:
    i = int(input("wat is het magische nummer:\n"))
    if i != awnser:
        if i < awnser:
            print("te laag")
        elif i > awnser:
            print("te hoog")

print("mooizo")
