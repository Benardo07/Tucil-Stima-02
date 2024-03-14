from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def create_bezier(control_points: List[Tuple[float, float]], iterations: int) -> List[Tuple[float, float]]:
    if len(control_points) < 2:
        raise ValueError("At least two control points are required")
    bezier_points = []
    bezier_points.append(control_points[0])  # Add the first control point
    find_bezier_points(bezier_points, control_points, 0, iterations)
    bezier_points.append(control_points[-1])  # Ensure the last control point is added
    return bezier_points

def find_bezier_points(bezier_points: List[Tuple[float, float]], control_points: List[Tuple[float, float]], current_iteration: int, iterations: int):
    if current_iteration < iterations:
        # Generate the next level of control points by finding mid-points
        k = 0
        next_level_points = [control_points]
        new_control_points = control_points
        while(k < len(control_points) -1):
            temp = []           
            for i in range(len(new_control_points) - 1):
                temp.append(mid_point(new_control_points[i], new_control_points[i+1]))
                print(mid_point(new_control_points[i], new_control_points[i+1]))

            next_level_points.append(temp)
            new_control_points = temp
            k += 1

        print(next_level_points)
        left_half = []
        right_half = []
        # Recursively refine the curve
        for i in range(len(next_level_points)):
            left_half.append(next_level_points[i][0])
            right_half.append(next_level_points[len(next_level_points) - 1 - i][-1])
        
        find_bezier_points(bezier_points, left_half, current_iteration + 1, iterations)

        bezier_points.append(next_level_points[len(next_level_points) - 1][0])
        
        find_bezier_points(bezier_points, right_half, current_iteration + 1, iterations)

def mid_point(p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
# Contoh penggunaan dengan empat titik kontrol dan iterasi
ctrl_points = [(0, 100), (100, 200), (150, 50),(300,100)]
iterations = 5

bezier_points = create_bezier(ctrl_points, iterations)
print(bezier_points)
# print(bezier_points)

all_points = ctrl_points + bezier_points  # Combine control points and bezier points
all_x = [p[0] for p in all_points]
all_y = [p[1] for p in all_points]

max_x = max(all_x)
max_y = max(all_y)
min_x = min(all_x)
min_y = min(all_y)

x_range = max_x - min_x
y_range = max_y - min_y

# Set a proportional buffer (e.g., 10% of the range)
x_buffer = x_range * 0.1
y_buffer = y_range * 0.1

# Ensure a minimum buffer size to avoid too tight plotting for very small ranges
min_buffer = 0.1  # Adjust as needed for better visuals
x_buffer = max(x_buffer, min_buffer)
y_buffer = max(y_buffer, min_buffer)

# Adjust plot limits dynamically
fig, ax = plt.subplots()
ax.set_xlim(min_x - x_buffer, max_x + x_buffer)
ax.set_ylim(min_y - y_buffer, max_y + y_buffer)

# Plotting remains the same
control_points_line, = ax.plot([p[0] for p in ctrl_points], [p[1] for p in ctrl_points], 'ro-', label='Control Points')
bezier_line, = ax.plot([], [], 'b-', label='Bezier Curve')
ax.legend()

def init():
    bezier_line.set_data([], [])
    return bezier_line,

def animate(i):
    x_vals, y_vals = zip(*bezier_points[:i+1])  # Unpack up to the current frame
    bezier_line.set_data(x_vals, y_vals)
    return bezier_line,

num_frames = len(bezier_points)  # One frame per bezier point

ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, repeat=True, interval=50)  # interval in milliseconds


plt.show()
