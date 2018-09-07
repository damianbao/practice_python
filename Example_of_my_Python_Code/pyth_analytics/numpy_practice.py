# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:48:12 2018

@author: rdsta
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 32, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.figure(figsize = (8,6))



plt.plot(X,C, color = 'red', linestyle = 'dashed', label = 'cos')
plt.plot(X,S, 'bo', label = 'sine')

plt.legend(loc='upper left')
plt.xlim(-4,4)
plt.ylim(-1.2,1.2)

plt.xticks(np.linspace(-np.pi, np.pi, 5, endpoint=True), \
           [r'$-\pi$',r'$-\pi/2$', r'$0$', r'$+\pi$',r'$+\pi/2$'])
plt.yticks(np.arange(-1, 1.1, 0.5))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_postion(('data',0))
ax.xaxis.set_ticks_postion('bottom')
ax.yaxis.set_ticks_postion('left')

plt.show()