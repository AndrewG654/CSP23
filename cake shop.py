#cake shop.py

#   Cake shop.py


import turtle as trtl

wn = trtl.Screen()

# create turtle object
painter = trtl.Turtle()
#background
trtl.Screen().bgcolor("lightblue")
for background in range(1):
    painter.hideturtle()
    painter.speed(0)
    painter.color("papayawhip")
    painter.pensize(30)
    painter.penup()
    painter.goto(-1000, -280)
    painter.pendown()
    painter.begin_fill()
    painter.forward(2000)
    painter.right(90)
    painter.forward(500)
    painter.right(90)
    painter.forward(2000)
    painter.right(90)
    painter.forward(500)
    painter.end_fill()
    painter.penup()
    painter.color("pink")
    painter.goto (0, -260)
    painter.pendown()
    painter.begin_fill()
    painter.right(90)
    painter.forward(400)
    painter.right(90)
    painter.forward(60)
    painter.right(90)
    painter.forward(800)
    painter.right(90)
    painter.forward(60)
    painter.right(90)
    painter.forward(400)
    painter.end_fill()




# add variables

toppings = []
place = -200
layers = 0
cake_l = 600
ice_l = 300
ice_h = -200
icing = "on"
cakebuild = "yes"
flavor = "notchosen"
cake_color = "choose"
question = "notchosen"
candl_num = 8
candl_l = 300




while(cakebuild == "yes"):

    # cake flavor
    while(flavor == "notchosen"):
        print("what flavor cake do you want?")
        print("vanilla or chocolate")
        cake_flavor = input("")
        
        if (cake_flavor == "vanilla"):
            print("cool")
            flavor = "chosen"
            cake_color = "yellow"
        elif (cake_flavor == "chocolate"):
            print("good")
            flavor = "chosen"
            cake_color = "brown"
        else:
            print("that's not a flavor try again")
    
    #how many layers
    while(layers == 0):
        print("how many layers do you want?")
        layers = int(input(""))
        if(layers < 6):
            for build in range(layers):
                shape = ((cake_l, 0), (cake_l, 80), (0,80), (0,0))
                trtl.register_shape("rectangle",shape)
                
                base = trtl.Turtle("rectangle")
                base.hideturtle()
                base.penup()
                base.right(90)
                base.fillcolor(cake_color)
                base.goto(cake_l / 2,1000)
                base.showturtle()
                base.goto(cake_l / 2,place)
                
                place = place + 80
                cake_l = cake_l - 120
        else:
            print("too many layers, max 6")
            layers = 0

    #icing
    shape = ((0,0), (120,0), (130,6), (136,12), (142,24), (144,30), (150,42), (156,54), (162, 60), (-42,60), (-36,54), (-30,42), (-24,30), (-22,24), (-15,12), (-10,6))
    trtl.register_shape("bowl", shape)
    bowl = trtl.Turtle("bowl")
    bowl.hideturtle()
    bowl.penup()
    bowl.right(270)
    bowl.fillcolor("antiquewhite")
    bowl.goto(120,-1000)
    shape = ((0,0), (120,0), (130,-3), (120,-6), (40,-6), (20,-20), (0,-6), (0,0))
    trtl.register_shape("spoon", shape)
    spoon = trtl.Turtle("spoon")
    spoon.hideturtle()
    spoon.fillcolor("silver")
    spoon.left(90)
    

    while (icing == "on"):
        bowl.showturtle()
        bowl.forward(700)
        spoon.showturtle()
        spoon.penup()
        print("what color icing do you want?")
        print("pink, red, orange, yellow, green, blue, purple, brown, white, black")
        ice_color = str(input(""))

        for spread in range(layers):
            spoon.pensize(20) 
            spoon.pencolor(ice_color)
            spoon.goto(180,-200)
            spoon.goto(180,-280)
            spoon.goto(180,-200)
            spoon.goto(-ice_l,ice_h-5)
            spoon.pendown()
            spoon.goto(ice_l,ice_h-5)
            spoon.penup()
            ice_l = ice_l - 60
            ice_h = ice_h + 80
        bowl.backward(500)
        spoon.hideturtle()
        icing = "off"

    # unadded candles
    shape = ((0,0), (15,0), (15,60), (0,60))
    trtl.register_shape("candle", shape)
    candle = trtl.Turtle("candle")
    candle.hideturtle()
    candle.left(90)


    '''
    while(question == "notchosen"):
        print("do you want candles?")
        print("y or n")
        candle = input("")
        if (candle == "y"):
            print("what color?")
            color = input("")
            candle.fillcolor(color)
            candle.goto(0,1000)
            ice_h = -200
            for cand in range(layers):
                for candl in range(candl_num):
                    
                    candle.goto()
        elif(candle == "n"):
            question = "chosen"
    '''



    print("Your cake looks good! Hope you like it! Goodbye")
    cakebuild = "no"
    



wn.mainloop()