
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
horizontal = 0
depth = 0

for line in Lines:
    command = line.split()
    if command[0] == 'forward':
        horizontal += int(command[1])
    elif command[0] == 'down':
        depth += int(command[1])
    elif command[0] == 'up':
        depth -= int(command[1])
    # print("Horizontal: " + str(horizontal) + " Depth: " + str(depth))

print("Total: " + str(horizontal * depth))