n=input()
if(n=='analog clock'):
    import turtle
    import time
    wndw = turtle.Screen()
    wndw.bgcolor("light blue")
    wndw.setup(width=600, height=600)
    wndw.title("Analogue Clock")
    wndw.tracer(0)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)
    pen1= turtle.Turtle()
    pen1.write("SRM UNIVERSITY",font=("Calibiri",20,"bold"),align="center")
    def draw_clock(hr, mn, sec, pen):
        pen.up()
        pen.goto(0, 210)
        pen.setheading(180)
        pen.color("Black")
        pen.pendown()
        pen.circle(210)
        pen.up()
        pen.goto(0, 0)
        pen.setheading(90)
        for _ in range(12):
            pen.fd(190)
            pen.pendown()
            pen.fd(20)
            pen.penup()
            pen.goto(0, 0)
            pen.rt(30)
            hands = [("black", 80, 12), ("blue", 150, 60), ("red", 110, 60)]
            time_set = (hr, mn, sec)
        for hand in hands:
            time_part = time_set[hands.index(hand)]
            angle = (time_part/hand[2])*360
            pen.penup()
            pen.goto(0, 0)
            pen.color(hand[0])
            pen.setheading(90)
            pen.rt(angle)
            pen.pendown()
            pen.fd(hand[1])
    while True:
        hr = int(time.strftime("%I"))
        mn = int(time.strftime("%M"))
        sec = int(time.strftime("%S"))
        draw_clock(hr, mn, sec, pen)
        wndw.update()
        time.sleep(1)
        pen.clear()
    wndw.mainloop()
elif(n=='digital clock'):
    
    from tkinter import * 
    from tkinter.ttk import *
    from time import strftime
    root = Tk()
    root.title('Clock')
  
    def time():
        
        string = strftime('%H:%M:%S %p')
        lbl.config(text = string)
        lbl.after(1000, time)

    lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
    lbl.pack(anchor = 'center')
    time()
  
    mainloop()
else:
    print("none")