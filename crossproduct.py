# vector input as a list of lists
# vectors = [[vector1], [vector2]]

def cross_product_xy(vectors):
  vector_1 = vectors[0]
  vector_2 = vectors[1]

  return [vector_1[0] * vector_2[1], vector_1[1] * vector_2[0]]

  
