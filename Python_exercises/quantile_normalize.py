import numpy as np

def quantile_normalize(matrix):
    """
    Performs quantile normalization on a numeric matrix.

    Steps:
        1. Sort each column.
        2. Compute mean of ranks across columns.
        3. Assign mean values back respecting original rank order.

    Parameters:
        matrix (numpy.ndarray): Input matrix of shape (n_samples, n_features).

    Returns:
        numpy.ndarray: Quantile-normalized matrix.
    """
    sorted_2d_array = np.sort(matrix, axis=0)
    mean_of_2d_array = np.mean(sorted_2d_array, axis=1)
    sorted_idx = np.argsort(matrix, axis=0)
    final_matrix = np.zeros_like(matrix, dtype=float)

    for num1 in range(matrix.shape[1]):
        val1 = sorted_2d_array[:, num1]
        idx1 = sorted_idx[:, num1]
        for num2 in range(matrix.shape[0]):
            val2 = val1[num2]
            idx2 = idx1[num2]
            final_matrix[idx2, num1] = mean_of_2d_array[num2]

    return final_matrix
