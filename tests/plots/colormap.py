#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib import cm

filename = sys.argv[1] if sys.argv[1] else 'infnoise.bin'
nx = 1000
ny = 1000

data = np.fromfile(open(filename,'rb'), dtype=np.uint8, count=nx**2)
data.resize(nx,ny)

plt.xlim(0, nx)
plt.ylim(0, ny)

plt.xlabel('samples')
plt.ylabel('samples')
plt.title(f'TRNG {filename}')

#cax = plt.imshow(data, interpolation='nearest', cmap=cm.coolwarm)
cax = plt.imshow(data, interpolation='nearest', cmap=cm.afmhot)
cbar = plt.colorbar(cax, ticks=[255, 127, 0])
cbar.ax.set_yticklabels(['255', '127', '0'])

plt.savefig(f'{filename}-colormap.png')
plt.show()
