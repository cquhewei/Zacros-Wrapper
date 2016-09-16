# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:28:48 2016

@author: RDX
"""

#import BuildInputFiles as BI
#import copy
#import GeneralUtilities as ut
#import numpy as np
#import os
#import ReadInputFiles as RI
#import ReadOutputFiles as RO
#import RunZacros as RunZacros

import matplotlib.pyplot as plt
import matplotlib as mat
import numpy as np
from KMCrun import KMCrun

class RateRescaling:
    
    def __init__(self):
        
        self.KMC_system = KMCrun()
        self.SDF_mat    = []        # scaledown factors for each iteration
    
    def PerformScaledown(self):
        # Print reaction names and scaledown factors into a file
        print 'Rescaling rate constants\n'
        
        max_iterations = 15
        max_events = int(1e5)
        converged = False
        iteration = 0        
        cutoff = 0.5                # If a rate constant is changing by a half-order of magnititude or more, continue
        
        self.SDF_mat = self.KMC_system.data.scaledown_factors
        
        # Set numerical parameters
        self.KMC_system.data.Conditions['MaxStep'] = max_events
        self.KMC_system.data.Report['procstat'] = ['event', max_events/10]
        
        while not converged and iteration < max_iterations:
            
            iteration += 1
            print 'Iteration number ' + str(iteration) + '\n'
            
            self.KMC_system.data.WriteAllInput()
            self.KMC_system.Run_sim()
            self.KMC_system.data.ReadAllOutput()
            delta_sdf = self.ProcessStepFreqs()         # compute change in scaledown factors based on simulation result
            # Check convergence
            if np.max(np.abs(np.log10(delta_sdf))) < cutoff:             # converged if changes to rate constants are small enough
                converged = True
                                   
            for rxn_ind in range (self.KMC_system.data.Reactions['nrxns']):            
                self.KMC_system.data.Reactions['Input'][rxn_ind]['variant'][0]['pre_expon'] = self.KMC_system.data.Reactions['Input'][rxn_ind]['variant'][0]['pre_expon'] * delta_sdf[rxn_ind]
                self.KMC_system.data.scaledown_factors[rxn_ind] = self.KMC_system.data.scaledown_factors[rxn_ind] * delta_sdf[rxn_ind]
            
            self.SDF_mat = np.vstack([self.SDF_mat,self.KMC_system.data.scaledown_factors])            

        # return time-scale information, use this to set a good sampling time for big run
                  
    def ProcessStepFreqs(self):                 # Process KMC output and determine how to further scale down reactions        
        stiff_cut = 100                     # minimum time scale separation
        delta_sdf = np.ones(self.KMC_system.data.Reactions['nrxns'])    # initialize the marginal scaledown factors        
        
        # data analysis
        freqs = self.KMC_system.data.Procstat['events'][-1,:]
        fwd_freqs = freqs[0::2]
        bwd_freqs = freqs[1::2]
        net_freqs = fwd_freqs - bwd_freqs
        tot_freqs = fwd_freqs + bwd_freqs
        frac_total = tot_freqs.astype(float) / (np.sum(tot_freqs) + 1)
        for i in range(len(tot_freqs)):
            if frac_total[i] > (1.0 - 1.0 / stiff_cut):
                other_events = np.sum(tot_freqs) + 1 - tot_freqs[i]
                freq_desired = 99 * other_events
                delta_sdf[i] = freq_desired.astype(float) / tot_freqs[i]
        
        return delta_sdf
 
    def WriteScaledownSummary(self,flname):
        # Print reaction names and scaledown factors into a file
        print 'Write scaledown summary'        
        
    def ReadScaledownSummary(self,flname):
        # Read reaction names and scaledown factors from a file
        print 'Read scaledown summary'
    
    def PlotStiffnessReduction(self):
        
        # Data
        SDF_dims = self.SDF_mat.shape
        n_iterations = SDF_dims[0]
        n_rxns = SDF_dims[1]
        iterations = range(n_iterations)
        rxn_labels = []
        
        # Plotting
        mat.rcParams['mathtext.default'] = 'regular'
        mat.rcParams['text.latex.unicode'] = 'False'
        mat.rcParams['legend.numpoints'] = 1
        mat.rcParams['lines.linewidth'] = 2
        mat.rcParams['lines.markersize'] = 16
        
        plt.figure()
        
        for i in range(n_rxns):
            plt.plot(iterations, np.transpose(self.SDF_mat[:,i]), 'o-', markersize = 15)
            rxn_labels.append(self.KMC_system.data.Reactions['Input'][i]['Name'])   
        
        plt.xticks(size=24)
        plt.yticks(size=24)
        plt.xlabel('iterations',size=30)
        plt.ylabel('scaledown factor',size=30)
        plt.legend(rxn_labels,loc=1,prop={'size':20},frameon=False)
        plt.show()
        
        plt.yscale('log')
        ax = plt.subplot(111)
        pos = [0.2, 0.15, 0.7, 0.8]
        ax.set_position(pos)