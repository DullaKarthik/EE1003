
#include <math.h>

void generate_quadratic_points(double start, double end, double step,
                               double* x_vals, double* y_vals, int max_points, int* n_points) {
    int i = 0;
    for (double x = start; x <= end && i < max_points; x += step) {
        x_vals[i] = x;
        y_vals[i] = x * x - 400; // Corresponds to b^2 - 400
        i++;
    }
    *n_points = i;  // Total points generated
}
