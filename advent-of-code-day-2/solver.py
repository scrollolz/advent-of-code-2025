
file_path = "password.txt"

num_invalid = []

try:
    with open(file_path, 'r') as password:
        for line in password:
            while(line):
                i = line.index(',')
                substring = line[0:i]

                line = line[i+1:len(line)]

                dash = substring.index('-')
                num1 = int(substring[0:dash])
                num2 = int(substring[dash+1:len(substring)])
                for i in range(num1, num2):
                    iString = str(i)

                    left = iString[0:1]
                    right = iString[1:len(iString)]
                    if


            

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

