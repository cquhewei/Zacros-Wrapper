# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:48:34 2016

@author: mpnun
"""

from KMCrun import KMCrun
from KMC_batch import KMC_batch
import os
import numpy as np
import matplotlib.pyplot as plt

#import sys
#import subprocess
#import pickle
#import matplotlib.pyplot as plt

################################################################

os.system('cls')
#RunPath = 'C:/Users/mpnun/Documents/Local_research_files/ZacrosWrapper/BigJobs/JobBuilds/AtoB/0111/'
#RunPath = 'C:/Users/mpnun/Documents/Local_research_files/ZacrosWrapper/BigJobs/JobBuilds/WGS/111/'
BatchPath = 'C:/Users/mpnun/Desktop/COox/Scaledown/Iteration_1/'
#BatchPath = 'C:/Users/mpnun/Documents/Local_research_files/ZacrosWrapper/BigJobs/JobBuilds/AtoB/'
#BatchPath = 'C:/Users/mpnun/Desktop/WGStest/'

''' Single run '''
#y = KMCrun()
#y.output.Path = RunPath
#y.output.ReadAllOutput()
#TOF = y.ComputeTOF('CO2')
#y.PlotSurfSpecVsTime()
#y.PlotGasSpecVsTime()
#y.PlotElemStepFreqs()

''' Group of runs '''

# Test batch of runs ----------------
x = KMC_batch()
x.ParentFolder = BatchPath
x.ReadMultipleRuns()
x.AverageRuns()


x.runAvg.PlotSurfSpecVsTime()
x.runAvg.PlotGasSpecVsTime()
x.runAvg.PlotElemStepFreqs()
#x.WvarCheck() 

#x.ComputeStats('CO2')
#x.ComputeStats('B')
#x.PlotSensitivities()
#x.WriteSA_output(BatchPath)