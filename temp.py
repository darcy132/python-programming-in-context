import turtle

# 创建一个Turtle对象
t = turtle.Turtle()

# 设置世界坐标系范围
turtle.setworldcoordinates(-1, -1, 10, 10)

# 画一个简单的图形，使用实际坐标系中的坐标
t.penup()
t.goto(-1, -1)
t.pendown()
t.goto(10,10)


# 等待点击关闭窗口
turtle.exitonclick()