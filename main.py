# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:47:20 2020

@author: ZongSing_NB
"""

from Chaotic import Chaotic
import numpy as np
import matplotlib.pyplot as plt
font = {'size'   : 15}
plt.rc('font', **font)
lw = 2
iteration = 100

fig , ax = plt.subplots()
fig.subplots_adjust(hspace=0.2, wspace=0.315)

# (-1, 1)
ax1 = plt.subplot(3, 4, 1)
init = Chaotic(chaotic_map='Chebyshev', init_val=0.7, iteration=iteration)
init.main()
plt.title('Chebyshev')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax1.get_xticklabels(), visible=False)
# plt.xlabel('Iteration')
plt.setp(ax1.get_yticklabels(), visible=True)
plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(-1, 1)
plt.grid()

# (0, 1)
ax2 = plt.subplot(3, 4, 2)
init = Chaotic(chaotic_map='Circle', init_val=0.7, iteration=iteration)
init.main()
plt.title('Circle')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax2.get_xticklabels(), visible=False)
# plt.xlabel('Iteration')
plt.setp(ax2.get_yticklabels(), visible=True)
# plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax3 = plt.subplot(3, 4, 3)
init = Chaotic(chaotic_map='Gauss/mouse', init_val=0.7, iteration=iteration)
init.main()
plt.title('Gauss/mouse')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax3.get_xticklabels(), visible=False)
# plt.xlabel('Iteration')
plt.setp(ax3.get_yticklabels(), visible=True)
# plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(0, 1)
plt.grid()

# (-1, 1)
ax4 = plt.subplot(3, 4, 4)
init = Chaotic(chaotic_map='Iterative', init_val=0.7, iteration=iteration)
init.main()
plt.title('Iterative')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax4.get_xticklabels(), visible=False)
# plt.xlabel('Iteration')
plt.setp(ax4.get_yticklabels(), visible=True)
# plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(-1, 1)
plt.grid()

# (0, 1)
ax5 = plt.subplot(3, 4, 5)
init = Chaotic(chaotic_map='Logistic', init_val=0.7, iteration=iteration)
init.main()
plt.title('Logistic')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax5.get_xticklabels(), visible=False)
# plt.xlabel('Iteration')
plt.setp(ax5.get_yticklabels(), visible=True)
plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax6 = plt.subplot(3, 4, 6)
init = Chaotic(chaotic_map='Piecewise', init_val=0.7, iteration=iteration)
init.main()
plt.title('Piecewise')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax6.get_xticklabels(), visible=False)
# plt.xlabel('Iteration')
plt.setp(ax6.get_yticklabels(), visible=True)
# plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax7 = plt.subplot(3, 4, 7)
init = Chaotic(chaotic_map='Sine', init_val=0.7, iteration=iteration)
init.main()
plt.title('Sine')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax7.get_xticklabels(), visible=False)
# plt.xlabel('Iteration')
plt.setp(ax7.get_yticklabels(), visible=True)
# plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax8 = plt.subplot(3, 4, 8)
init = Chaotic(chaotic_map='Singer', init_val=0.7, iteration=iteration)
init.main()
plt.title('Singer')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax8.get_xticklabels(), visible=False)
# plt.xlabel('Iteration')
plt.setp(ax8.get_yticklabels(), visible=True)
# plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax9 = plt.subplot(3, 4, 9)
init = Chaotic(chaotic_map='Sinusoidal', init_val=0.7, iteration=iteration)
init.main()
plt.title('Sinusoidal')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax9.get_xticklabels(), visible=True)
plt.xlabel('Iteration')
plt.setp(ax8.get_yticklabels(), visible=True)
plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax10 = plt.subplot(3, 4, 10)
init = Chaotic(chaotic_map='Tent', init_val=0.6, iteration=iteration)
init.main()
plt.title('Tent')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax10.get_xticklabels(), visible=True)
plt.xlabel('Iteration')
plt.setp(ax10.get_yticklabels(), visible=True)
# plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(0, 1)
plt.grid()

# (-1, 1)
ax11 = plt.subplot(3, 4, 11)
init = Chaotic(chaotic_map='composite mapping', init_val=0.7, iteration=iteration)
init.main()
plt.title('Composite')
plt.plot(np.arange(iteration)+1, init.X, color='blue', linewidth=lw)
plt.setp(ax11.get_xticklabels(), visible=True)
plt.xlabel('Iteration')
plt.setp(ax11.get_yticklabels(), visible=True)
# plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(-1, 1)
plt.grid()
# plt.show()

# (0, 1)
ax12 = plt.subplot(3, 4, 12)
plt.title('Uniform distribution')
plt.plot(np.arange(iteration)+1, np.random.uniform(size=iteration), color='blue', linewidth=lw)
plt.setp(ax12.get_xticklabels(), visible=True)
plt.xlabel('Iteration')
plt.setp(ax12.get_yticklabels(), visible=True)
# plt.ylabel('X')
plt.xlim(1, iteration)
plt.ylim(0, 1)
plt.grid()
# plt.show()

# fig , ax = plt.subplots()
# fig.subplots_adjust(hspace=0.4, wspace=0.4) #設定子圖的間隔
# for i in range(1,6):
#     plt.subplot(2, 3, i)
#     plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')