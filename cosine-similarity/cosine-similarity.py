import numpy as np
import math

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    A=np.asarray(a,dtype='float')
    B=np.asarray(b,dtype='float')

    magA=math.sqrt(sum(i**2 for i in a))
    magB=math.sqrt(sum(i**2 for i in b)) 

    if not magA or not magB:
        return 0.0
                   
    res=np.dot(A,B)/(magA*magB)

    return float(res)
    pass