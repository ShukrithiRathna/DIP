from scipy import ndimage
import numpy as np
a = np.arange(12.).reshape((4, 3))
a




ndimage.map_coordinates(a, [[0.5, 2], [0.5, 1]], order=1)