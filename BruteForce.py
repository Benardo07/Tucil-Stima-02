from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_bezier_brute_force(control_points: List[Tuple[float, float]], iterations: int) -> List[Tuple[float, float]]:
    bezier_points = []
    n = len(control_points) - 1
    for t in range(0,2**iterations+1):
        t_normalized = t / 2**iterations
        x, y = 0, 0
        for i in range(n + 1):
            binomial_coefficient = binomial(n, i)
            x += binomial_coefficient * ((1 - t_normalized) ** (n - i)) * (t_normalized ** i) * control_points[i][0]
            y += binomial_coefficient * ((1 - t_normalized) ** (n - i)) * (t_normalized ** i) * control_points[i][1]
        bezier_points.append((x, y))
    print(bezier_points)
    return bezier_points

def binomial(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)

# ctrl_points = [(0, 100), (100, 200), (150, 50), (300, 100), (200, 150), (150, 150)]
# iterations = 5

# bezier_points = create_bezier_brute_force(ctrl_points, iterations)
# fig, ax = plt.subplots()
# control_points_line, = ax.plot([p[0] for p in ctrl_points], [p[1] for p in ctrl_points], 'ro-', label='Control Points')
# bezier_line, = ax.plot([], [], 'b-', label='Bezier Curve')
# ax.legend()

# def animate(i):
#     x_vals, y_vals = zip(*bezier_points[:i + 1])
#     bezier_line.set_data(x_vals, y_vals)
#     return [bezier_line]

# ani = animation.FuncAnimation(fig, animate, frames=len(bezier_points), blit=True, interval=50)

# plt.show()
