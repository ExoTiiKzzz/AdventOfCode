# get the input file (input.txt)
with open('input.txt', 'r') as f:
    input = f.read().splitlines()

total = 0

for line in input:
    min_red = 0
    min_green = 0
    min_blue = 0
    # split by ':'
    game = line.split(':')
    sweepstakes = game[1].split(';')
    is_possible = True
    for sweepstake in sweepstakes:
        red = min_red
        green = min_green
        blue = min_blue
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
        # check if red, green, and blue are less than the min
        if red > min_red:
            min_red = red
        if green > min_green:
            min_green = green
        if blue > min_blue:
            min_blue = blue


    line_total = min_red * min_green * min_blue
    total += line_total

print('Total: ' + str(total))