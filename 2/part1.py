# get the input file (input.txt)
with open('input.txt', 'r') as f:
    input = f.read().splitlines()

total = 0
color_dict = {
    'red': 12,
    'green': 13,
    'blue': 14
}

for line in input:
    # split by ':'
    game = line.split(':')
    sweepstakes = game[1].split(';')
    is_possible = True
    for sweepstake in sweepstakes:
        red = 0
        green = 0
        blue = 0
        # split by ','
        sweepstake = sweepstake.split(',')
        # get the color and the number of the color
        for color in sweepstake:
            color = color.strip().split(' ')
            if color[1] == 'red':
                red = int(color[0])
            elif color[1] == 'green':
                green = int(color[0])
            elif color[1] == 'blue':
                blue = int(color[0])
        # add the number of colors to the total
        # check if the sweepstake is possible
        for key, value in color_dict.items():
            if key == 'red':
                if red > value:
                    is_possible = False
            elif key == 'green':
                if green > value:
                    is_possible = False
            elif key == 'blue':
                if blue > value:
                    is_possible = False


    if is_possible:
        #add game number to total
        total += int(game[0].split(' ')[1])

print('Total: ' + str(total))