import turtle as t


def cube(t, x, y, w, h, hand):
    t.up()
    t.goto(x, y)
    t.setheading(0)

    t.down()

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

    t.up()


t.setup(900, 600)

# cube(t, 10, 10, 300, 180, 'right')
# cube(t, -300-10, 10, 300, 180, 'right')
# cube(t, 10, -200-10, 300, 180, 'right')
# cube(t, -300-10, -200-10, 300, 180, 'right')

# for i in range(5):
#     cube(t, i*10, i*10, 300, 180, 'right')

# t.done()


def turn_right_line(t, length):
    if length < 0:
        return

    t.right(90)
    t.forward(length)

    turn_right_line(t, length-10)


t.setup(900, 600)
t.down()

turn_right_line(t, 200)

t.done()

