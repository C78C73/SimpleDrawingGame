import tkinter, random, turtle, os
from tkinter import messagebox

window = tkinter.Tk()
window.geometry("800x800")
window.title("Turtle Drawing")

canvas = tkinter.Canvas(window, width=1500, height=800)
canvas.pack()

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
t.pendown()
t.speed(25)
t.shape("circle")

colors = ['red', 'purple', 'brown', 'black', 'yellow', 'orange', 'grey', 'blue']

def move_up():
    randColor = random.choice(colors)
    t.color(randColor)
    t.setheading(90)
    t.forward(100)

def turn_left():
    randColor = random.choice(colors)
    t.color(randColor)
    t.setheading(180)
    t.forward(100)

def move_backward():
    randColor = random.choice(colors)
    t.color(randColor)
    t.setheading(270)
    t.forward(100)

def turn_right():
    randColor = random.choice(colors)
    t.color(randColor)
    t.setheading(0)
    t.forward(100)

def undo():
    t.undo()

def save_drawing():
    try:
        file_path = "turtle_drawing.ps"
        canvas.postscript(file=file_path, colormode='color')
        messagebox.showinfo("Save Successful", f"Drawing saved as {file_path}")
    except Exception as e:
        messagebox.showerror("Save Error", f"Error saving drawing: {e}")

def exit_program():
    window.destroy()

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(move_backward, "Down")
screen.onkey(turn_right, "Right")
screen.onkey(undo, "u")
screen.onkey(exit_program, "q")

save_button = tkinter.Button(window, text="Save Drawing", command=save_drawing)
save_button.pack()

window.mainloop()