# TODO 1. extract the colors
# import colorgram
# colors = colorgram.extract('image.jpg',30)
# rgb_colors= []
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# TODO 2.create the HIRST
import random
import turtle as t
t.colormode(255)
tim= t.Turtle()
screen=t.Screen()


tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setheading(190)
tim.fd(250)
tim.setheading(0)
tim.setheading(280)
tim.fd(200)
tim.setheading(0)

colors = [(199, 12, 32), (249, 236, 25), (244, 248, 253), (40, 77, 187), (239, 229, 4), (38, 217, 69), (29, 40, 156), (213, 75, 14), (17, 153, 17), (242, 35, 160), (196, 16, 11), (68, 10, 31), (223, 21, 120), (61, 15, 8), (223, 141, 207), (11, 97, 62), (221, 159, 9), (53, 210, 230), (19, 21, 48), (75, 72, 218), (238, 156, 218), (10, 228, 239), (75, 211, 167), (89, 234, 199)]
number_of_dots = 100
for i in range (1,number_of_dots+1):

         tim.dot(20,random.choice(colors))
         tim.forward(50)
         if i % 10 == 0:
             tim.setheading(90)
             tim.fd(50)
             tim.setheading(180)
             tim.fd(500)
             tim.setheading(0)





screen.exitonclick()