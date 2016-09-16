# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:29:01 2016

@author: mpnun
"""

from const import const
import numpy as np
from Reaction import Reaction
import matplotlib.pyplot as plt
import matplotlib as mat

class ReactionNetwork:
    
    def __init__(self): 
        
        self.species = []
        self.reactions = []
        self.stoich_mat = np.array([])              # stoichiometric matrix
      
    def PlotEnrgDiagram(self,rxn_list):
        
        E = 0
        state_ind = [0,1]
        state_eng = [E,E]
        
        state = 2
        
        for i in rxn_list:
            
            state_ind.append(state)
            state += 1
            state_ind.append(state)
            state += 1
            
            E += self.reactions[i-1].delE
            state_eng.append(E)
            state_eng.append(E)
        
        # Plotting
        mat.rcParams['mathtext.default'] = 'regular'
        mat.rcParams['text.latex.unicode'] = 'False'
        mat.rcParams['legend.numpoints'] = 1
        mat.rcParams['lines.linewidth'] = 2
        mat.rcParams['lines.markersize'] = 16
        
        plt.figure()
        
        plt.plot(state_ind, state_eng, 'o-', markersize = 15)   
        
        plt.xticks(size=24)
        plt.yticks(size=24)
        plt.xlabel('reaction coordinate',size=30)
        plt.ylabel('energy (eV)',size=30)
#        plt.legend(rxn_labels,loc=1,prop={'size':20},frameon=False)
        plt.show()
        
        ax = plt.subplot(111)
        pos = [0.2, 0.15, 0.7, 0.8]
        ax.set_position(pos)        
        
    def AddRxn(self,rcnt_list,prod_list):
        rxn = Reaction()
        for rcnt in rcnt_list:
            rxn.reactants.append(self.species[rcnt-1])
        for prod in prod_list:
            rxn.products.append(self.species[prod-1])       
        rxn.calc_delE()
        self.reactions.append(rxn)