import turtle
turtle.title("My cute little turtle")
turtle.bgcolor("Grey")
s = turtle.getscreen()
t = turtle.Turtle()
u = input("Would you like to draw a shape?  Type yes or no: ")
if u == "yes":
    t.circle(50)
else:
    print("Okay")
turtle.mainloop()