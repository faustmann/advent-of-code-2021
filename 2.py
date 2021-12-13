
def prepare_line(line):
    splitted_line = line.split(' ')
    return (splitted_line[0], int(splitted_line[1]))

with open("2_1.txt") as fp:
    commands = list(map(prepare_line, fp.readlines()))

x = 0
y = 0
aim = 0

for command in commands:
    if command[0] == 'forward':
        x = x + command[1]
        y = y + command[1] * aim
    elif command[0] == 'down':
        aim = aim + command[1]
    elif command[0] == 'up':
        aim = aim - command[1]

print(x*y)
