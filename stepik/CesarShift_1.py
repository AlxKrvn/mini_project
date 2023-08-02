text = input()

c = []
low_alph = 'abcdefghijklmnopqrstuvwxyz'
upp_alph = low_alph.upper()

a = text.split()

for i in a:
    f = []
    b = []
    rot = 0
    for j in i:
        if j in low_alph or j in upp_alph:
            rot += 1
    i = [m for m in i]
    for  k in i:
        if k in low_alph:
            if low_alph.index(k) + rot > len(low_alph) - 1:
                k = low_alph[low_alph.index(k) + rot - len(low_alph)]
            else:
                k = low_alph[low_alph.index(k) + rot]
        elif k in upp_alph:
            if upp_alph.index(k) + rot > len(upp_alph) - 1:
                k = upp_alph[upp_alph.index(k) + rot - len(upp_alph)]
            else:
                k = upp_alph[upp_alph.index(k) + rot]
        b += k
    b = ''.join(b)
    f = [b]
    c += f

c = ' '.join(c)    
print(c)