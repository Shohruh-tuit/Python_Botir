n = input('Ismingizni kiriting: ')
s = input('Familyangizni kiriting: ')
y = int(input('yoshingizni kiriting sonda: '))
print('Salom sizning ismingiz {0}, familyangiz esa {1}, yoshingiz esa {2} shundaymi ?'.format(
    n, s, y))

Javob = int(input("Agar ha bo'lsa 1 ni bosing yo'q bo'lsa 2 ni: "))

def TrueFalse(Javob):
    if(Javob == 1):
        print('Demak hammasi chiki chiki! ')
    else:
        print("Formani boshqattan to'ldiring, please!!! ")

TrueFalse(Javob)