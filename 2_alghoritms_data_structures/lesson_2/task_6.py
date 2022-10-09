from random import randrange

def game(num, attemp=1):
    print(f'attemp {attemp}')
    i = input('Enter the number: ')
    if num == i:
        print('OK')
        return
    else:
        if attemp == 10:
            print(f'game over, secret number = {num}')
            return
        else:
            attemp += 1
            game(num, attemp)

secret = randrange(1,101)
game(secret)