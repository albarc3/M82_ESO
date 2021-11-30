from packages import*

directory='/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/K_aligned/PSF_K/'
p = Path(directory) #To place us in the directory
filelist = list(sorted(p.glob('*.fits')))

for i in filelist:
    hdu = fits.open(i)
    #image=fits.getdata('{}'.format(i))
    data=hdu[0].data
    header=hdu[0].header

    cents = np.where(data == np.max(data))
    xc = int(cents[1])
    yc = int(cents[0])

    bb=37  #43 ---> H #31----> J #37 ---->K
    datacut = data[yc-bb:yc+bb,xc-bb:xc+bb]
    hdu = fits.PrimaryHDU(datacut)
    hdul = fits.HDUList([hdu])
    hdul.writeto('/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/K_aligned/PSF_K/Trim/'+'{}'.format(Path(i).stem)+'.fits',overwrite='yes')
