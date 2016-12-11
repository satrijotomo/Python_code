#! /usr/bin/env python3

import turtle
import time

bgcol = "yellow"
reccol = "blue"
circol = "red"
tricol = "white"

def draw_rect(rectang):
    i = 0
    while i <= 3:
        rectang.forward(100)
        rectang.right(90)
        i = i + 1

def draw_triang(triang):
    i = 0
    while i <= 2:
        triang.forward(100)
        triang.right(120)
        i = i + 1

def draw_shape():
    window = turtle.Screen()
    window.bgcolor(bgcol)

    drawme = turtle.Turtle()
    drawme.shape("turtle")
    drawme.speed(0)
    drawme.color(reccol)

    l = 0
    while l <= 35:
        draw_triang(drawme)
        drawme.right(10)
        l = l + 1

    j=0

    while j <= 35:
        draw_rect(drawme)
        drawme.right(10)
        j = j + 1
    drawme.right(90)
    drawme.forward(300)
    time.sleep(5)

draw_shape()
