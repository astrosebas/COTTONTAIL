import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def conditional(x_ob,y_ob,field,x_tf,y_tf):

    x = []
    y = []
    f = []

    # Diámetro de campo de visiión de TAOS-II
    f_view = 1.7          
    df = f_view/2

    for i,ii in zip (x_ob,y_ob):
        for j,jj,jjj in zip (x_tf,y_tf,field):        
            #cont += 1
            if j-df <= i <= j+df and jj-df <= ii <= jj+df:
                #print (iii,i,ii)
                x.append(i)
                y.append(ii)
                f.append(jjj)

    return x,y,f

# =============================================================================
# Extrating coordinates of objects to find
# =============================================================================
def crossmatch(file,type):
    
    objects_data = pd.read_csv(file)

    X   = objects_data[1]
    Y  = objects_data[2]

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    Fields = pd.read_csv('TAOS_fields.csv', header= 0)
    if type == 'equatorial':

        RA_fields =  Fields['RA_EQ_dec'] 
        DEC_fields =  Fields['Dec_EQ_dec']
        Campo = Fields['Field']

        x,y,f = conditional(X,Y,Campo,RA_fields,DEC_fields)
        Crossmatch = pd.DataFrame({"WD_name":x,"SDSS":y,"RA":f})

    elif type == 'galactic':
        Lon_fields =  Fields['Gal_Lon_deg']
        Lat_fields =  Fields['Gal_Lat_deg'] 
        Campo = Fields['Field']

        x,y,f = conditional(X,Y,Campo,Lon_fields,Lat_fields)
        Crossmatch = pd.DataFrame({"WD_name":x,"SDSS":y,"RA":f})       

    else:
        break
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # saving the dataframe 
    Crossmatch.to_csv('objects_in_TAOSII_fields.csv')