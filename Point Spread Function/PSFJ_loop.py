from PSF_J import PSFJ
from packages import*

directory='/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/J_aligned/' #Put your own directory
p = Path(directory) #To place us in the directory


filelist = list(sorted(p.glob('*.fits')))

for i in filelist:
    PSFJ(i)
