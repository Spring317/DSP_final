import tkinter as tk

def animate_bar():
    canvas.move(bar, 3, 0)  # Move the bar 3 pixels to the right
    if canvas.coords(bar)[2] < WIDTH:
        root.after(50, animate_bar)  # Repeat the animation after 50 milliseconds

# Create the main window
root = tk.Tk()
root.title("Running Bar Animation")

# Set the dimensions of the canvas
WIDTH, HEIGHT = 400, 100
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Create the running bar
bar_width = 100
bar_height = 20
bar = canvas.create_rectangle(0, 0, bar_width, bar_height, fill="blue")

# Start the animation
animate_bar()

# Start the Tkinter event loop
root.mainloop()