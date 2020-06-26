# summa = input("Summani kiriting: ")

# if summa.isdigit() and int(summa) > 0 and int(summa) < 100000000:     # isdigit funksiyasi son yoki sonmasligini tekshiradi
#     print("To'lov amalga oshirildi! ")
# else:
#     print("xatolik bor yaxshilab ko'ring")


# ism = input("What is your name: ")
# familya = input("What is your surname: ")

# if ism or familya:
#     print("Tashshakurlar! ")
# else:
#     print("Bittasi kiriting")


#                                  # Masala

# son = input("1 dan 30 gacha sonni kiriting: ")
# if son.isdigit():
#     son = int(son)
#     if son > 0 and son < 30:
#         qoldiq = son % 10
#         letter = ''
#         if son > 9 and son < 20:
#             letter = "o'n "
#         elif son > 19 and son < 30:
#             letter = 'yigirma '

#         if qoldiq == 1:
#             letter += 'bir'
#         elif qoldiq == 2:
#             letter += 'ikki'
#         elif qoldiq == 3:
#             letter += 'uch'
#         elif qoldiq == 4:
#             letter += 'to\'rt'
#         elif qoldiq == 5:
#             letter += 'besh'
#         elif qoldiq == 6:
#             letter += 'olti'
#         elif qoldiq == 7:
#             letter += 'yetti'
#         elif qoldiq == 8:
#             letter += 'sakkiz'
#         elif qoldiq == 9:
#             letter += 'to\'qqiz'
#     print(letter)

                            # Masala unli yoki undoshligini topish

unli = ['a', 'u', 'i', 'e', 'o', "o'"]
undosh = ['b', 'd', 'r', 't', 'y', 'p', 'q', 's', 'f',
          'g', 'h', 'j', 'k', 'l', 'z', 'x', 'v', 'n', 'm']

soz = str(input('Harf kiriting: '))

if soz in unli:
    print('unli harf')
elif soz in undosh:
    print('undosh harf')
else:
    print('Siz harf kiritmadingiz')
