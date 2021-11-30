from packages import*

def PSFH(file):

    HDUList_object = fits.open(file)
    data_K=HDUList_object[0].data
    header_K = HDUList_object[0].header


# ## 2. Define stars' coordinates


    x=[223.46,338.65,815.77,94.71,640.49,632.87,561.50,830.50,585.58,858.94]
    y=[754.26,552.42,585.37,338.99,766.38,576.49,702.49,356.52,359.33,468.16]

    peaks_tbl=pd.DataFrame({'x':x,'y':y})




# ## 3. Extract stars data



    x = peaks_tbl['x']
    y = peaks_tbl['y']

    stars_tbl = Table() #To do an astropy table
    stars_tbl['x'] = x
    stars_tbl['y'] = y

# The ***extract_stars()*** function requires the input data as an NDData object. The key distinction from raw *numpy.ndarray* is the presence of additional metadata such as uncertainty, mask, unit, a coordinate system and/or a dictionary containing further meta information. This class only provides a container for storing such datasets. An NDData object is easy to create from our data array:

# In[12]:

    nddata = NDData(data=data_K)

    stars = extract_stars(nddata, stars_tbl, size=95)  #Size is the number of pixels. In this case 50x50


# ## 4. Plot the extracted stars to take a look



# ## 5. Calculate and plot the e-PSF


    epsf_builder = EPSFBuilder(oversampling=1, maxiters=1,progress_bar=False)
    epsf, fitted_stars = epsf_builder(stars)


# In[17]:


    a=epsf.data


# In[18]:


    b=a/a.sum()


# In[19]:


    b.sum() #normalized


# In[20]:


    plt.figure(figsize=(8,8))
    norm = simple_norm(b, 'log',percent=99.)
    plt.imshow(b, norm=norm, origin='lower', cmap='viridis')
    plt.title('Effective PSF')
    plt.colorbar()
    plt.show()
    plt.close()




    data_image = CCDData(b,unit=u.adu)

    #get_ipython().run_line_magic('cd', '/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/K_aligned/PSFK/')
    hdu = fits.PrimaryHDU(b)
    hdul = fits.HDUList([hdu])
    hdul.writeto("/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/H_aligned/PSF_H/"+Path(file).stem +"_PSF_H.fits",overwrite='yes')

    pass
