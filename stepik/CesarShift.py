eng_low_alph = 'abcdefghijklmnopqrstuvwxyz'
eng_upp_alph = eng_low_alph.upper()
rus_low_alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upp_alph = rus_low_alph.upper()

while True:
    we_do = input('encryption or decryption? (enc or dec) ').lower()
    if we_do in ['enc', 'dec']:
        break
    else:
        print('repeat')
while True:
    what_leng = input('Rus or Eng alphabet? ').lower()
    if what_leng in ['rus', 'eng']:
        break
    else:
        print('repeat')
if what_leng == 'rus':
    low_alph = rus_low_alph
    upp_alph = rus_upp_alph
elif what_leng == 'eng':
    low_alph = eng_low_alph
    upp_alph = eng_upp_alph
rot = int(input('cipher key = '))
text = input()

if we_do == 'enc':
    a = []
    for i in text:
        if i in low_alph:
            if low_alph.index(i) + rot < len(low_alph):
                i = low_alph[low_alph.index(i) + rot]
            else:
                i = low_alph[low_alph.index(i) + rot - len(low_alph)]
        elif i in upp_alph:
            if upp_alph.index(i) + rot < len(upp_alph):
                i = upp_alph[upp_alph.index(i) + rot]
            else:
                i = upp_alph[upp_alph.index(i) + rot - len(upp_alph)]
        a += i

if we_do == 'dec':
    a = []
    for i in text:
        if i in low_alph:
            if low_alph.index(i) - rot < 0:
                i = low_alph[len(low_alph) + low_alph.index(i) - rot]
            else:
                i = low_alph[low_alph.index(i) - rot]
        if i in upp_alph:
            if upp_alph.index(i) - rot < 0:
                i = upp_alph[len(low_alph) + upp_alph.index(i) - rot]
            else:
                i = upp_alph[upp_alph.index(i) - rot]
        a += i

a= ''.join(a)
print(a)

    

