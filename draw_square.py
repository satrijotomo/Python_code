#! /usr/bin/env python3

import turtle

bgcol = "yellow"
reccol = "blue"
circol = "red"
tricol = "white"

def draw_shape():
    window = turtle.Screen()
    window.bgcolor(bgcol)

    drawme = turtle.Turtle()
    drawme.shape("turtle")
    drawme.speed(1)
    drawme.color(reccol)

    i = 0
    while i <= 3:
        drawme.forward(75)
        drawme.left(90)
        i = i +1


    roni = turtle.Turtle()
    roni.shape("turtle")
    roni.speed(1)
    roni.color(circol)
    roni.circle(50)

    wowo = turtle.Turtle()
    wowo.shape("arrow")
    wowo.speed(1)
    wowo.color(tricol)

    i = 0
    while i <= 2:
        drawme.forward(75)
        drawme.right(120)
        i = i +1


    window.exitonclick()


draw_shape()

