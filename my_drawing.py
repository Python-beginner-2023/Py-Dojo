import turtle as t


def cube(t, x, y, w, h, hand):
    t.goto(x, y)
    t.setheading(0)

    if hand == 'right':
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    elif hand == 'left':
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    else:
        print(f'手性错误: {hand}')


t.setup(900, 600)
cube(t, 10, 10, 300, 200, 'left')
t.done()
