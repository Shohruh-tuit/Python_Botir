#format()
# s = input('What is your name: ')
# print('Hello {}'.format(s))
# print('{:.5}'.format(s))    # truncate long string -- yani nechta belgini chiqarish

# print('{} {}'.format('one', 'two'))

# soz = 'I love programming with python'
# print(len(soz.split()))

# class Data(object):
#     def __str__(self):
#         return 'str'
#     def __repr__(self):
#         return 'repr'

# print('{0!s} {0!r}'.format(Data()))

print('{:10}{}'.format('test','ss'))  # testdan keyin 10 ta qator tashlaydi
print('{:>10} {}'.format('test','ss'))  # testdan oldin 10 ta qator tashlaydi
print('{:^10}'.format('test'))          # testni 10 beligini ichiga joylashtirib beradi
