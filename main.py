names = []
with open("./Input/Names/invited_names.txt", mode="r") as file:
    for name in file:
        names.append(name.strip())

for x in range(len(names)):
    with open(f"./Output/ReadyToSend/{names[x]}.txt", mode="w") as f1:
        f2 = open(f"Input/Letters/starting_letter.txt")
        for lines in f2:
            line = lines
            if line == "Dear [name],\n":
                replace = line.replace("[name]", names[x])
                f1.write(replace)
            else:
                f1.write(lines)
        f2.close()


