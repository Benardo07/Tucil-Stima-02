from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_bezier(control_points: List[Tuple[float, float]], iterations: int) -> Tuple[List[Tuple[float, float]], List[List[Tuple[float, float]]]]:
    if len(control_points) < 2:
        raise ValueError("At least two control points are required")
    bezier_points = [control_points[0]]  
    iteration_points = [[control_points[0]] for _ in range(iterations)]  
    find_bezier_points(bezier_points, control_points, 0, iterations, iteration_points)
    bezier_points.append(control_points[-1])
    for i in range(iterations):  
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



def create_bezier_3_points(p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float], iterations: int) -> List[Tuple[float, float]]:
    bezier_points = []
    bezier_points.append(p1)  
    find_bezier_points_3_points(bezier_points, p1, p2, p3, 0, iterations)
    bezier_points.append(p3) 
    return bezier_points

def find_bezier_points_3_points(bezier_points: List[Tuple[float, float]], p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float], current_iteration: int, iterations: int):
    if current_iteration < iterations:
        mid_point1 = mid_point(p1, p2)
        mid_point2 = mid_point(p2, p3)
        mid_point3 = mid_point(mid_point1, mid_point2)  
        current_iteration += 1
        find_bezier_points(bezier_points, p1, mid_point1, mid_point3, current_iteration, iterations)  # Left branch
        bezier_points.append(mid_point3) 
        find_bezier_points(bezier_points, mid_point3, mid_point2, p3, current_iteration, iterations)  # Right branch
