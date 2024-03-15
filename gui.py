from pathlib import Path
from tkinter import Tk, Canvas, Button
from tkinter import Entry
from main5 import create_bezier
from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\asus\Documents\Strategi-Algoritma-Sem4\Tucil2_Stima\Tkinter-Designer\build\assets\frame0")

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
    try:
        control_points_str = point_number_entry.get().strip()
        control_points = [tuple(map(int, point.strip().strip('()').split(','))) for point in control_points_str.split('),(')]

        iterations = int(number_of_iterations_entry.get().strip())

        if len(control_points) < 2:
            raise ValueError("Number of points must be at least 2")
        if iterations < 1:
            raise ValueError("Number of iterations must be at least 1")

        bezier_points = create_bezier(control_points, iterations)

        fig, ax = plt.subplots()
        ax.plot([p[0] for p in control_points], [p[1] for p in control_points], 'ro-', label='Control Points')
        bezier_line, = ax.plot([], [], 'b-', label='Bezier Curve')
        ax.legend()

        def init():
            bezier_line.set_data([], [])
            return bezier_line,

        def animate(i):
            x_vals, y_vals = zip(*bezier_points[:i + 1])
            bezier_line.set_data(x_vals, y_vals)
            return bezier_line,

        ani = animation.FuncAnimation(fig, animate, frames=len(bezier_points), init_func=init, blit=True, repeat=True, interval=50)

        canvas = FigureCanvasTkAgg(fig, master=window)
        plot_widget = canvas.get_tk_widget()
        plot_widget.place(x=431, y=130, width=537, height=389)
        canvas.draw()
    except ValueError as e:
        print("Error:", e)


window = Tk()

window.geometry("1000x550")
window.configure(bg="#32746D")

canvas = Canvas(
    window,
    bg="#32746D",
    height=550,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

#Plot
create_rounded_rectangle(
    canvas,
    431.0,
    130.0,
    968.0,
    519.0,
    radius=100, 
    fill="#104F55",
    outline=""
)
entry_options = {
    'bg': '#011502',
    'fg': '#9EC5AB',
    'font': ("Times", 24, "bold")
}

frame_options = {
    'fill': '#011502',
    'outline': ''
}
point_number_entry = create_rounded_entry(
    canvas,
    x=21.0, y=174.0, width=200, height=50, radius=40,
    entry_options=entry_options,
    frame_options=frame_options
)
number_of_iterations_entry = create_rounded_entry(
    canvas,
    x=21.0, y=334.0, width=200, height=50, radius=40,
    entry_options=entry_options,
    frame_options=frame_options
)
canvas.create_rectangle(
    0,
    0,
    1003.5,
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
    font=("Times", 36, "bold")
)

canvas.create_text(
    21.0,
    114.0 + 15,
    anchor="nw",
    text="Point Number:",
    fill="#9EC5AB",
    font=("Times", 24, "bold")
)

canvas.create_text(
    21.0,
    284.0,
    anchor="nw",
    text="Number of Iterations:",
    fill="#9EC5AB",
    font=("Times", 24, "bold")
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
    font=("Times", 24, "bold"),
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

window.mainloop()
