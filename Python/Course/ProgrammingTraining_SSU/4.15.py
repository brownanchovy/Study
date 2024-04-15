import random
import time
words = [None]
def run_game():
    print('starting')
    for countdown in range(3,0,-1):
        print(countdown)
        time.sleep(1)
    print('start')

    score =0
    chances = 3

    while chances >0:
        word = random.choice(words)
        print(word,'-->', end= '')

        user_input = input()
        if user_input == word:
            print('correct')
        else:
            chances -=1
            print('wrong')

run_game()