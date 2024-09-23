# vector parameters: should be three dimensions, parametrized
# vector calculations possible:
# curvature k
# unit tangent T and unit normal N
# osculating curve calculation
# projection calculations
# cross product, dot product

vector1 = input()
vector2 = input() # should be the same dimensions
dimensions = input("enter dimensions")

def dot_product(vector1, vector2, dim=3):
    return None

def cross_product(vector1, vector2, dim=3):
    if dim != [3,7]:
        print("Dimensions do not match, not 3 or 7.")
        return None

