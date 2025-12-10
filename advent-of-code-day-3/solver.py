
file_path = "password.txt"
output = 0
firstNum = 0
secondNum = 0

try:
    with open(file_path, 'r') as password:
        for num in password:
            num = num.strip()
            print(num)
            for c in num:
                if int(c) > firstNum and num.find(c) != len(num) - 1:
                    firstNum = int(c)
            for c in num[num.find(str(firstNum))+1:len(num)]:
                if int(c) > secondNum:
                    secondNum = int(c)


            numTogether = str(firstNum) + str(secondNum)
            print(numTogether)

            firstNum = 0
            secondNum = 0

            output += int(numTogether)




except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(output)