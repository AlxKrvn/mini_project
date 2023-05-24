from random import sample
from time import sleep

def need(text):

    while True:
        symbol = input(text).lower()
        if symbol in ['yes', 'no']:
            if symbol == 'yes':
                return True
            else:
                return False
        else:
            print('repeat')
            continue
def if_not(ans, symb):

    global chars
    if not ans:
        for i in chars:
            if i in symb:
                chars = chars[:chars.index(i)] + chars[chars.index(i)+1:]
    return chars
def password_gen(lengh, symb):
    def need_1(ans, smbl):

        nonlocal a
        if ans:
            for i in p:
                if i in smbl:
                    a -= 1
                    break
        else:
            a -=1   
        return a 
    
    a = 4
    while a != 0:

        a = 4
        p = sample(symb, lengh)
        a = need_1(need_dig, dig)
        a = need_1(need_low, low_lett)
        a = need_1(need_upp, upp_lett)            
        a = need_1(need_punct, punct)

    p = ''.join(p)
    return p

dig = '0123456789'
low_lett = 'abcdefghijklmnopqrstuvwxyz'
upp_lett = low_lett.upper()
punct = '!#$%&*+-=?@^_'
chars = dig + low_lett + upp_lett + punct
anb_char = 'il1Lo0O'

print('Hello)))')
sleep(2)

how_much = int(input('how many passwords do you need? '))
lenght = int(input('how many characters are in the password? '))
need_dig = need('need digits? ')
need_low = need('need low letters? ')
need_upp = need('need upp letters? ')
need_punct = need('need special symbols? ')
need_anb = need('need ambiguous characters (il1Lo0O)? ')

chars = if_not(need_dig, dig)
chars = if_not(need_low, low_lett)
chars = if_not(need_upp, upp_lett)
chars = if_not(need_punct, punct)
chars = if_not(need_anb, anb_char)

for i in range(1, how_much+1):
    pas = password_gen(lenght, chars)
    print(f'password №{i}: {pas}')






