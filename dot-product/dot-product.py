import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    X=np.asarray(x,dtype=float)
    Y=np.asarray(y,dtype=float)

    res=np.dot(X,Y)
    
    return float(res)
    pass