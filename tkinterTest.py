import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("10x10 Tile Grid")

# Set the window size and background color
GRID_WIDTH = 10
GRID_HEIGHT = 10
tile_size = 30
gap = 5
canvas_size_x = GRID_WIDTH * tile_size + gap * (GRID_WIDTH)
canvas_size_y = GRID_HEIGHT * tile_size + gap * (GRID_HEIGHT)
background_color = "green"

# Create a canvas to draw on
canvas = tk.Canvas(root, width=canvas_size_x, height=canvas_size_y, bg=background_color)
canvas.pack()

# Draw the 10x10 grid
for row in range(GRID_HEIGHT):
    for col in range(GRID_WIDTH):
        x1 = col * (tile_size + gap) + gap
        y1 = row * (tile_size + gap) + gap
        x2 = x1 + tile_size
        y2 = y1 + tile_size
        canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="")

# Start the application
root.mainloop()
