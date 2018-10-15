import numpy as np

def cubic(src, x, y):
  # Check if (x, y) isn't already a point on the original image
  if int(x) == x and int(y) == y:
    return src[int(y)][int(x)]

  def w_cub(x):
    if (0 <= abs(x) < 1):
      return abs(x**3) - 2*(x**2) + 1
    if (1 <= abs(x) < 2):
      return -abs(x**3) + 5*(x**2) - 8*abs(x) + 4
    return 0
  
  def w_bicub(x, y):
    return w_cub(x)*w_cub(y)
  
  M, N, O = src.shape # O = size of color vector (3, since it's RGB)

  color = np.zeros(O)
  u0, v0 = np.floor([x, y])

  x_neighbors = np.array([u0-1, u0, u0+1, u0+2], dtype=int)
  y_neighbors = np.array([v0-1, v0, v0+1, v0+2], dtype=int)

  for v in y_neighbors:
    for u in x_neighbors:
      if (v >= 0 and v < M and u >= 0 and u < N):
        original_color = src[v][u]
      else:
        original_color = np.zeros(O)
      color = np.add(color, w_bicub(x-u, y-v)*original_color)
  
  return np.minimum(np.full(O, 255), np.maximum(np.zeros(O), color)) # val = 0 if val < 0 and val = 255 if val > 255