lines = []
f = open("input2.txt", "r")

lines = f.read().splitlines()

horizontal = 0
depth = 0
aim = 0

for i in lines:
    move = i.split()

    if (move[0] == 'up'):
        aim -= int(move[1])
    elif (move[0] == "down"):
        aim += int(move[1])
    elif (move[0] == "forward"):
        horizontal += int(move[1])
        depth += int(move[1]) * aim

print(depth * horizontal)