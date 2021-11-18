import sys
from random import randint

#argumentos nombre, apellido num menor y num mayor (rango de número a adivinar)
filename = sys.argv[0]
first = sys.argv[1]
last = sys.argv[2]
print(f'filename: {filename}')
print(f'hiii! {first} {last}')



num_gen = randint(1, 10)
lim_inf= int(sys.argv[3])
lim_sup = int(sys.argv[4])
num_gen = randint(lim_inf, lim_sup)
num_opor = 4

while num_opor > 0:
    try:
        print(num_gen)
        guess = int(input(f'Tienes {num_opor} oportunidades para adivinar un num entre {lim_inf}-{lim_sup}: '))
        if lim_inf <= guess <= lim_sup:
            if guess == num_gen:
                print('you won')
                break
            else:
                num_opor -= 1
                if num_opor <= 0:
                    print(f'Sorry, you lost. The number was {num_gen}')
                    break
                else:
                    print(f'wrong guess, try again. You only have {num_opor} chances left')
        else:
            print(f'Please, enter a number between {lim_inf}-{lim_sup}: ')
    except ValueError:
        print('enter a valid number')
        continue

