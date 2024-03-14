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
        mid_point = []

        for i in range(len(control_points) - 1):
            mid_point.append(mid_point(control_points[i],control_points[i+1]))
        
        
        find_bezier_points(bezier_points, left_half, current_iteration + 1, iterations)
        
        if current_iteration + 1 < iterations:
            bezier_points.append(next_level_points[mid])
        
        find_bezier_points(bezier_points, right_half, current_iteration + 1, iterations)

def mid_point(p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
# Contoh penggunaan dengan empat titik kontrol dan iterasi
ctrl_points = [(0, 100), (100, 200), (150, 50),(300,100)]
iterations = 5

bezier_points = create_bezier(ctrl_points, iterations)

# print(bezier_points)

fig, ax = plt.subplots()

# Adjust plot limits to fit the control points and Bezier curve dynamically
ctrl_points_max_x = max(p[0] for p in ctrl_points)
ctrl_points_max_y = max(p[1] for p in ctrl_points)
ctrl_points_min_x = min(p[0] for p in ctrl_points)
ctrl_points_min_y = min(p[1] for p in ctrl_points)

buffer = 50  # Add some buffer for visibility
ax.set_xlim(ctrl_points_min_x - buffer, ctrl_points_max_x + buffer)
ax.set_ylim(ctrl_points_min_y - buffer, ctrl_points_max_y + buffer)

# Initial drawing: control points and an empty bezier curve
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

ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, repeat=True)

plt.show()
