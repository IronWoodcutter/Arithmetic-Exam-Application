# write your code here
import random

n = 0
level = 0

def arithmetic():
    global math_tasks
    line = []
    operator = ['+', '*', '-']
    line.append(str(random.randint(2, 9)))
    line.append(random.choice(operator))
    line.append(str(random.randint(2, 9)))
    print_line = ' '.join(line)
    if line[1] == '+':
        math_tasks = int(line[0]) + int(line[2])
        print(print_line)
    elif line[1] == '*':
        math_tasks = int(line[0]) * int(line[2])
        print(print_line)
    elif line[1] == '-':
        math_tasks = int(line[0]) - int(line[2])
        print(print_line)
def squares():
    global math_tasks
    a = random.randint(11, 29)
    print(a)
    math_tasks = a * a
r = int()
while True:

    print('Which level do you want? Enter a number:')
    print('1 - simple operations with numbers 2-9')
    print('2 - integral squares of 11-29')
    level = int(input())
    if level == 1 or level == 2:
        break
    else:
        print('Incorrect format.')

for item in range(5):
    if level == 1:
        arithmetic()
    else:
        squares()
    while True:

        try:
            answer = int(input())
            if answer == math_tasks:
                print('Right!')
                n += 1
                break
            else:
                print('Wrong!')
                break
        except ValueError:
            print('Incorrect format.')
print(f'Your mark is {n}/5. Would you like to save your result to the file? Enter yes or no.')
save = input()
if save in ('yes, YES, y, Yes'):
    print('What is your name?')
    name = input()
    if level == 1:
        description = ('simple operations with numbers 2-9' )
    else:
        description = ('integral squares 11-29')

    result = (f'{name}: {n}/5 in level {level} ({description}).')
    #result = (f"Alex: 3/5 in level 1 (simple operations with numbers 2-9).")

    with open('results.txt', 'a+') as file:
        file.write(result)
print('The results are saved in "results.txt".')