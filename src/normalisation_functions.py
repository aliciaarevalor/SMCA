import numpy as np

def normalise_slope_cost(slope_array, threshold=20.0):
    slope_clipped = np.clip(slope_array, 0, threshold)
    norm = 10 * (threshold - slope_clipped) / threshold
    return np.clip(norm, 0, 10)

def normalise_proximity(dist_array, threshold=2000.0):
    clipped = np.clip(dist_array, 0, threshold)
    norm = 10 * (1 - (clipped / threshold))
    return np.clip(norm, 0, 10)

def normalise_proximity2(dist_array, threshold=10000.0):
    clipped = np.clip(dist_array, 0, threshold)
    norm = 10 * (1 - (clipped / threshold))
    return np.clip(norm, 0, 10)

def normalise_aqueduct_sewer(array, min_val=30, max_val=80):
    clipped = np.clip(array, min_val, max_val)
    norm = 10 * (clipped - min_val) / (max_val - min_val)
    return np.clip(norm, 0, 10)

def normalise_climate(array, min_val=0, max_val=10):
    clipped = np.clip(array, min_val, max_val)
    norm = 10 * (clipped - min_val) / (max_val - min_val)
    return np.clip(norm, 0, 10)
    