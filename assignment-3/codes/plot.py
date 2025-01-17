import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
quadratic_lib = ctypes.CDLL('./libquadratic.so')

# Define the C function signature
quadratic_lib.generate_quadratic_points.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.c_int, ctypes.POINTER(ctypes.c_int)
]
quadratic_lib.generate_quadratic_points.restype = None

# Parameters
start = -25.0
end = 25.0
step = 0.5
max_points = 200
n_points = ctypes.c_int()

# Allocate arrays
x_vals = np.zeros(max_points, dtype=np.double)
y_vals = np.zeros(max_points, dtype=np.double)

# Generate points for the equation b^2 - 400 = 0
quadratic_lib.generate_quadratic_points(
    start, end, step,
    x_vals.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    y_vals.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    max_points,
    ctypes.byref(n_points)
)

# Plot the graph
plt.plot(x_vals[:n_points.value], y_vals[:n_points.value], label='$b^2 - 400 = 0$', color='blue')

# Mark the points where the curve touches the x-axis
roots = [20, -20]
plt.scatter(roots, [0, 0], color='red', label='Roots ($b = \pm 20$)')

# Add annotations
for root in roots:
    plt.annotate(f'({root}, 0)', (root, 0), textcoords="offset points", xytext=(0, 10), ha='center')

# Additional plot formatting
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('b')
plt.ylabel('$b^2 - 400$')
plt.title('Graph of $b^2 - 400 = 0$')
plt.grid()
plt.legend()
plt.show()
