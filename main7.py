from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_bezier(control_points: List[Tuple[float, float]], iterations: int) -> Tuple[List[Tuple[float, float]], List[List[Tuple[float, float]]]]:
    if len(control_points) < 2:
        raise ValueError("At least two control points are required")
    bezier_points = [control_points[0]]  # Add the first control point
    iteration_points = [[control_points[0]] for _ in range(iterations)]   # Store points for each iteration
    find_bezier_points(bezier_points, control_points, 0, iterations, iteration_points)
    bezier_points.append(control_points[-1])
    for i in range(iterations):  # Ensure the last control point is added
        iteration_points[i].append(control_points[-1])
    return bezier_points, iteration_points

def find_bezier_points(bezier_points: List[Tuple[float, float]], control_points: List[Tuple[float, float]], current_iteration: int, iterations: int, iteration_points: List[List[Tuple[float, float]]]):
    if current_iteration < iterations:
        next_level_points = [control_points]
        new_control_points = control_points
        for _ in range(len(control_points) - 1):
            temp = []
            for i in range(len(new_control_points) - 1):
                temp.append(mid_point(new_control_points[i], new_control_points[i + 1]))
            next_level_points.append(temp)
            new_control_points = temp

        left_half = [point[0] for point in next_level_points]
        right_half = [point[-1] for point in reversed(next_level_points)]

        find_bezier_points(bezier_points, left_half, current_iteration + 1, iterations, iteration_points)
        for i in range(iterations):
            if(i >= current_iteration):
                iteration_points[i].append(next_level_points[-1][0])
        bezier_points.append(next_level_points[-1][0])      
        find_bezier_points(bezier_points, right_half, current_iteration + 1, iterations, iteration_points)

def mid_point(p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def main():
    ctrl_points = [(0, 0), (1, 1), (2, 1), (3, 0)]
    iterations = 5

    bezier_points, iteration_points = create_bezier(ctrl_points, iterations)

    print(bezier_points)
    all_points = ctrl_points + bezier_points
    all_x = [p[0] for p in all_points]
    all_y = [p[1] for p in all_points]

    x_buffer, y_buffer = 0.1, 0.1

    fig, ax = plt.subplots()
    ax.set_xlim(min(all_x) - x_buffer, max(all_x) + x_buffer)
    ax.set_ylim(min(all_y) - y_buffer, max(all_y) + y_buffer)

    control_points_line, = ax.plot([p[0] for p in ctrl_points], [p[1] for p in ctrl_points], 'ro-', label='Control Points')
    bezier_line, = ax.plot([], [], 'b-', label='Bezier Curve')
    ax.legend()

    def init():
        bezier_line.set_data([], [])
        return bezier_line,

    def animate(i):
        if i < len(iteration_points):
            x_vals, y_vals = zip(*iteration_points[i])
            bezier_line.set_data(x_vals, y_vals)
        return bezier_line,

    ani = animation.FuncAnimation(fig, animate, frames=len(iteration_points), init_func=init, blit=True, repeat=True, interval=250)

    plt.show()

if __name__ == '__main__':
    main()
