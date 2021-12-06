
file1 = open('input.txt', 'r')
lines = file1.readlines()
 
previous = -1
increase = 0
window_size = 3


for i in range(len(lines) - window_size + 1):
    val1 = int(lines[i])
    val2 = int(lines[i+1])
    val3 = int(lines[i+2])

    window_value = val1 + val2 + val3

    if previous > 0:
        if int(window_value) > previous:
            increase += 1

    previous = int(window_value)

print("Total increased: " + str(increase))
