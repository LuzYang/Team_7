import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to create a rotation matrix for rotating the cube
def rotation_matrix(axis, angle):
    """
    Returns a rotation matrix for rotating an object around the given axis by the given angle (in degrees).
    """
    angle = np.radians(angle)
    if axis == 'x':
        return np.array([
            [1, 0, 0],
            [0, np.cos(angle), -np.sin(angle)],
            [0, np.sin(angle), np.cos(angle)]
        ])
    elif axis == 'y':
        return np.array([
            [np.cos(angle), 0, np.sin(angle)],
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)]
        ])
    elif axis == 'z':
        return np.array([
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]
        ])

# Function to plot and rotate the cube
def rotate_cube():
    try:
        # Get the angle and axis from user input
        angle = float(angle_entry.get())
        axis = axis_var.get()
        
        # Define the original cube coordinates (8 points)
        cube_points = np.array([
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1]
        ])
        
        # Define the edges of the cube (pairs of points)
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom square
            (4, 5), (5, 6), (6, 7), (7, 4),  # Top square
            (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical connections
        ]

        # Apply rotation
        rotation_mat = rotation_matrix(axis, angle)
        rotated_cube = cube_points.dot(rotation_mat.T)

        # Clear previous plot
        ax.clear()
        ax.set_title("Rotated Cube in 3D Coordinates")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")
        
        # Set consistent axis limits
        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        ax.set_zlim([-2, 2])

        # Set the viewpoint to improve visualization
        ax.view_init(elev=30, azim=30) 

        # Draw the cube edges
        for edge in edges:
            p1, p2 = rotated_cube[edge[0]], rotated_cube[edge[1]]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'b-')

        # Redraw the canvas
        canvas.draw()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the rotation angle.")

# Initialize Tkinter window
root = tk.Tk()
root.title("3D Cube Rotation")

# Create a Matplotlib figure and axis for 3D plotting
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

# Create canvas to display Matplotlib figure in Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Input controls for angle and axis
tk.Label(root, text="Rotation Angle (in degrees):").pack(pady=5)
angle_entry = tk.Entry(root)
angle_entry.pack(pady=5)

tk.Label(root, text="Choose Rotation Axis:").pack(pady=5)
axis_var = tk.StringVar(value='x')
tk.Radiobutton(root, text="X-axis", variable=axis_var, value='x').pack(pady=5)
tk.Radiobutton(root, text="Y-axis", variable=axis_var, value='y').pack(pady=5)
tk.Radiobutton(root, text="Z-axis", variable=axis_var, value='z').pack(pady=5)

# Button to trigger the cube rotation
rotate_button = tk.Button(root, text="Rotate Cube", command=rotate_cube)
rotate_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
