
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
count = 0
previous = -1
increase = 0

for line in Lines:
    count += 1
    if previous > 0:
        if int(line) > previous:
            # print("Increased: " + line)
            increase += 1

    previous = int(line)

print("Total increased: " + str(increase))