"""
Exercícios

1) Mude/defina a forma da tartaruga
2) Mude a ordem das cores
3) Mude a largura da linha
4) Faça a tartaruga desenhar dois quadrados
"""

import turtle

turtle = turtle.Turtle()
turtle.pensize(5)
turtle.shape('circle') #1)

for _ in range(2):
    for color in ['black', 'red', 'pink', 'blue']: #2)
        turtle.color(color)
        turtle.forward(100)
        turtle.right(90)
    turtle.up()
    turtle.right(90)
    turtle.forward(150)
    turtle.down()
