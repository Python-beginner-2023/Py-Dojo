import turtle as t

t.setup(600, 400)

def my_draw(r):
    t.circle(r)
    t.circle(r)   # 绘制半径100
    t.circle(r, 360, 8)   # 绘制半径100的八边形
    t.circle(r, 360, 4)   # 绘制对角线100的正方形

my_draw(100)
my_draw(150)
my_draw(200)

t.done()
