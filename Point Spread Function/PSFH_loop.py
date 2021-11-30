from PSF_H import PSFH
from packages import*

directory='/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/H_aligned/' #Put your own directory
p = Path(directory) #To place us in the directory

filelist = list(sorted(p.glob('*.fits')))

for i in filelist:
    file=i #we need the complete path
    PSFH(file)
