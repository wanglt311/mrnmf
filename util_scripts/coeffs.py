"""
   Copyright (c) 2014, Austin R. Benson, David F. Gleich, 
   Purdue University, and Stanford University.
   All rights reserved.
 
   This file is part of MRNMF and is under the BSD 2-Clause License, 
   which can be found in the LICENSE file in the root directory, or at 
   http://opensource.org/licenses/BSD-2-Clause
"""

import numpy as np
import math

r = 40
n = 320
Hprime = np.zeros((r, n-r))
for i in xrange(r):
	for j in xrange(n-r):
		if i - j == 0:
			Hprime[i, j] = 0.
		else:
			Hprime[i, j] = 1. / abs(i - j)
	
with open('Hprime_40_320.txt', 'w') as f:
	for row in Hprime:
		row = [str(v) for v in row]
		f.write(' '.join(row) + '\n')

r = 20
n = 200
Hprime = np.zeros((r, n-r))
for i in xrange(r):
	for j in xrange(n-r):
		if i - j == 0:
			Hprime[i, j] = 0.
		else:
			Hprime[i, j] = math.sqrt(i ** 2 + j ** 2)
for i in xrange(n-r):
	Hprime[:, i] = (Hprime[:, i] / np.linalg.norm(Hprime[:, i], 1))

Hprime = np.random.random((r, n-r))
with open('Hprime_20_200.txt', 'w') as f:
	for row in Hprime:
		row = [str(v) for v in row]
		f.write(' '.join(row) + '\n')
