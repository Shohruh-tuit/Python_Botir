                                    # break and continue

# soz = input("So'z kiriting: ")

# for s in soz:
#     if s.isdigit():
#         #break
#         continue
#     print(s)


                                    # 11 - dastur 

from turtle import Turtle, Screen

oyna = Screen()
oyna.title("Bu mening birinchi oynam")


chiziq = Turtle()
chiziq.hideturtle()
chiziq.pensize(3)
chiziq.color('blue')
chiziq.speed(3)
chiziq.up()
chiziq.goto(150,150)
chiziq.down()
chiziq.goto(150,-150)
chiziq.goto(-150, -150)
chiziq.goto(-150,150)
chiziq.goto(150, 150 )

chegara = Turtle()
chegara.color('green')
chegara.pensize(5)
chegara.up()
chegara.goto(-125, -150)
chegara.down()
chegara.goto(-125, -125)
chegara.goto(-40, -125)
chegara.goto(-40, -150)

koptok = Turtle()
koptok.shape('circle')
koptok.shapesize(1)
koptok.color('red')
koptok.up()
koptok.goto(0,0)

golyozuvi = Turtle()
golyozuvi.hideturtle()

step_x = 3
step_y = 2
while True:
    x, y = koptok.position()

    if x + step_x >= 150 or x + step_x <= -150:
        step_x = -step_x
    if y + step_y >= 150 or y + step_y <= -150:
        step_y = -step_y
    if x>=-125 and  x<=-75 and y>=-150 and y<=-125:
        golyozuvi.color('deep pink')
        style = ('Courier', 30, 'italic')
        golyozuvi.write('Goal!', font=style, align='center')
        golyozuvi.hideturtle() 
        break


    koptok.goto(x + step_x, y + step_y)
    
oyna.mainloop()