#add fits files together

import glob
from scipy.signal import convolve, boxcar
import scipy
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import emcee
import osiris_fmp as nspf
import corner
import os, sys
import time
from astropy.table import Table
from astropy.io import fits
import copy
import pyfits
import scipy.io as spio
import matplotlib.image as mpimg

#frames to add together (no sky or moving back to star in between)
spec18 = 's190526_a018002_tlc_Kbb_050.fits' #fits data file
spec19 = 's190526_a019002_tlc_Kbb_050.fits'
spec20 = 's190526_a020002_tlc_Kbb_050.fits'
spec21 = 's190526_a021002_tlc_Kbb_050.fits'
spec22 = 's190526_a022002_tlc_Kbb_050.fits'
spec23 = 's190526_a023002_tlc_Kbb_050.fits'

#combos all days
hdulist18=fits.open(spec18)
hdulist19=fits.open(spec19)
hdulist20=fits.open(spec20)
hdulist21=fits.open(spec21)
hdulist22=fits.open(spec22)
hdulist23=fits.open(spec23)


#data from the files
data18=hdulist18[0].data
data19=hdulist19[0].data
data20=hdulist20[0].data
data21=hdulist21[0].data
data22=hdulist22[0].data
data23=hdulist23[0].data


#add up data
mosaic_gj_19026_18_23 = np.sum((data18,data19,data20,data21,data22,data23),axis=0)

outfile = 'stacked_gj19026_18_23.fits'
#save to new fits file
hdu = fits.PrimaryHDU(mosaic_gj_19026_18_23)
hdu.writeto(outfile, clobber=True)
