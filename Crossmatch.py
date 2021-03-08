import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

# =============================================================================
# WD en Crossmatch de GDR2
# =============================================================================

Tabla_GDR2 = pd.read_csv('J_MNRAS_482_4570_gaia2wd.csv', header= 0)
"""
RA   = Tabla_GDR2['_RAJ2000']
DEC  = Tabla_GDR2['_DEJ2000']
Name = Tabla_GDR2['WD']
SDSS = Tabla_GDR2['SDSS']
Pwd  = Tabla_GDR2['Pwd']

#SpC  = Tabla_GDR2['SpClass']

G_mag = Tabla_GDR2['Gmag']
BP_mag = Tabla_GDR2['BPmag']
RP_mag = Tabla_GDR2['RPmag']

TeffH = Tabla_GDR2['TeffH']
LoggH = Tabla_GDR2['loggH']
MassH = Tabla_GDR2['MassH']
Plx = Tabla_GDR2['Plx']
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Campos = pd.read_csv('TAOS_fields.csv', header= 0)

RA_fields =  Campos['RA_EQ_dec'] 
DEC_fields =  Campos['Dec_EQ_dec']
Campo = Campos['Field']
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ra = []
dec = []
name = []
sdss = []
pwd = []
g = []
bp = []
rp = []
massh = []
teffh = []
loggh = []
plx = []

f_view = 1.7          # Diámetro de campo de visiión de TAOS-II
df = f_view/2

cont = 1
for i,ii,iii,i4,i5,i6,i7,i8,i9,i10,i11,i12 in zip (RA,DEC,Name,SDSS,Pwd,G_mag,BP_mag,RP_mag,TeffH,MassH,LoggH,Plx):
    for j,jj,jjj in zip (RA_fields,DEC_fields,Campo):        
        #cont += 1
        if j-df <= i <= j+df and jj-df <= ii <= jj+df:
            #print (iii,i,ii)
            ra.append(i)
            dec.append(ii)
            name.append(iii)
            sdss.append(i4)
            pwd.append(i5)
            g.append(i6)
            bp.append(i7)
            rp.append(i8)
            massh.append(i9)
            teffh.append(i10)
            loggh.append(i11)
            plx.append(i12)

# sys.exit()
Crossmatch = pd.DataFrame({"WD_name":name,"SDSS":sdss,"RA":ra, "DEC":dec,
                           'Pwd':pwd, "G_mag":g,"BP_mag":bp,"RP_mag":rp,
                           'TeffH':teffh,'MassH':massh,'LoggH':loggh,'Parallax':plx})
Crossmatch_OK = Crossmatch.drop_duplicates(subset=['WD_name',"SDSS"], keep='first')

# saving the dataframe 
Crossmatch.to_csv('Crossmatch_PP_Marzo_gdr2.csv')