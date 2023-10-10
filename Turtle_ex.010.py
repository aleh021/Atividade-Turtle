"""
Exercícios

1) Faça cada quadrado ter uma cor
2) Faça cada quadrado com um formato diferente da tartaruga
3) Faça os quadrados não se tocarem
4) Desenhe um quadrado maior ao redor dos demais quadrados
"""

import turtle

turtle = turtle.Turtle()

for _ in range(4):
    turtle.shape('classic') #2)
    turtle.color('mediumslateblue') #1)
    turtle.forward(100)
    turtle.right(90)

turtle.up() #3)
turtle.backward(100) #3)
turtle.down() #3)

for _ in range(4):
    turtle.shape('square') #2)
    turtle.color('slateblue') #1)
    turtle.right(90)
    turtle.forward(100)

turtle.up() #3)
turtle.forward(100) #3)
turtle.left(90) #3)
turtle.forward(100) #3)
turtle.down() #3)

for _ in range(4):
    turtle.shape('arrow') #2)
    turtle.color('darkslateblue') #1)
    turtle.forward(100)
    turtle.left(90)

turtle.up() #3)
turtle.backward(300) #3)
turtle.down() #3)

for _ in range(4):
    turtle.shape('triangle') #2)
    turtle.color('mediumslateblue') #1)
    turtle.left(90)
    turtle.forward(100)

#4) FAZENDO O QUADRADO MAIOR AO REDOR
# ALINHANDO OP PONTEIRO
turtle.up()
turtle.backward(100)
turtle.left(90)
turtle.backward(200)
turtle.down()

for _ in range(4):
    turtle.shape('circle')
    turtle.color('black')
    turtle.forward(500)
    turtle.right(90)
