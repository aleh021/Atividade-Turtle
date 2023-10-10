"""
Exercicios:

1) Faça cada passo da tartaruga ter uma cor diferente
2) Aumente/diminua o diâmetro do círculo
"""

import turtle
import random
turtle = turtle.Turtle()
cores=['yellow', 'black']

turtle.speed(100)

for c in range(1080):
    yeblackow=random.choice(cores) #1)
    turtle.color(yeblackow)
    turtle.forward(3) #2
    turtle.right(1) #2
