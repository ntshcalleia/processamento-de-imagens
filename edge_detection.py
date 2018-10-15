import numpy as np

def sobel(src, threshold = 0):
  M, N, O = src.shape
  filtered_img = np.zeros((M, N, O), dtype=np.uint8)

  def cor(x, y):
    if x >= 0 and x < N and y >= 0 and y < M:
      return np.sum(src[y][x])
    else:
      return 0

  for y, row in enumerate(filtered_img):
    for x, _ in enumerate(row):
      Gx = cor(x-1, y-1) + 2*cor(x-1, y) + cor(x-1, y+1) - (cor(x+1, y-1) + 2*cor(x+1, y) + cor(x+1, y+1))
      Gy = cor(x-1, y-1) + 2*cor(x, y-1) + cor(x+1, y-1) - (cor(x-1, y+1) + 2*cor(x, y+1) + cor(x+1, y+1))

      # calculate the length of the gradient
      length = np.sqrt((Gx**2) + (Gy**2))

      # normalise the length of gradient to the range 0 to 255
      length = (length / 4328 * 255)

      if length < threshold:
        length = 0

      filtered_img[y][x] = np.full(O, length)
  
  return filtered_img

def robert(src, threshold = 0):
  M, N, O = src.shape
  filtered_img = np.zeros((M, N, O), dtype=np.uint8)

  def cor(x, y):
    if x >= 0 and x < N and y >= 0 and y < M:
      return np.sum(src[y][x])/3
    else:
      return 0
  
  for y, row in enumerate(filtered_img):
    for x, _ in enumerate(row):
      length = cor(x, y) - cor(x+1, y+1) + cor(x+1, y) - cor(x, y+1)

      if length < threshold:
        length = 0

      filtered_img[y][x] = np.full(O, length)

  return filtered_img