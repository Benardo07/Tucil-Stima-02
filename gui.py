from pathlib import Path
from tkinter import Tk, Canvas, Button,font
from tkinter import Entry
from main7 import create_bezier
from BruteForce import create_bezier_brute_force
from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import sys
import atexit
import time
beziertime = ""
bftime = ""
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\asus\Documents\Strategi-Algoritma-Sem4\Tucil2_Stima\Tkinter-Designer\build\assets\frame0")
def close_window_and_cleanup():
    plt.close('all') 
    window.destroy() 
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Draw a rounded rectangle on the canvas."""
    points = [
        x1+radius, y1,
        x1+radius, y1,
        x2-radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1+radius,
        x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)
def create_rounded_entry(canvas, x, y, width, height, radius, entry_options, frame_options):
    frame = create_rounded_rectangle(canvas, x, y, x + width, y + height, radius, **frame_options)
    entry = Entry(canvas, bd=0, highlightthickness=0, **entry_options)
    entry.place(x=x + radius, y=y + (height - entry.winfo_reqheight()) // 2, width=width - 2 * radius)
    entry.insert(0, "  ")
    return entry
def button_click():
    global beziertime, bftime
    try:
        control_points_str = point_number_entry.get().strip()
        ctrl_points = [tuple(map(int, point.strip().strip('()').split(','))) for point in control_points_str.split('),(')]
        iterations = int(number_of_iterations_entry.get().strip())
        if len(ctrl_points) < 2:
            raise ValueError("Number of points must be at least 2")
        if iterations < 1:
            raise ValueError("Number of iterations must be at least 1")
        start = time.time()
        bezier_points, iteration_points = create_bezier(ctrl_points, iterations)
        end = time.time()
        beziertime = end-start
        beziertime = f"Time: {beziertime:.5f} s"
        start = time.time()
        brute_force_bezier_points = create_bezier_brute_force(ctrl_points, iterations)
        end = time.time()
        bftime = end-start
        bftime = f"Time: {bftime:.5f} s"
        all_points = ctrl_points + bezier_points
        all_x = [p[0] for p in all_points]
        all_y = [p[1] for p in all_points]
        x_buffer, y_buffer = 0.1, 0.1
        fig, ax = plt.subplots()
        ax.set_xlim(min(all_x) - x_buffer, max(all_x) + x_buffer)
        ax.set_ylim(min(all_y) - y_buffer, max(all_y) + y_buffer)
        ax.plot([p[0] for p in ctrl_points], [p[1] for p in ctrl_points], 'ro-', label='Control Points', markersize=8)   
        bezier_line, = ax.plot([], [], 'b-', label='Bezier Curve')
        bezier_points_line, = ax.plot([], [], 'bo', label='Bezier Points', markersize=4) 
        ax.legend()
        def init():
            bezier_line.set_data([], [])
            bezier_points_line.set_data([], [])
            return bezier_line, bezier_points_line
        def animate(i):
            if i < len(iteration_points):
                x_vals, y_vals = zip(*iteration_points[i])
                bezier_line.set_data(x_vals, y_vals)
                bezier_points_line.set_data(x_vals, y_vals)  # Update the Bézier points
            return bezier_line, bezier_points_line

        # Create the animation
        ani = animation.FuncAnimation(fig, animate, frames=len(iteration_points), init_func=init, blit=True, repeat=True, interval=250)
        fig2, ax2 = plt.subplots()
        ax2.plot([p[0] for p in ctrl_points], [p[1] for p in ctrl_points], 'ro-', label='Control Points')
        brute_force_bezier_line, = ax2.plot([], [], 'g-', label='Brute Force Bezier Curve')
        ax2.legend()
        def animate_brute_force(i):
            x_vals, y_vals = zip(*brute_force_bezier_points[:i + 1])
            brute_force_bezier_line.set_data(x_vals, y_vals)
            return brute_force_bezier_line,
        ani2 = animation.FuncAnimation(fig2, animate_brute_force, frames=len(brute_force_bezier_points), blit=True, interval=50)
        canvas1 = FigureCanvasTkAgg(fig, master=window)
        plot_widget1 = canvas1.get_tk_widget()
        plot_widget1.place(x=431, y=180, width=507, height=459)
        canvas1.draw()
        canvas2 = FigureCanvasTkAgg(fig2, master=window)
        plot_widget2 = canvas2.get_tk_widget()
        plot_widget2.place(x=960, y=180, width=507, height=459) 
        canvas2.draw()
        canvas.itemconfig(bezier_time_text, text=beziertime)
        canvas.itemconfig(brute_force_time_text, text=bftime)

    except ValueError as e:
        print("Error:", e)


window = Tk()
window.geometry("1500x1000")
window.configure(bg="#32746D")
canvas = Canvas(
    window,
    bg="#32746D",
    height=750,
    width=1550,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
font.families()
bezier_time_text = canvas.create_text(
    431 + 253.5, 
    160,  
    anchor="center",
    text=beziertime,
    fill="#9EC5AB",
    font=("Batang Che", 24, "bold")
)

brute_force_time_text = canvas.create_text(
    960 + 253.5, 
    160,  
    anchor="center",
    text=bftime,
    fill="#9EC5AB",
    font=("Batang Che", 24, "bold")
)
#Plot
create_rounded_rectangle(
    canvas,
    431.0,
    180.0,
    938.0,
    639.0,
    radius=100, 
    fill="#104F55",
    outline=""
)
create_rounded_rectangle(
    canvas,
    960.0,
    180.0,
    1467.0,
    639.0,
    radius=100, 
    fill="#104F55",
    outline=""
)
entry_options = {
    'fg': '#011502',
    'bg': '#9EC5AB',
    'font': ("Batang Che", 24, "bold")
}

frame_options = {
    'fill': '#9EC5AB',
    'outline': ''
}
point_number_entry = create_rounded_entry(
    canvas,
    x=21.0, y=174.0, width=300, height=50, radius=40,
    entry_options=entry_options,
    frame_options=frame_options
)
number_of_iterations_entry = create_rounded_entry(
    canvas,
    x=21.0, y=334.0, width=300, height=50, radius=40,
    entry_options=entry_options,
    frame_options=frame_options
)
canvas.create_rectangle(
    0,
    0,
    1553.5,
    97.5,
    fill="#011502",
    outline=""
)

canvas.create_text(
    21.0 + 25,
    0.0 + 25,
    anchor="nw",
    text="BEZIER",
    fill="#9EC5AB",
    font=("Batang Che", 36, "bold")
)

canvas.create_text(
    21.0,
    114.0 + 15,
    anchor="nw",
    text="Point Number:",
    fill="#9EC5AB",
    font=("Batang Che", 24, "bold")
)

canvas.create_text(
    21.0,
    284.0,
    anchor="nw",
    text="Number of Iterations:",
    fill="#9EC5AB",
    font=("Batang Che", 24, "bold")
)

button_width = 200
button_height = 70
button_x = 21.0
button_y = 454.0
button_radius = 20  # Adjust the radius for roundness
create_rounded_rectangle(
    canvas,
    button_x, button_y,
    button_x + button_width, button_y + button_height,
    button_radius,
    fill="#011502",
    outline="",
    tags="button_bg_1"
)
canvas.create_text(
    button_x + button_width / 2, button_y + button_height / 2,
    text="Generate",
    fill="#9EC5AB",
    font=("Batang Che", 24, "bold"),
    tags="button_text_1"
)
canvas.tag_bind("button_bg_1", "<Enter>", lambda event: button_hover(event, "button_bg_1", "button_text_1"))
canvas.tag_bind("button_bg_1", "<Leave>", lambda event: button_leave(event, "button_bg_1", "button_text_1"))
canvas.tag_bind("button_text_1", "<Enter>", lambda event: button_hover(event, "button_bg_1", "button_text_1"))
canvas.tag_bind("button_text_1", "<Leave>", lambda event: button_leave(event, "button_bg_1", "button_text_1"))
canvas.tag_bind("button_bg_1", "<Button-1>", lambda event: button_click())
canvas.tag_bind("button_text_1", "<Button-1>", lambda event: button_click())
def button_hover(event, bg_tag, text_tag):
    canvas.itemconfig(bg_tag, fill="#88BDA0")
    canvas.itemconfig(text_tag, fill="black")
def button_leave(event, bg_tag, text_tag):
    canvas.itemconfig(bg_tag, fill="#011502")
    canvas.itemconfig(text_tag, fill="#9EC5AB")
window.protocol("WM_DELETE_WINDOW", close_window_and_cleanup)
window.bind('<Escape>', lambda event: close_window_and_cleanup())
atexit.register(close_window_and_cleanup)
window.mainloop()
