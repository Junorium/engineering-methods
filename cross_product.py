# vector input as a list of lists
# vectors = [[vector1], [vector2]]

def cross_product_xy(vectors):
  vector_1 = vectors[0]
  vector_2 = vectors[1]

  return [vector_1[0] * vector_2[1], vector_1[1] * vector_2[0]]

def cross_product_xyz(vectors):
  vector_1 = vectors[0]
  vector_2 = vectors[1]

  return [(vector_1[1]*vector_2[2]) - (vector_1[2]*vector_1[1]),
          (vector_1[0]*vector_2[2]) - (vector_1[2]*vector_2[0]), 
          (vector_1[0]*vector_2[1]) - (vector_1[1]*vector_2[0])]
