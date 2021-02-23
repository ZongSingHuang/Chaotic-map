# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:32:15 2020

@author: ZongSing_NB
"""
"""
ref:
https://www.mdpi.com/2076-3417/10/11/3667
https://link.springer.com/article/10.1007/s00521-014-1597-x
https://www.mathworks.com/matlabcentral/fileexchange/47215-chaos-theory-and-meta-heuristics?s_tid=mwa_osa_a
"""

import numpy as np

class Chaotic():
    def __init__(self, chaotic_map='Logistic', init_val=0.7, iteration=100):
        self.chaotic_map = chaotic_map
        self.init_val = init_val
        self.iteration = iteration
        self.X = np.zeros(iteration)
        
    def main(self):
        if self.chaotic_map=='composite mapping':
            # https://www.mdpi.com/2076-3417/10/11/3667
            init_X = self.init_val
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                init_X = 1 - 2*( np.cos( 4*np.arccos(init_X) ) )**2

        elif self.chaotic_map=='Chebyshev':
            init_X = self.init_val
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                init_X = np.cos((i+1)*np.arccos(init_X))
        
        elif self.chaotic_map=='Circle':
            a = 0.5
            b = 0.2
            init_X = self.init_val
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                init_X = np.mod(init_X+b-(a/(2*np.pi))*np.sin(2*np.pi*init_X), 1)

        elif self.chaotic_map=='Gauss/mouse':
            P = 0.4
            init_X = self.init_val
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                if init_X==0:
                    init_X = 1
                else:
                    init_X = np.mod(1/init_X, 1)

        elif self.chaotic_map=='Iterative':
            a = 0.7
            init_X = self.init_val
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                init_X = np.sin(a*np.pi/init_X)
        
        elif self.chaotic_map=='Logistic':
            a = 4
            init_X = self.init_val
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                init_X = a*init_X*(1-init_X)
        
        elif self.chaotic_map=='Piecewise':
            P = 0.4
            init_X = self.init_val
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                if 0<=init_X and init_X<P:
                    init_X = init_X/P
                elif P<=init_X and init_X<0.5:
                    init_X = (init_X-P)/(0.5-P)
                elif 0.5<=init_X and init_X<1-P:
                    init_X = (1-P-init_X)/(0.5-P)
                elif 1-P<=init_X and init_X<1:
                    init_X = (1-init_X)/P
                else:
                    print(666)

        elif self.chaotic_map=='Sine':
            a = 4
            init_X = self.init_val
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                init_X = (a/4)*np.sin(np.pi*init_X)
        
        # if X(t)>0.999, then X(t+1) will bigger than 1!!!
        elif self.chaotic_map=='Singer':
            u = 1.07
            init_X = self.init_val
            if init_X>0.999:
                print('If the init_X>=0.999 are met, the Singer will crash!!!')
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                init_X = u*(7.86*init_X-23.31*init_X**2+28.75*init_X**3-13.302875*init_X**4)

        elif self.chaotic_map=='Sinusoidal':
            a = 2.3
            init_X = self.init_val
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                init_X = a*init_X**2 * np.sin(np.pi*init_X)
        
        elif self.chaotic_map=='Tent':
            init_X = self.init_val
            self.X = np.zeros(self.iteration)
            for i in range(self.iteration):
                self.X[i] = init_X
                if init_X<0.7:
                    init_X = init_X/0.7
                elif init_X>=0.7:
                    init_X = (10/3)*(1-init_X)