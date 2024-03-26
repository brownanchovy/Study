import random

num = random.randint(1, 100)

while True:
    try:
        my_num = int(input(("innput val form 0 to  100")))
        if my_num > num:
            print('down')
        elif my_num < num:
            print('up')
        else:
            print('ans')
            exit()
    except ValueError:
        print('num please')

'''
user_list = ['a', 'b', 'c']
user_id = input("input name")

if user_id in user_list:
    pw = int(input("input passwd").strip())

    if pw == '1234':
        print('welcome')

    else:
        print('wrong passwd')
else:
    print('not our team')
'''
