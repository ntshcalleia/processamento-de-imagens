import numpy as np
import imageio
from transforms import twirl

duna = imageio.imread('imgs/duna.jpg')
face = imageio.imread('imgs/face.jpg')
livre = imageio.imread('imgs/livre.jpg')
ruido = imageio.imread('imgs/ruido.jpg')

#imageio.imwrite('results/twirl/duna.jpg', twirl(duna, alpha=2*np.pi))
#imageio.imwrite('results/twirl/face2.jpg', twirl(face, alpha=np.pi))
#imageio.imwrite('results/twirl/livre.jpg', twirl(livre, alpha=2*np.pi))
#imageio.imwrite('results/twirl/ruido.jpg', twirl(ruido, alpha=2*np.pi))