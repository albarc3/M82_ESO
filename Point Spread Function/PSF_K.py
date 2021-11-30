from packages import*

def PSFK(file):

    HDUList_object = fits.open(file)
    data_K=HDUList_object[0].data
    header_K = HDUList_object[0].header


# ## 2. Define stars' coordinates


    x=[736.56,933.47,689.55,743.54,442.01,962.49,326.63,919.69,665.57,901.68]
    y=[671.60,451.85,454.80,862.49,651.36,564.27,850.40,680.52,797.60,495.36]

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

    stars = extract_stars(nddata, stars_tbl, size=80)  #Size is the number of pixels. In this case 50x50


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




    data_image = CCDData(b,unit=u.adu)

    #get_ipython().run_line_magic('cd', '/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/K_aligned/PSFK/')
    hdu = fits.PrimaryHDU(b)
    hdul = fits.HDUList([hdu])
    hdul.writeto("/Users/alba/Desktop/ESO/Data/KOA_118904/NIRC2/calibrated/K_aligned/PSF_K/"+Path(file).stem +"_PSF_K.fits",overwrite='yes')

    pass
