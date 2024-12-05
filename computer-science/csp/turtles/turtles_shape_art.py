import turtle

t = turtle.Turtle()

def spiral(iterations, d, a, direction='left'):
    for i in range(iterations * 4):
        t.forward(d)
        if direction == 'right':
            t.right(a)
        else:
            t.left(a)

spiral(100, 75, 81, 'right')
