import threading
import queue
import turtle

# Create the queue for shapes
shape_queue = queue.Queue()

def create_turtle():
    return turtle.Turtle()

def draw_rectangle():
    turtle = create_turtle()
    turtle.color("purple")
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

def draw_circle():
    turtle = create_turtle()
    turtle.color("pink")
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

def worker():
    while True:
        shape, *args = shape_queue.get()
        if shape == 'rectangle':
            draw_rectangle(*args)
        elif shape == 'circle':
            draw_circle(*args)
        shape_queue.task_done()

# Start the worker thread
thread = threading.Thread(target=worker, daemon=True)
thread.start()

# Queue up the shapes
shape_queue.put(('rectangle',))
shape_queue.put(('circle',))

# Wait for the shapes to be drawn
shape_queue.join()

# Exit the program
turtle.done()
