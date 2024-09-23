import numpy as np
from sympy import symbols, diff

# vector parameters: should be three dimensions, parametrized
# vector calculations possible:
# curvature k
# unit tangent T and unit normal N
# osculating curve calculation
# projection calculations
# cross product, dot product

vector_list = input() #list of lists
dimensions = input("enter dimensions")

def dot_product(vector_list, dim=3):
    product = 0
    # component matching
    # element wise multiplication
    # element wise aggregation
    dim_comp = [1] * dim # default identity
    for vector in vector_list:
        for index,elem in enumerate(vector):
            dim_comp[index] = dim_comp[index] * elem
    product = sum(dim_comp)

    return product

def cross_product(vector1, vector2, dim=3):
    if dim != [3,7]:
        print("Dimensions do not match, not 3 or 7.")
        return None


def curvature():
    return None

def projection(vector, base_vector):
    return None