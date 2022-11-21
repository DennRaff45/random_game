import random

while True:
    start_input = input('Hey, this is my first simple game, please enter you number from 1~3: ')
    random_num = str(random.randint(1, 2))
    if start_input == random_num:
        print('WOOOOOWWW, you are win!!!! OMGGGGGGGG')
        print(f'The number was really {start_input} !!!')
        break
    elif start_input != random_num:
        print('mmmmmm.... try again, I think you are so close....')
        print('The number was: ' + str(random_num))
