# import random

# a = random.randrange(1,500)
# b = random.randrange(1,500)

# c = int(input('{} + {} = '.format(a, b)))

# if c == (a + b):
#     print("To'g'ri")
# else:
#     print("xato")


                                    #Kabisa yilini topish                                

yil = int(input("Yilni kiriting:"))
if yil % 4 != 0:
    print("Kabisa yili emas")
elif yil % 100 == 0:
    if yil % 400 == 0:
        print("Kabisa yili")
    else:
        print("Kabisa yili emas")
else:
    print("Kabisa yili")