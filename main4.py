from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def create_bezier(p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float], iterations: int) -> List[Tuple[float, float]]:
    bezier_points = []
    bezier_points.append(p1)  # Add the first control point
    find_bezier_points(bezier_points, p1, p2, p3, 0, iterations)
    bezier_points.append(p3)  # Add the last control point
    return bezier_points

def find_bezier_points(bezier_points: List[Tuple[float, float]], p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float], current_iteration: int, iterations: int):
    if current_iteration < iterations:
        mid_point1 = mid_point(p1, p2)
        mid_point2 = mid_point(p2, p3)
        mid_point3 = mid_point(mid_point1, mid_point2)  # The next control point
        current_iteration += 1
        find_bezier_points(bezier_points, p1, mid_point1, mid_point3, current_iteration, iterations)  # Left branch
        bezier_points.append(mid_point3) 
        find_bezier_points(bezier_points, mid_point3, mid_point2, p3, current_iteration, iterations)  # Right branch


def mid_point(p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)



ctrl_points = [(25, 70), (95, 379), (250, 90)]
iterations = 1

bezier_points = create_bezier(ctrl_points[0],ctrl_points[1],ctrl_points[2], iterations)

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

# from typing import List, Tuple
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import numpy as np

# # Adjusted to track and animate Q0, Q1 lines for each Bezier point
# def create_bezier(p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float], iterations: int):
#     bezier_data = []  # Stores (Bezier point, Q0, Q1)
#     find_bezier_points(bezier_data, p1, p2, p3, 0, iterations)
#     return bezier_data

# def find_bezier_points(bezier_data, p1, p2, p3, current_iteration, iterations):
#     if current_iteration < iterations:
#         Q0 = mid_point(p1, p2)
#         Q1 = mid_point(p2, p3)
#         R = mid_point(Q0, Q1)
        
#         if current_iteration == iterations - 1:
#             # On the final iteration, store Bezier point with its generating Q points
#             bezier_data.append((R, Q0, Q1))
#         else:
#             current_iteration += 1
#             find_bezier_points(bezier_data, p1, Q0, R, current_iteration, iterations)
#             find_bezier_points(bezier_data, R, Q1, p3, current_iteration, iterations)

# def mid_point(p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
#     return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# # Adapt for animation with helper lines for each Bezier point
# fig, ax = plt.subplots()
# ctrl_points = [(0.0, 0.0), (1.0, 2.0), (2.0, 0.0)]
# iterations = 5

# bezier_data = create_bezier(ctrl_points[0], ctrl_points[1], ctrl_points[2], iterations)

# ax.set_xlim(-0.5, 2.5)
# ax.set_ylim(-0.5, 2.5)
# control_points_line, = ax.plot([p[0] for p in ctrl_points], [p[1] for p in ctrl_points], 'ro-', label='Control Points')
# bezier_curve, = ax.plot([], [], 'b-', lw=2, label='Bezier Curve')
# q0_line, = ax.plot([], [], 'g--', lw=1, label='Q0 Line')
# q1_line, = ax.plot([], [], 'g--', lw=1, label='Q1 Line')
# ax.legend()

# def init():
#     bezier_curve.set_data([], [])
#     q0_line.set_data([], [])
#     q1_line.set_data([], [])
#     return bezier_curve, q0_line, q1_line

# def animate(i):
#     bezier_point, Q0, Q1 = bezier_data[i]
#     if i == 0:
#         x_vals, y_vals = [bezier_point[0]], [bezier_point[1]]
#     else:
#         x_vals, y_vals = zip(*[(bp[0], bp[1]) for bp, _, _ in bezier_data[:i+1]])
    
#     bezier_curve.set_data(x_vals, y_vals)
#     q0_line.set_data([Q0[0], bezier_point[0]], [Q0[1], bezier_point[1]])
#     q1_line.set_data([Q1[0], bezier_point[0]], [Q1[1], bezier_point[1]])
    
#     return bezier_curve, q0_line, q1_line

# ani = animation.FuncAnimation(fig, animate, frames=len(bezier_data), init_func=init, blit=True, interval=100)

# plt.show()
