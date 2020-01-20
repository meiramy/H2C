file = open("lorem.txt", "r")

lines = file.readlines()

first_lines = lines[:3]
last_lines = lines[-3:]

print("The first three lines:")
for line in first_lines:
    print(line)
    print("")
print("The last three lines: ")     
for line in last_lines:
    print(line)
file.close()
