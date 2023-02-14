from turtle import*
speed('fastest')
side=10
size=50
for i in range(side):
    fd(size)
    lt(360/side)
    write(i)
hideturtle()
mainloop()