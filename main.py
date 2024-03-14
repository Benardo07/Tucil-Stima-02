import matplotlib.pyplot as plt

def bezier_curve(P0, P1, P2, t):
    Q0 = (1 - t) * P0 + t * P1
    Q1 = (1 - t) * P1 + t * P2
    R0 = (1 - t) * Q0 + t * Q1
    return R0

def divide_and_conquer(P0, P1, P2, threshold=0.01):
    points = [P0]
    def divide(p0, p1, p2, depth=0):
        q0 = (p0 + p1) / 2
        q1 = (p1 + p2) / 2
        r0 = (q0 + q1) / 2
        if depth < threshold:
            points.append(r0)
        else:
            divide(p0, q0, r0, depth / 2)
            divide(r0, q1, p2, depth / 2)
    divide(P0, P1, P2, 1)
    points.append(P2)
    return points

# Define control points
P0 = 2 + 0j
P1 = 6 + 6j
P2 = 3 + 3j


# Generate curve points
curve_points = divide_and_conquer(P0, P1, P2, threshold=0.01)

print(curve_points)
# Plotting
plt.figure(figsize=(8, 6))
plt.plot([P0.real, P1.real, P2.real], [P0.imag, P1.imag, P2.imag], 'ro-')  # Control points and lines
plt.plot([p.real for p in curve_points], [p.imag for p in curve_points], 'b-')  # Bezier curve
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Quadratic Bezier Curve')
plt.grid(True)
plt.show()