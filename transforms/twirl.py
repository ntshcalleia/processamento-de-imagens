import numpy as np

# Twirl
def twirl(src, xc = None, yc = None, alpha = 0, rmax = None):
  M, N, O = src.shape

  # default xc and yc: image center
  if xc == None:
    xc = N/2
  if yc == None:
    yc = M/2
  if rmax == None:
    rmax = np.min([xc - 1, yc - 1]) # Chosen arbitrarily

  new_image = np.zeros((M, N, O), dtype=np.uint8)

  # For each pixel on the target image, with coordinates x_new, y_new
  for new_y, row in enumerate(new_image):
    for new_x, _ in enumerate(row):
      dx = new_x - xc
      dy = new_y - yc
      r = np.sqrt(dx**2 + dy**2)
      if (r > rmax):
        x = new_x
        y = new_y
      else:
        beta = np.arctan2(dy, dx) + alpha*(rmax - r)/rmax
        x = xc + r*np.cos(beta)
        y = yc + r*np.sin(beta)
      # If there's a pixel on the original image, at x, y
      if (x >= 0 and x < N and y >= 0 and y < M):
        # Pixel at position new_x, new_y will be at nearest neighbor
        new_image[new_y][new_x] = src[int(y)][int(x)]

  return new_image