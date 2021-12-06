
file1 = open('input.txt', 'r')
oxygen_lines = file1.readlines()
carbon_lines = oxygen_lines.copy()

 

def most_frequent(lines, col):
    count = 0
    for line in lines:
        if line[col] == "1":
            count += 1
    if count >= len(lines)/2:
        return 1
    else:
        return 0

def least_frequent(lines, col):
    ones = 0
    zeros = 0
    for line in lines:
        if line[col] == "1":
            ones += 1
        else:
            zeros += 1
    if ones < zeros:
        return 1
    elif zeros < ones:
        return 0
    else:
        return 0

def filter_lines(lines, col, value):
    new_lines = []
    for line in lines:
        if int(line[col]) == value:
            new_lines.append(line)
    return new_lines

oxygen = ""
carbon = ""

for column in range(len(oxygen_lines[0].strip())):
    if oxygen_lines == 1:
        oxygen += oxygen_lines[0][column]
    else:
        mf = most_frequent(oxygen_lines, column)
        oxygen_lines = filter_lines(oxygen_lines, column, mf)
        oxygen += str(mf)

for column in range(len(carbon_lines[0].strip())):
    if len(carbon_lines) == 1:
        carbon += carbon_lines[0][column]
    else:
        lf = least_frequent(carbon_lines, column)
        carbon_lines = filter_lines(carbon_lines, column, lf)
        carbon += str(lf)

print("Oxygen:", oxygen, int(oxygen, 2))
print("Carbon:", carbon, int(carbon, 2))
print("Life Support Rating:", int(oxygen, 2) * int(carbon, 2))