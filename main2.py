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
fig.subplots_adjust(hspace=0.3, wspace=0.315)

# (-1, 1)
ax1 = plt.subplot(3, 4, 1)
init1 = Chaotic(chaotic_map='Chebyshev', init_val=np.random.uniform(low=-1, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='Chebyshev', init_val=np.random.uniform(low=-1, high=1), iteration=iteration)
init2.main()
plt.title('Chebyshev')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax1.get_xticklabels(), visible=True)
# plt.xlabel('X1')
plt.xlim(-1, 1)
plt.setp(ax1.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(-1, 1)
plt.grid()

# (0, 1)
ax2 = plt.subplot(3, 4, 2)
init1 = Chaotic(chaotic_map='Circle', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='Circle', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init2.main()
plt.title('Circle')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax2.get_xticklabels(), visible=True)
# plt.xlabel('X1')
plt.xlim(0, 1)
plt.setp(ax2.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax3 = plt.subplot(3, 4, 3)
init1 = Chaotic(chaotic_map='Gauss/mouse', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='Gauss/mouse', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init2.main()
plt.title('Gauss/mouse')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax3.get_xticklabels(), visible=True)
# plt.xlabel('X1')
plt.xlim(0, 1)
plt.setp(ax3.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(0, 1)
plt.grid()

# (-1, 1)
ax4 = plt.subplot(3, 4, 4)
init1 = Chaotic(chaotic_map='Iterative', init_val=np.random.uniform(low=-1, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='Iterative', init_val=np.random.uniform(low=-1, high=1), iteration=iteration)
init2.main()
plt.title('Iterative')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax4.get_xticklabels(), visible=True)
# plt.xlabel('X1')
plt.xlim(-1, 1)
plt.setp(ax4.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(-1, 1)
plt.grid()

# (0, 1)
ax5 = plt.subplot(3, 4, 5)
init1 = Chaotic(chaotic_map='Logistic', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='Logistic', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init2.main()
plt.title('Logistic')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax5.get_xticklabels(), visible=True)
# plt.xlabel('X1')
plt.xlim(0, 1)
plt.setp(ax5.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax6 = plt.subplot(3, 4, 6)
init1 = Chaotic(chaotic_map='Piecewise', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='Piecewise', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init2.main()
plt.title('Piecewise')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax6.get_xticklabels(), visible=True)
# plt.xlabel('X1')
plt.xlim(0, 1)
plt.setp(ax6.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax7 = plt.subplot(3, 4, 7)
init1 = Chaotic(chaotic_map='Sine', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='Sine', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init2.main()
plt.title('Sine')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax7.get_xticklabels(), visible=True)
# plt.xlabel('X1')
plt.xlim(0, 1)
plt.setp(ax7.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax8 = plt.subplot(3, 4, 8)
init1 = Chaotic(chaotic_map='Singer', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='Singer', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init2.main()
plt.title('Singer')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax8.get_xticklabels(), visible=True)
# plt.xlabel('X1')
plt.xlim(0, 1)
plt.setp(ax8.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax9 = plt.subplot(3, 4, 9)
init1 = Chaotic(chaotic_map='Sinusoidal', init_val=np.random.uniform(low=0.5, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='Sinusoidal', init_val=np.random.uniform(low=0.5, high=1), iteration=iteration)
init2.main()
plt.title('Sinusoidal')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax9.get_xticklabels(), visible=True)
plt.xlabel('X1')
plt.xlim(0, 1)
plt.setp(ax9.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(0, 1)
plt.grid()

# (0, 1)
ax10 = plt.subplot(3, 4, 10)
init1 = Chaotic(chaotic_map='Tent', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='Tent', init_val=np.random.uniform(low=0, high=1), iteration=iteration)
init2.main()
plt.title('Tent')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax10.get_xticklabels(), visible=True)
plt.xlabel('X1')
plt.xlim(0, 1)
plt.setp(ax10.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(0, 1)
plt.grid()

# (-1, 1)
ax11 = plt.subplot(3, 4, 11)
init1 = Chaotic(chaotic_map='composite mapping', init_val=np.random.uniform(low=-1, high=1), iteration=iteration)
init1.main()
init2 = Chaotic(chaotic_map='composite mapping', init_val=np.random.uniform(low=-1, high=1), iteration=iteration)
init2.main()
plt.title('Composite')
plt.scatter(init1.X, init2.X, color='blue', s=25, facecolors='none')
plt.setp(ax11.get_xticklabels(), visible=True)
plt.xlabel('X1')
plt.xlim(-1, 1)
plt.setp(ax11.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(-1, 1)
plt.grid()

# (0, 1)
ax12 = plt.subplot(3, 4, 12)
plt.title('Uniform distribution')
plt.scatter(np.random.uniform(low=0, high=1, size=iteration), np.random.uniform(low=0, high=1, size=iteration), color='blue', s=25, facecolors='none')
plt.setp(ax12.get_xticklabels(), visible=True)
plt.xlabel('X1')
plt.xlim(0, 1)
plt.setp(ax12.get_yticklabels(), visible=True)
plt.ylabel('X2')
plt.ylim(0, 1)

# fig , ax = plt.subplots()
# fig.subplots_adjust(hspace=0.4, wspace=0.4) #設定子圖的間隔
# for i in range(1,6):
#     plt.subplot(2, 3, i)
#     plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')