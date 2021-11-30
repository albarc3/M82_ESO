
from packages import*

#images from 1st night
directory='/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/K_aligned/'

keys = ['imagetyp','OBJECT' , 'EXPTIME' , 'INSFLID' , 'INSFLNAM','FILTER','DATE-OBS']
ic1 = ImageFileCollection(directory, glob_include='*.fits', keywords=keys)

matches = (ic1.summary['DATE-OBS'] =='2015-01-31' )
filelist = ic1.summary['file'][matches]

#for combined
p = Path(directory) #To place us in the directory
filelist1 = list(sorted(p.glob('*.fits')))




#PSF
directory1='/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/K_aligned/PSF_K/Trim/' #Put your own directory

p1 = Path(directory1) #To place us in the directory
PSFS = list(sorted(p1.glob('*.fits')))
n=len(PSFS)
print(n)
for i in np.arange(0,n-1): #n-1 to complete
    a=run_subtraction("{}".format(directory+filelist[i]), "{}".format(filelist1[-1]), "{}".format(PSFS[i]), "{}".format(PSFS[-1]))
    norm = simple_norm(a[0],percent=99)

    fig=plt.figure(figsize=(8,8))
    plt.imshow(a[0],norm=norm,  origin='lower', cmap='RdYlBu')
    plt.title("{}".format(Path(filelist[i]).stem))
    plt.colorbar()
    plt.close()

    #To save matplotlib
    fig.savefig('/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/K_aligned/Subtracted/'+'{}'.format(Path(filelist[i]).stem)+'_sub.jpg', bbox_inches='tight', dpi=150)

    #TO save .fits
    hdu = fits.PrimaryHDU(a[0])
    hdul = fits.HDUList([hdu])
    hdul.writeto('/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/K_aligned/Subtracted/'+'{}'.format(Path(filelist[i]).stem)+'_sub'+'.fits',overwrite='yes')
