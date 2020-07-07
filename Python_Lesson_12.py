
                                            # 12-dastur. Statistika
                            
# import pygal

# line_chart = pygal.Line()
# line_chart.title = 'Statistika'
# line_chart.x_labels = ['Fevral', 'Mart', 'Aprel', 'May']
# line_chart.add('Youtube', [9.24, 12.5, 12.8, 19.4])
# line_chart.add('Instagram', [10.6, 15.4, 17.8, 20])
# line_chart.add('Facebook', [13.4, 11.8, 14.9, 22.8])
# line_chart.add('TikTok', [8, 10.4, 15.7, 22.7])
# line_chart.render_in_browser()


# l = list(map(float , input().split()))
# print(l)


                                                # Homework

import pygal

line_chart = pygal.Line()
line_chart.title = 'Statistika'

Tarmoq_1 = input("ijtimoiy tarmoq nomini kiriting: ")
Qiymat_1 = input(Tarmoq_1 + "ning 3 ta qiymatini kiriting: ")
userList_1 = list(map(float, Qiymat_1.split()))

Tarmoq_2 = input("ijtimoiy tarmoq nomini kiriting: ")
Qiymat_2 = input(Tarmoq_2 + "ning 3 ta qiymatini kiriting: ")
userList_2 = list(map(float, Qiymat_2.split()))

Tarmoq_3 = input("ijtimoiy tarmoq nomini kiriting: ")
Qiymat_3 = input(Tarmoq_3 + "ning 3 ta qiymatini kiriting: ")
userList_3 = list(map(float, Qiymat_3.split()))

line_chart.x_labels = [Tarmoq_1, Tarmoq_2, Tarmoq_3]

line_chart.add(Tarmoq_1, userList_1)
line_chart.add(Tarmoq_2, userList_2)
line_chart.add(Tarmoq_3, userList_3)

line_chart.render_in_browser()

