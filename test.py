import tkinter as tk
import math

def animate_bar():
    global angle
    angle -= 0.5  # Increment the angle by 1 degree

    # Calculate the coordinates of the moving endpoint of the bar
    x2 = center_x + math.cos(math.radians(angle)) * bar_length
    y2 = center_y - math.sin(math.radians(angle)) * bar_length
    
    # Update the coordinates of the bar
    canvas.coords(bar, center_x, center_y, x2, y2)
    
    # Schedule the next animation frame
    root.after(1, animate_bar)

# Create the main window
root = tk.Tk()
root.title("Animated Bar Example")

# Create the canvas
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Set the center of the canvas
center_x = canvas_width // 2
center_y = canvas_height // 2

# Set the length of the bar
bar_length = 150

# Calculate the initial coordinates of the moving endpoint of the bar
initial_x = center_x + math.cos(math.radians(90)) * bar_length
initial_y = center_y - math.sin(math.radians(90)) * bar_length

# Create the bar
bar = canvas.create_line(center_x, center_y, initial_x, initial_y, width=3, fill="red")

# Initialize the angle
angle = 90

# Start the animation
animate_bar()

# Start the Tkinter event loop
root.mainloop()