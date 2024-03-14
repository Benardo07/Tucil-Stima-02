import numpy as np
import matplotlib.pyplot as plt

def bezier_curve_iterative(P0, P1, P2, iterations):
    points = [P0, P1, P2]
    
    for _ in range(iterations):
        new_points = []
        # Step a: Create new points Q0 and Q1
        Q0 = (P0 + P1) / 2
        Q1 = (P1 + P2) / 2
        
        # Step b & c: Create new point R0
        R0 = (Q0 + Q1) / 2
        
        # Steps for next level of iteration
        S0 = (P0 + Q0) / 2
        S1 = (Q0 + R0) / 2
        S2 = (R0 + Q1) / 2
        S3 = (Q1 + P2) / 2
        
        T0 = (S0 + S1) / 2
        T1 = (S2 + S3) / 2
        
        # Update points for next iteration
        new_points.extend([P0, S0, T0, R0, T1, S3, P2])
        
        points = new_points
    
    return points

# Define initial control points
P0 = np.array([0, 0])
P1 = np.array([1, 2])
P2 = np.array([2, 0])

# Number of iterations
iterations = 2

# Calculate points
bezier_points = bezier_curve_iterative(P0, P1, P2, iterations)
print(bezier_points)
# Extracting x and y coordinates
x_points = [p[0] for p in bezier_points]
y_points = [p[1] for p in bezier_points]

# Plotting the curve
plt.figure(figsize=(8, 6))
plt.plot(x_points, y_points, 'b-', label='Approximated Bezier Curve')
plt.plot([P0[0], P1[0], P2[0]], [P0[1], P1[1], P2[1]], 'ro-', label='Control Points')
plt.legend()
plt.title('Iterative Bezier Curve Approximation')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
