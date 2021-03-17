import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

# =============================================================================
# Graficar WD en campos de TAOS-II
# =============================================================================

Fields = pd.read_csv('TAOS_fields.csv', header= 0)

RA_fields =  Fields['RA_EQ_dec'] 
DEC_fields =  Fields['Dec_EQ_dec']
Campo = Fields['Field']

f_view = 1.7          # Diámetro de campo de visiión de TAOS-II
df = f_view/2

# =============================================================================
from Crossmatch import Crossmatch

ra  = Crossmatch["RA"]
dec = Crossmatch["DEC"]

# =============================================================================
plt.scatter(ra,dec,marker='*',color='m',s=1,label='White Dwarfs')

plt.errorbar(RA_fields, DEC_fields, ms=2,fmt='rs', label="data",
              xerr=df, yerr=df, ecolor='blue',capsize=30, elinewidth=1)
#plt.errorbar(RA_fields, DEC_fields, xerr=df, yerr=df)
plt.ylim(-60,60)
plt.xlim(0,360)
plt.ylabel('DEC')
plt.xlabel('RA')
plt.title('WDs en campos de TAOS 2')
plt.axvline(180, color='g', ls="solid")
plt.axhline(23.45, color='g', ls="dotted")
plt.axhline(0, color='g', ls="solid")
plt.axhline(-23.45, color='g', ls="dotted")
plt.show()