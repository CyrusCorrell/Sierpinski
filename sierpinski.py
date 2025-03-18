import turtle
import time as t
from PIL import Image
import numpy as np
def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, my_turtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, colormap[degree], my_turtle)
    if degree > 0:
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   degree-1, my_turtle)
        sierpinski([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                   degree-1, my_turtle)
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                   degree-1, my_turtle)
    

def draw_mandelbrot(my_turtle, width, height, x_min, x_max, y_min, y_max, max_iter):
    for x in range(width):
        for y in range(height):
            c = complex(x_min + (x / width) * (x_max - x_min),
                        y_min + (y / height) * (y_max - y_min))
            m = mandelbrot(c, max_iter)
            color = 255 - int(m * 255 / max_iter)   # Normalize color to 0-255
            my_turtle.goto(x - width // 2, y - height // 2)
            my_turtle.dot(1, (color, color, color))

def draw_sierpinski(my_turtle,depth=3):
    my_turtle.clear()   # Clear the screen before drawing
    my_points = [[-200, -100], [0, 200], [200, -100]]
    sierpinski(my_points, depth, my_turtle)

def draw_mandelbrot_fractal(my_turtle):
    my_turtle.clear()
    draw_mandelbrot(my_turtle, 100, 100, -2.0, 1.0, -1.5, 1.5, 100)


def draw_sierpinski_grid(my_turtle):
    my_points = [[-200, -100], [0, 200], [200, -100]]
    for i in range(7):
        my_turtle.clear()
        my_turtle.penup()
        my_turtle.goto(0, 250)
        total_triangle_count =0
        for j in range(1,i+1):
            total_triangle_count += np.power(3,j)
        total_triangle_count+=1
        my_turtle.write(f"Drawing Sierpinski Triangle of degree {i}\nTotal Triangle count: {total_triangle_count}", align="center", font=("Arial", 16, "bold"))
        my_turtle.goto(0, 0)
        my_turtle.pendown()
        sierpinski(my_points, i, my_turtle)
        t.sleep(2)

def setup_buttons(my_turtle, my_win):
    button_sierpinski = turtle.Turtle()
    button_sierpinski.penup()
    button_sierpinski.goto(-100, -250)
    button_sierpinski.write("Sierpinski", align="center", font=("Arial", 12, "bold"))
    button_sierpinski.goto(-100, -270)
    button_sierpinski.shape("square")
    button_sierpinski.shapesize(2, 5)
    button_sierpinski.fillcolor("lightblue")
    button_sierpinski.onclick(lambda x, y: draw_sierpinski(my_turtle, int(turtle.textinput("Input", "Select depth (0-6): "))))

    button_sierpinski_grid = turtle.Turtle()
    button_sierpinski_grid.penup()
    button_sierpinski_grid.goto(100, -250)
    button_sierpinski_grid.write("Sierpinski Grid", align="center", font=("Arial", 12, "bold"))
    button_sierpinski_grid.goto(100,-270)
    button_sierpinski_grid.shape("square")
    button_sierpinski_grid.shapesize(2, 5)
    button_sierpinski_grid.fillcolor("lightblue")
    button_sierpinski_grid.onclick(lambda x, y: draw_sierpinski_grid(my_turtle))
    '''
    button_mandelbrot = turtle.Turtle()
    button_mandelbrot.penup()
    button_mandelbrot.goto(100, -250)
    button_mandelbrot.write("Mandelbrot", align="center", font=("Arial", 12, "bold"))
    button_mandelbrot.goto(100, -270)
    button_mandelbrot.shape("square")
    button_mandelbrot.shapesize(2, 5)
    button_mandelbrot.fillcolor("lightblue")
    button_mandelbrot.onclick(lambda x, y: draw_mandelbrot_fractal(my_turtle))
    '''
    #my_win.listen()
    my_win.exitonclick()

def save_screen_as_image(my_win, filename):
    canvas = my_win.getcanvas()
    canvas.postscript(file=filename + ".eps")
    try:
        img = Image.open(filename + ".eps")
        img.save(filename + ".png", "png")
    except ImportError:
        print("PIL module not found. Install it to convert EPS to PNG.")
def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_win.colormode(255)
    #draw_sierpinski(my_turtle)
    #setup_buttons(my_turtle,my_win)
    my_win.title("Fractal Drawer")
    my_win.bgcolor("lightgray")
    my_turtle.hideturtle()
    my_turtle.speed(0)
    setup_buttons(my_turtle, my_win)
    ''''
        my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_win.title("Sierpinski Triangle")
    my_win.bgcolor("lightgray")
    my_turtle.hideturtle()
    my_turtle.speed(0.01)
    my_turtle.penup()
    my_turtle.goto(0, 250)
    my_turtle.write("Drawing Sierpinski Triangle", align="center", font=("Arial", 16, "bold"))
    my_turtle.goto(0, 0)
    my_turtle.pendown()
    my_points = [[-200, -100], [0, 200], [200, -100]]
    sierpinski(my_points, 5, my_turtle)
    my_win.exitonclick()
    '''
if __name__ == "__main__":
    main()