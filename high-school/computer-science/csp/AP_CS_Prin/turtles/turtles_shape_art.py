import turtle
import time
t = turtle.Turtle()
time.sleep(5)
def spiral(iterations, d, a, direction='left'):
    for i in range(iterations * 4):
        t.forward(d)
        if direction == 'right':
            t.right(a)
        else:
            t.left(a)

spiral(15, 100, 101, 'right')
