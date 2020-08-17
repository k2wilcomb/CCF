import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os, sys
import time
from astropy.table import Table
from astropy.io import fits
import copy
from astropy.io import ascii
import csv

data = pd.read_csv('51Eri_b_highres_template_gaussconv_R4000_Kbb.csv', delim_whitespace=True)
print(data['wvs'],data['spectrum'])
waves = data['wvs']
fluxes = data['spectrum']
#Allmystuff=np.vstack((filenames,isitthere,xcen,ycen)).T
Allmystuff=np.vstack((waves, fluxes)).T
np.savetxt('ccf_51eri_mod.txt',Allmystuff, fmt = '%s')
