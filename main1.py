import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define control points
P0 = 0 + 0j
P1 = 1 + 1j
P2 = 2 + 0j

# Set up the figure, the axis, and the plot elements we want to animate
fig, ax = plt.subplots(figsize=(8, 6))

# Drawing the static parts: control points and lines
control_points_line, = ax.plot([P0.real, P1.real, P2.real], [P0.imag, P1.imag, P2.imag], 'ro-', label='Control Points')
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 1.5)
ax.set_title('Quadratic Bezier Curve with Dynamic Q Lines')
ax.legend()

# Creating lines for the animated parts: Bezier curve (blue line) and the Q lines (green lines), including the R line (purple line for clarity)
bezier_line, = ax.plot([], [], 'b-', label='Bezier Curve')
q0_line, = ax.plot([], [], 'go-', label='Q0 Line')
q1_line, = ax.plot([], [], 'go-', label='Q1 Line')
r_line, = ax.plot([], [], 'mo-', label='R Line')  # This is the new line connecting Q0 and Q1
r0_point, = ax.plot([], [], 'ko', label='Current Point')

# Initialization function: plot the background of each frame
def init():
    bezier_line.set_data([], [])
    q0_line.set_data([], [])
    q1_line.set_data([], [])
    r_line.set_data([], [])  # Initialize the R line as well
    r0_point.set_data([], [])
    return bezier_line, q0_line, q1_line, r_line, r0_point  # Include r_line in the return tuple

# Number of frames for the animation
num_frames = 100

# Animation function. This is called sequentially
def animate(i):
    t = i / (num_frames - 1)

    # Calculate the points on the curve for each frame
    Q0 = (1 - t) * P0 + t * P1
    Q1 = (1 - t) * P1 + t * P2
    R0 = (1 - t) * Q0 + t * Q1
    
    # Update the Bezier curve
    if i == 0:
        bezier_line.set_data([P0.real], [P0.imag])
    else:
        bezier_xs, bezier_ys = bezier_line.get_data()
        bezier_xs = np.append(bezier_xs, R0.real)
        bezier_ys = np.append(bezier_ys, R0.imag)
        bezier_line.set_data(bezier_xs, bezier_ys)
    
    # Update the Q0 and Q1 lines (green lines)
    q0_line.set_data([P0.real, Q0.real], [P0.imag, Q0.imag])
    q1_line.set_data([P1.real, Q1.real], [P1.imag, Q1.imag])
    
    # Update the R line (purple line) to show interpolation between Q0 and Q1
    r_line.set_data([Q0.real, Q1.real], [Q0.imag, Q1.imag])
    
    # Update the current R0 point (black point on the curve)
    r0_point.set_data([R0.real], [R0.imag])
    
    return bezier_line, q0_line, q1_line, r_line, r0_point

# Call the animator. blit=True means only re-draw the parts that have changed.
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=30, blit=True)

plt.show()
