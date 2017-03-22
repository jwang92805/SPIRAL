from myFunction import *
import turtle

bob=turtle.Turtle()                 #bob and alice variables
alice=turtle.Turtle()
bob.speed(0)
alice.speed(0)
turtle.colormode(255)               #colors from 0-255
turtle.bgcolor("black")             #background color black

multispiral(bob)                    #multispiral function creates 5 different colored spirals
circles(alice,600)                  #circles function creates a number of growing circles that rotate and change color


