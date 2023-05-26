# Code généré avec GPT3
# Chargement du fichier d'input
with open("day4_gpt3/input/input.txt", "r") as file:
    # Lecture des lignes du fichier et stockage dans une liste
    lines = file.read().splitlines()

# Parse the input
pairs = []
for line in lines:
    a, b = line.strip().split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    pairs.append((a1, a2, b1, b2))

# Solve the first part
counter1 = 0
for a1, a2, b1, b2 in pairs:
    if a1 <= b1 and b2 <= a2:
        counter1 += 1
    elif b1 <= a1 and a2 <= b2:
        counter1 += 1

# Solve the second part
counter2 = 0
for a1, a2, b1, b2 in pairs:
    if a1 <= b1 and b1 <= a2:
        counter2 += 1
    elif a1 <= b2 and b2 <= a2:
        counter2 += 1
    elif b1 <= a1 and a1 <= b2:
        counter2 += 1
    elif b1 <= a2 and a2 <= b2:
        counter2 += 1

# Print the results
print(counter1)
print(counter2)
