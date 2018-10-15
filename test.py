import numpy as np
import imageio
from transforms import twirl
from edge_detection import sobel, robert

duna = imageio.imread('imgs/duna.jpg')
face = imageio.imread('imgs/face.jpg')
livre = imageio.imread('imgs/livre.jpg')
ruido = imageio.imread('imgs/ruido.jpg')

# TWIRL
#imageio.imwrite('imgs/results/twirl/duna.jpg', twirl(duna, alpha=2*np.pi))
#imageio.imwrite('imgs/results/twirl/face2.jpg', twirl(face, alpha=np.pi))
#imageio.imwrite('imgs/results/twirl/livre.jpg', twirl(livre, alpha=2*np.pi))
#imageio.imwrite('imgs/results/twirl/ruido.jpg', twirl(ruido, alpha=2*np.pi))

# SOBEL
#imageio.imwrite('imgs/results/sobel/duna.jpg', sobel(duna))
#imageio.imwrite('imgs/results/sobel/face.jpg', sobel(face))
#imageio.imwrite('imgs/results/sobel/livre.jpg', sobel(livre, 20))
#imageio.imwrite('imgs/results/sobel/ruido.jpg', sobel(ruido))

# ROBERT
imageio.imwrite('imgs/results/robert/duna.jpg', robert(duna))
imageio.imwrite('imgs/results/robert/face.jpg', robert(face))
imageio.imwrite('imgs/results/robert/livre.jpg', robert(livre))
imageio.imwrite('imgs/results/robert/ruido.jpg', robert(ruido))