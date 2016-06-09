# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 14:00:23 2016

@author: robieta
"""

from ClassFunctions.BuildInputFiles import BuildInputFiles as BI
from ClassFunctions.KMCUtilities import KMCUtilities as KMCut
from ClassFunctions.ProcessOutput import ProcessOutput as PO
from ClassFunctions.ReadInputFiles import ReadInputFiles as RI
from ClassFunctions.ReadOutputFiles import ReadOutputFiles as RO
from ClassFunctions.ReconditionStiffness import ReduceStiffness as RS
from ClassFunctions.RunZacros import RunZacros
from ClassFunctions.GeneralUtilities import GeneralUtilities as ut
import sys
import os
import numpy as np
import subprocess
import pickle
import matplotlib.pyplot as plt

"""
This section of the code reads the files from a given path and writes the info
to the Demo.p file for later use
"""
#Path = ut().SystemInformation()['Path']['Data'] + 'NH3/'
#Cnd = KMCut().InitializeCnd()
#Cnd = RI().ReadAll(Path,Cnd)
#Cnd = RO().ReadAll(Path,Cnd)
#KMCut().pickleCnd(Cnd,'NH3')




"""
This section of the code retreives and displays the python structure associated
with the Demo.p file
"""
#Cnd = KMCut().unpickleCnd('AtoB')
#ut().PrintDict(Cnd)


"""
This section of the code perfoms a stiffness reduction on the Demo system for 
the given reduction modes and saves the result in a .p file
"""
#ModeList = ['linear_1_2','linear_1.5_3']

TypeName = 'AtoB'
Mode = 'linear_1_2'
MaxEvents = 10000

# See if the reconditioning has already been done
if os.path.isfile(ut().SystemInformation()['Path']['Data'] + 'PickledRunStructures/' + 'Recondition_' + TypeName +'_' + Mode + '.p'): 
    os.remove(ut().SystemInformation()['Path']['Data'] + 'PickledRunStructures/' + 'Recondition_' + TypeName +'_' + Mode + '.p')
    
print 'Starting reconditioning'        
RS().ReconditionCnd(CndIn = KMCut().unpickleCnd(TypeName),Name=TypeName+'_' + Mode,RunParam = {'Event':1e3,'MaxEvents':MaxEvents,'Mode':Mode})



"""
This section builds jobs on Farber based on the prior stiffness reduction and
submits them
"""
#nRareSample = 500 # Estimate, can be off depending on the system
#nRuns = 5
#
#for i in range(len(ModeList)):
#    Mode = ModeList[i]
#    OutList = KMCut().unpickleCnd('Recondition_' + TypeName+'_' + Mode)
#    SDDict = KMCut().InitializeScaleDown()
#    SDDict['SF'] = OutList['SF']
#    SDDict['Mode'] = OutList['Cnd']['StiffnessRecondition']['Mode']
#    SDDict['SDF'] = RS().CalculateScaleDown(BaseCnd='',Mode=SDDict['Mode'],SFIn=SDDict['SF'])['SDF']
#    Cnd = OutList['Cnd']
#    
#    ETsS = np.log10(np.sum(SDDict['SF']/SDDict['SDF'])) # Estimated Timescale separation (for run time estimates)
#    Cnd = KMCut().SetMaxEventNumber(Cnd,ETsS,nRareSample)
#    JobPath = ut().SystemInformation()['Path']['Data'] + 'JobBuilds/' + TypeName+'_' + Mode + '/'
#    if not os.path.isdir(JobPath):
#        BI().BuildJob(Cnd,SDDict=SDDict,nRuns=nRuns,Name = TypeName+'_' + Mode)    
#        if ut().SystemInformation()['OS'] == 'Linux':        
#            p = subprocess.Popen("cd " + JobPath + "; " + "chmod 744 ./SubmitKMC.sh;./SubmitKMC.sh"
#                            , stdout=subprocess.PIPE,shell=True)
#            sys.stdout.flush()
#        else:
#            for j in ut().GetDir(JobPath):
#                RunZacros().Run(JobPath + j + '/')




"""
This line goes through the job build folder, detects which jobs have completed
but have not been parsed, parses them, and saves the result
"""
#RO().ReadAllJobs()


"""
This line reads the output of a parsed job which can then be processed.
"""
#CndList = RO().ReadJobOutput('Demo_linear_1_2')


"""
This section takes the various stiffness reduction runs and plots them to show
the effect of stiffness reduction on observed rate.
"""
#yLim = [0,0.0015]
#RegFun = ['linear_','tanh_']
#Modes = ['1_2','2_4']

#nSites = 1
#RxnStoich = [-1,1]
#PropensityStoich = [-1,1,0,0]
#LineColors = ['k','b']
#RegFun = ['linear_']
#Modes = ['1_2','1.5_3']
#PO().PlotReductionComparison(TypeName + '_',Modes,RegFun,nSites,RxnStoich,PropensityStoich,LineColors)
                            
                            
                            
                            
                            
                            
                            
                            
