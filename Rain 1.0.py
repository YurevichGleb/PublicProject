import turtle
import time
import random
list =  ['+','-','//','%','*']
rn1 = random.randrange(0,80)
rn2 = random.randrange(1,80)
b = random.choice(list)
drops = 5
while True:
    rn1 = random.randrange(0,80)
    rn2 = random.randrange(1,80)
    b = random.choice(list)
    print(rn1,b,rn2)
    otvet = int(input('Введите ваш ответ:'))
    if b == list[0]:
        resault = rn1 + rn2
    if b == list[1]:
        resault = rn1 - rn2
    if b == list[2]:
        resault = rn1 // rn2
    if b == list[3]:
        resault = rn1 % rn2
    if b == list[4]:
        resault = rn1 * rn2
    if resault == otvet:
        drops -=1
        print(drops)
    if resault != otvet:
        drops +=1
        print(drops)
    if drops == 10:
        break
    if drops == 0:
        break
turtle.register_shape('smile/happy.gif')
turtle.register_shape('smile/happysmile.gif')
turtle.register_shape('smile/drop.gif')
turtle.register_shape('smile/nothappy.gif')
if drops == 0:
    window = turtle.Screen()
    window.bgcolor('Yellow')
    print ('you normal')
    happy = turtle.Turtle()
    happy.shape('smile/happy.gif')
    happy2 = turtle.Turtle()
    happy2.shape('smile/happysmile.gif')
    for i in range (5):
        time.sleep(2)
        happy.hideturtle()
        time.sleep(2)
        happy2.showturtle()
        time.sleep(2)
        happy2.hideturtle()
        happy.showturtle()
    turtle.bye()
if drops == 10:
    print('you bad ')
    nothappy = turtle.Turtle()
    nothappy.shape('smile/nothappy.gif')
    drop = turtle.Turtle()
    drop.shape('smile/drop.gif')
    drop.up()
    window = turtle.Screen()
    window.bgcolor('Red')
    drop.speed(0)
    drop.fd(8)
    drop.rt(90)
    for i in range (2):
        for i in range (7):
            drop.showturtle()
            time.sleep(1)
            drop.fd(10)
            drop.hideturtle()
        drop.hideturtle()
        drop.reset()
        drop.lt(180)
        drop.up()
        drop.fd(8)
        drop.lt(90)
        drop.showturtle()
        for i in range (7):
            drop.showturtle()
            time.sleep(1)
            drop.fd(10)
            drop.hideturtle()
        turtle.bye()
        
        


