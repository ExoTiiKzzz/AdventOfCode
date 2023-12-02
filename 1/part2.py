# get input (input.txt)
with open('input.txt', 'r') as f:
    input = f.read().splitlines()

numbersDict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_line_total(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        # concatenate number with himself
        return int(str(numbers[0]) + str(numbers[0]))
    elif len(numbers) == 2:
        # concatenate numbers
        return int(str(numbers[0]) + str(numbers[1]))
    else:
        # return concatenation of first and last number
        return int(str(numbers[0]) + str(numbers[-1]))


def search_for_number(line, number, start_index):
    number = str(number)
    if line.find(number, start_index) != -1:
        return line.find(number, start_index)
    else:
        return -1


def get_line_numbers(line):
    # get index of all digits
    digit_indexes = []
    for digit in digits:
        # check if digit is present multiple times
        start_index = 0
        while search_for_number(line, digit, start_index) != -1:
            start_index = search_for_number(line, digit, start_index)
            end_index = start_index + len(str(digit)) - 1
            digit_indexes.append({
                'start': start_index,
                'end': end_index,
                'number': digit
            })
            start_index += 1

    # get start and end index of all numbers (one, two, three, etc.)
    number_indexes = []
    for number in numbersDict:
        # get numbers start index using searchForNumber
        start_index = 0
        while search_for_number(line, number, start_index) != -1:
            start_index = search_for_number(line, number, start_index)
            end_index = start_index + len(number) - 1
            number_indexes.append({
                'start': start_index,
                'end': end_index,
                'number': numbersDict[number]
            })
            start_index += 1

    all_numbers = []
    # order numbers by start index
    for numberIndex in number_indexes:
        all_numbers.append(numberIndex)
    for digitIndex in digit_indexes:
        all_numbers.append(digitIndex)

    all_numbers.sort(key=lambda x: x['start'])

    # get all numbers
    numbers = []
    for number in all_numbers:
        numbers.append(number['number'])

    return numbers


total = 0
for line in input:
    # get each number
    numbers = get_line_numbers(line)

    lineTotal = get_line_total(numbers)
    total += lineTotal

print('Total should be 54019 (found:', total, ')')
