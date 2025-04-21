import numpy as np

def barbilian_metric(A, B, P, Q):
    """
    Calculate the Barbilian (Apollonian) metric between two points A and B.
    
    Parameters:
    -----------
    A, B : array-like
        Points between which to calculate the distance
    P, Q : array-like
        Boundary points of the domain
    
    Returns:
    --------
    float
        The Barbilian distance between points A and B
    """
    try:
        # Convert inputs to numpy arrays
        A, B, P, Q = map(np.asarray, (A, B, P, Q))
        
        # Calculate distances
        AP = np.linalg.norm(A - P)
        BQ = np.linalg.norm(B - Q)
        AQ = np.linalg.norm(A - Q)
        BP = np.linalg.norm(B - P)
        
        # Check for zero distances
        if AP <= 0 or BQ <= 0 or AQ <= 0 or BP <= 0:
            raise ValueError("Zero distances detected")
            
        return float(np.log((AP * BQ) / (AQ * BP)))
    except Exception as e:
        raise ValueError(f"Error calculating Barbilian metric: {str(e)}")
		
# 2D points example
A = np.array([1.0, 2.0])
B = np.array([3.0, 4.0])
P = np.array([0.0, 0.0])
Q = np.array([5.0, 5.0])

distance = barbilian_metric(A, B, P, Q)
