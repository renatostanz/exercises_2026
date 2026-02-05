import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
    v1_mag = sum(val**2 for val in v1) ** (1/2)
    v2_mag = sum(val**2 for val in v2) ** (1/2)
    return np.dot(v1, v2) / (v1_mag * v2_mag)
