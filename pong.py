# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


while True:
    wn.update()