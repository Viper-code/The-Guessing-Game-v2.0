import random
import time

print('Welcome to The Guessing Game!')
time.sleep(2)
print(
    'You will want to guess a number from 1-10\nif you want to change this please type "change_num", or if your fine please type "start" below>')
time.sleep(1.5)
start_chng_num = input('(start/change_num): ')

if start_chng_num == 'change_num':
    wt_num = int(input('What number do you choose: '))
    if wt_num > 100:
        print('Please pick a number lower than 100 and higher then 2.')
        exit()
    if wt_num < 5:
        print('Please pick a number higher than 2 and lower than 100.')
        exit()
    if wt_num == 10:
        print('sorry you cannot choose this number!\nPlease run this programm again!')
        input('Please press enter to Exit:')
        exit()
    else:
        core_num = random.randint(1, int(wt_num))
        if wt_num < 10:
            choose = 4
        if 11 < wt_num <= 21:
            choose = 5
        if 21 < wt_num <= 31:
            choose = 6
        if 31 < wt_num <= 41:
            choose = 7
        if 41 < wt_num <= 51:
            choose = 9
        if 51 < wt_num <= 61:
            choose = 12
        if 61 < wt_num <= 71:
            choose = 13
        if 71 < wt_num <= 81:
            choose = 15
        if 81 < wt_num <= 91:
            choose = 19
        if 91 < wt_num < 101:
            choose = 21
        print(f'Success changed your number to 1,{wt_num}!\nPlease dont restart the programm or else the nmber will be changed back! You have {str(choose)} tries! Please type "start" to start the game')
        start = input('Please type start: ')
        if start == 'start':
            tries = choose
            while tries != 0:
                tip = random.randint(1, 20)
                if tip == 7:
                    time.sleep(1.1)
                    print('*tip*do /end if you want to end the game.')
                guess = input(f'please input your guess from 1,{wt_num}: ')
                if str(guess) == '/end':
                    print('You have ended the game!')
                    break
                if int(guess) == core_num:
                    print('Well done you got the number!!!')
                    break
                elif guess != core_num:
                    tries = tries - 1
                    print(f'try again, you got {tries} tries')
                if tries == 0:
                    print(f'Oh no! you ran out of tries! The number was {core_num}')
                    break

if start_chng_num == 'start':
    tries = 4
    core_num = random.randint(1, 10)
    while tries != 0:
        tip = random.randint(1, 20)
        if tip == 7:
            time.sleep(1.1)
            print('*tip*do /end if you want to end the game.')
        guess = input(f'please input your guess from 1,10: ')
        if str(guess) == '/end':
            print('You have ended the game!')
            break
        if int(guess) == core_num:
            print('Well done you got the number!!!')
            break
        elif guess != core_num:
            tries = tries - 1
            print(f'try again, you got {tries} tries')
        if tries == 0:
            print(f'Oh no! you ran out of tries! The number was {core_num}')
            break
