"""
Exercícios

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope
"""

import turtle
import random

turtle = turtle.Turtle()
cores=['black', 'blue', 'aquamarine'] #3

for _ in [1, 2, 3]:
    turtle.color(random.choice(cores))
    turtle.shape('triangle') #2)
    turtle.forward(100) #4)
    turtle.right(120)
turtle.up()
turtle.backward(50)
turtle.down()
for _ in [1, 2, 3, 4]:
    turtle.color(random.choice(cores))
    turtle.shape('circle') #2)
    turtle.forward(200)
    turtle.right(90)
