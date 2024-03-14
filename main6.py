def create_bezier(p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float], p4: Tuple[float, float], iterations: int) -> List[Tuple[float, float]]:
    bezier_points = []
    bezier_points.append(p1)  # Add the first control point
    find_bezier_points(bezier_points, p1, p2, p3, p4, 0, iterations)
    bezier_points.append(p4)  # Add the last control point
    return bezier_points

def find_bezier_points(bezier_points: List[Tuple[float, float]], p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float], p4: Tuple[float, float], current_iteration: int, iterations: int):
    if current_iteration < iterations:
        mid_point1 = mid_point(p1, p2)
        mid_point2 = mid_point(p2, p3)
        mid_point3 = mid_point(p3, p4)
        mid_mid_point1 = mid_point(mid_point1, mid_point2)
        mid_mid_point2 = mid_point(mid_point2, mid_point3)
        new_control_point = mid_point(mid_mid_point1, mid_mid_point2)  # The next control point
        current_iteration += 1
        find_bezier_points(bezier_points, p1, mid_point1, mid_mid_point1, new_control_point, current_iteration, iterations)  # First quarter
        bezier_points.append(new_control_point)
        find_bezier_points(bezier_points, new_control_point, mid_mid_point2, mid_point3, p4, current_iteration, iterations)  # Last quarter

def mid_point(p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)