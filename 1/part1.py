# get input (input.txt)
with open('input.txt', 'r') as f:
    input = f.read().splitlines()

def getLineTotal(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        # concatenate number with himself
        return int(str(numbers[0]) + str(numbers[0]))
    else:
        # return concatenation of first and last number
        return int(str(numbers[0]) + str(numbers[-1]))

total = 0
for line in input:
    # get each number
    numbers = []
    # loop through each character
    for char in line:
        # if character is a number
        if char.isdigit():
            # append to numbers
            numbers.append(int(char))

    lineTotal = getLineTotal(numbers)
    total += lineTotal

print('Total:', total)
