#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1] if sys.argv[1] else 'infnoise.bin'
bp = np.dtype([('byte1',np.uint8),('byte2',np.uint8)]) # 'struct' byte pairs

Z = np.fromfile(filename, dtype=bp, count=2000) # read 2000 byte pairs from binary file

x, y = zip(*Z) # unpack Z pairs into lists

plt.grid(True)

plt.xlim(0, 255)
plt.ylim(0, 255)

plt.xlabel('bytes')
plt.ylabel('bytes')
plt.title(f'TRNG {filename}')

plt.scatter(x[:1000],y[:1000])

plt.savefig(f'{filename}-scatter.png')
plt.show()


