import numpy as np

# Target-to-source Mapping
def linear_transformation(src, A): # src: matrix representing image ; A: transformation matrix
  M, N, O = src.shape

  new_image = np.zeros((M, N, O), dtype=np.uint8)

  # For each pixel on the target image, with coordinates x_new, y_new
  for new_y, row in enumerate(new_image):
    for new_x, _ in enumerate(row):
      # Dot product using homogenous coordinates, with h = 1
      x, y, _ = np.dot(np.linalg.inv(A), [new_x, new_y, 1])
      if (x >= 0 and x < N and y >= 0 and y < M):
        new_image[new_y][new_x] = src[int(y)][int(x)]

  return new_image

# Source-to-target Mapping
def linear_transformation2(src, A):
  M, N, O = src.shape

  new_image = np.zeros((M, N, O), dtype=np.uint8)

  # For each pixel on the image, with coordinates x, y
  for y, row in enumerate(src):
    for x, pixel in enumerate(row):
      # Dot product using homogenous coordinates, with h = 1
      new_x, new_y, _ = np.dot(A, [x, y, 1])
      new_x = int(new_x)
      new_y = int(new_y)
      if (new_x >= 0 and new_x < N and new_y >= 0 and new_y < M):
        # Pixel at position new_x, new_y will be at nearest neighbor
        new_image[new_y][new_x] = pixel

  return new_image

# Translate
def translate(src, dx = 0, dy = 0):
  translate_matrix = np.array([[1, 0, dx],
                               [0, 1, dy],
                               [0, 0, 1]])

  return linear_transformation(src, translate_matrix)

# Scale
def scale(src, sx = 1, sy = 1):
  scale_matrix = np.array([[sx, 0, 0],
                           [0, sy, 0],
                           [0, 0, 1]])

  return linear_transformation(src, scale_matrix)

# Shear
def shear(src, bx = 0, by = 0):
  shear_matrix = np.array([[1, bx, 0],
                           [by, 1, 0],
                           [0, 0, 1]])
                           
  return linear_transformation(src, shear_matrix)

# Rotate
def rotate(src, alpha = 0, xc = 0, yc = 0):
  a = np.array([[1, 0, xc],
                [0, 1, yc],
                [0, 0, 1]])
  b = np.array([[np.cos(alpha), -np.sin(alpha), 0],
                [np.sin(alpha), np.cos(alpha), 0],
                [0, 0, 1]])
  c = np.array([[1, 0, -xc],
                [0, 1, -yc],
                [0, 0, 1]])
  
  rotate_matrix = np.dot(np.dot(a, b), c)
                           
  return linear_transformation(src, rotate_matrix)