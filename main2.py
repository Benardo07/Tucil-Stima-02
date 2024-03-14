import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define control points
P0 = 0 + 0j
P1 = 1 + 1j
P2 = 2 + 0j

# Function to calculate Bezier points
def calculate_bezier_points(P0, P1, P2, num_steps):
    points = []
    for i in range(num_steps):
        t = i / (num_steps - 1)
        Q0 = (1 - t) * P0 + t * P1
        Q1 = (1 - t) * P1 + t * P2
        R0 = (1 - t) * Q0 + t * Q1
        points.append(R0)
    return points

# Calculate Bezier curve points
num_frames = 100
bezier_points = calculate_bezier_points(P0, P1, P2, num_frames)

# Set up the figure, the axis, and the plot elements we want to animate
fig, ax = plt.subplots(figsize=(8, 6))

# Drawing the static parts: control points and lines
control_points_line, = ax.plot([P0.real, P1.real, P2.real], [P0.imag, P1.imag, P2.imag], 'ro-', label='Control Points')
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 1.5)
ax.set_title('Quadratic Bezier Curve with Dynamic Q Lines')
ax.legend()

# Creating lines for the animated parts
bezier_line, = ax.plot([], [], 'b-', label='Bezier Curve')
q0_line, = ax.plot([], [], 'go-', label='Q0 Line')
q1_line, = ax.plot([], [], 'go-', label='Q1 Line')
r_line, = ax.plot([], [], 'bo:', label='R Line')
r0_point, = ax.plot([], [], 'ko', label='Current Point')

# Initialization function
def init():
    bezier_line.set_data([], [])
    q0_line.set_data([], [])
    q1_line.set_data([], [])
    r_line.set_data([], [])
    r0_point.set_data([], [])
    return bezier_line, q0_line, q1_line, r_line, r0_point

# Animation function
def animate(i):
    R0 = bezier_points[i]
    t = i / (num_frames - 1)
    Q0 = (1 - t) * P0 + t * P1
    Q1 = (1 - t) * P1 + t * P2
    
    bezier_xs, bezier_ys = [point.real for point in bezier_points[:i+1]], [point.imag for point in bezier_points[:i+1]]
    bezier_line.set_data(bezier_xs, bezier_ys)
    
    q0_line.set_data([P0.real, Q0.real], [P0.imag, Q0.imag])
    q1_line.set_data([P1.real, Q1.real], [P1.imag, Q1.imag])
    
    r_line.set_data([Q0.real, Q1.real], [Q0.imag, Q1.imag])
    
    r0_point.set_data([R0.real], [R0.imag])
    
    return bezier_line, q0_line, q1_line, r_line, r0_point

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=30, blit=True)

plt.show()
