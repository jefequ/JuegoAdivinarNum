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
num_opor = 6
cve_show_num_gen = 343443410

while num_opor > 0:
    try:
#        print(num_gen)
        guess = int(input(f'Tienes {num_opor} oportunidades para adivinar un num entre {lim_inf}-{lim_sup}: '))
        if guess == cve_show_num_gen:
            print(f'el número a adivinar es: {num_gen}')
        elif guess == num_gen:
            print('you won')
            break
        elif lim_inf <= guess <= lim_sup:
            num_opor -= 1
            if num_opor <= 0:
                print(f'Sorry, you lost. The number was {num_gen}')
                break
            elif guess > num_gen:
                print(f'Wrong guess. The number is smaller than {guess}. You have {num_opor} chances left')
            else:
                print(f'Wrong guess. The number is greater than {guess}. You have {num_opor} chances left')
        else:
            print(f'Please, enter a number between {lim_inf}-{lim_sup}: ')
    except ValueError:
        print('enter a valid number')
        continue

