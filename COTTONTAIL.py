import pandas as pd
import numpy as np

def conditional(x_ob, y_ob, field, x_tf, y_tf):

    x = []
    y = []
    f = []

    # Diámetro de campo de visiión de TAOS-II
    f_view = 1.7
    df = f_view/2

    for i, ii in zip(x_ob, y_ob):
        for j, jj, jjj in zip(x_tf, y_tf, field):
            #cont += 1
            if j-df <= i <= j+df and jj-df <= ii <= jj+df:
                #print (iii,i,ii)
                x.append(i)
                y.append(ii)
                f.append(jjj)

    return x, y, f

# =============================================================================
# Extrating coordinates of objects to apply the conditional algorith
# =============================================================================


def crossmatch(file, coor_bool):

    col_Names = ['RA', 'DEC']
    objects_data = pd.read_csv(str(file)+'.csv', header=0)

    X = objects_data['RA']
    Y = objects_data['DEC']

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Fields = pd.read_csv('TAOS_fields.csv', header=1)
    
    if coor_bool == 0:    # equatorial

        RA_fields = Fields['RA_EQ_dec']
        DEC_fields = Fields['Dec_EQ_dec']
        Campo = Fields['Field']

        x, y, f = conditional(X, Y, Campo, RA_fields, DEC_fields)
        Crossmatch = pd.DataFrame({"RA": x, "DEC": y, "Field": f})

    elif coor_bool == 1:   # galactic

        Lon_fields = Fields['Gal_Lon_deg']
        Lat_fields = Fields['Gal_Lat_deg']
        Campo = Fields['Field']

        x, y, f = conditional(X, Y, Campo, Lon_fields, Lat_fields)
        Crossmatch = pd.DataFrame({"RA": x, "DEC": y, "Field": f})

    else:
        print('ERROR: Wrong coordinates system \n Try again')
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # saving the dataframe 
    Crossmatch.to_csv('objects_in_TAOSII_fields.csv')
    
    return Crossmatch
