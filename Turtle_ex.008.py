"""
Exercicios

1) Acrescente cores
2) Mude a largura da linha
3) Aumente a quantidade de linhas
"""

import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(4)
colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'aquamarine', 'plum' ] #1)
for _ in range (12):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(30)
