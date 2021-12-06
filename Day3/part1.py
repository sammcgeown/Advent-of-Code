
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
bits = {}

for line in Lines:
    for i, c in enumerate(line.strip(), 1) :
        if c == "1":
            if i not in bits:
                bits[i] = 1
            else:
                bits[i] += 1

half = len(Lines) // 2
gamma = ""
epsilon = ""

for bit in sorted(bits):
    print(bit, bits[bit])
    if bits[bit] > half:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("Gamma:", gamma, int(gamma, 2))
print("Epsilon:", epsilon, int(epsilon, 2))
print("Consumption:", int(gamma, 2) * int(epsilon,2))