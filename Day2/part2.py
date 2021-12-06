
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
horizontal = 0
depth = 0
aim = 0

for line in Lines:
    command = line.split()
    if command[0] == 'forward':
        horizontal += int(command[1])
        depth += aim * int(command[1])
    elif command[0] == 'down':
        aim += int(command[1])
    elif command[0] == 'up':
        aim -= int(command[1])
    # print("Horizontal: " + str(horizontal) + " Depth: " + str(depth) + " Aim: " + str(aim))

print("Total: " + str(horizontal * depth))