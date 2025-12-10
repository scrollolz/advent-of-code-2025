
file_path = "password.txt"
dial = 50
numSol = 0

try:
    with open(file_path, 'r') as password:
        for line in password:
            line = line.strip()
            direction = line[0]
            num = int(line[1:])
            if direction == 'R':
                dial += num
                dial %= 100
                if dial == 0:
                    numSol += 1
            elif direction == 'L':
                dial -= num
                dial %= 100
                if dial == 0:
                    numSol += 1

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(numSol)