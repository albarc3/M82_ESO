from PSF_K import PSFK
from packages import*

#Aquí no se calcula el combined

directory='/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/K_aligned/' #Put your own directory
p = Path(directory) #To place us in the directory

#We want to exclude the second night
keys = ['imagetyp','OBJECT' , 'EXPTIME' , 'INSFLID' , 'INSFLNAM','FILTER','DATE-OBS']
ic1 = ImageFileCollection(directory, glob_include='*.fits', keywords=keys)

matches = (ic1.summary['DATE-OBS'] =='2015-01-31' )

filelist = ic1.summary['file'][matches]

filelist1 = list(sorted(p.glob('*.fits')))

for i in filelist:
    file=directory+i #we need the complete path
    PSFK(file)

PSFK(filelist1[-1]) #Combined
