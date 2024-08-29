import turtle

# 初始化画布
window = turtle.Screen()
window.bgcolor("white")

# 创建一个turtle对象
flower = turtle.Turtle()
flower.speed(1)  # 设置绘画速度

# 绘制花朵的主体部分
for _ in range(8):  # 画8个花瓣
    flower.forward(50)
    flower.left(45)
    flower.forward(50)
    flower.right(90)
    flower.forward(50)
    flower.left(45)
    flower.forward(50)
    flower.right(180)

# 绘制花的中心
flower.penup()  # 抬笔
flower.goto(0, -30)  # 移动到花心位置
flower.pendown()  # 落笔
flower.color("yellow")
flower.begin_fill()  # 开始填充颜色
flower.circle(20)  # 画圆作为花心
flower.end_fill()  # 结束填充

# 隐藏turtle图标
flower.hideturtle()

# 完成绘制后保持窗口打开
window.mainloop()
