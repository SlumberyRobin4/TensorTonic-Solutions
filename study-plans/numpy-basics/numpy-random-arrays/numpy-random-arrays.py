import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    # Create a Generator instance with seed for reproducibility
    np.random.seed(seed)

    if kind == 'uniform':
        # Draws from U(0,1)
        return np.random.random(shape)
    else:
        # Draws from N(0,1)
        return np.random.standard_normal(shape)