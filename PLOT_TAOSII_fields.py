#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:10:45 2020

@author: seba
"""

import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)


def gal2eq(l_gal, b_gal):

    # Transforms equatorial coordinates to galactic ones.

    gal = SkyCoord(l_gal, b_gal, unit=u.deg, frame='galactic')
    eq = gal.transform_to('icrs')

    # Minus appears bcause of “mapping from the inside” issue
    l_eq, b_eq = -eq.ra.wrap_at('180d').radian, eq.dec.radian

    return l_eq, b_eq


def ecl2eq(lon_ecl, lat_ecl):

    # Transforms ecliptic coordinates to equatorial ones.

    ecl = SkyCoord(lon_ecl, lat_ecl, unit=u.deg,
                   frame='barycentricmeanecliptic')
    eq = ecl.transform_to('icrs')

    # Minus appears bcause of “mapping from the inside” issue
    lon_eq, lat_eq = -eq.ra.wrap_at('180d').radian, eq.dec.radian

    return lon_eq, lat_eq


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Campos = pd.read_csv('TAOS_fields.csv', header=1)

RA_fields = Campos['RA_EQ_dec']
DEC_fields = Campos['Dec_EQ_dec']
Campo = Campos['Field']
f_view = 1.7
df = f_view/2

# Galactic plane
l_gal_all = np.linspace(-180, 180, 1000)
b_gal_0 = np.zeros(1000)
l_eq, b_eq = gal2eq(l_gal_all, b_gal_0)

# Ecliptic plane
lon_ecl = np.linspace(0, 360, 1000)
lat_ecl = np.zeros(1000)
lon_eq, lat_eq = ecl2eq(lon_ecl, lat_ecl)


# ORIGEN DEL PLOT, 0 or a multiple of 30 degrees in [0,360), 0 or a multiple of 30 degrees in [0,360)
origen = 0
x = np.remainder(RA_fields+360-origen, 360)  # CAMBIO EN LOS VALORES DE RA
ind = x > 180
x[ind] -= 360                                # ESCALA DE -180 A 180
x = -x                                       # CAMBIO DE ESCALA AL ESTE A LA IZQUIERDA
tick_labels = ['150°', '120°', '90°', '60°', '30°',
               '0°', '330°', '300°', '270°', '240°', '210°']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='mollweide')

ax.scatter(l_eq, b_eq, s=3, marker='o', alpha=0.7,
           color='orange', label='Galactic plane')
# ax.plot(l_eq, b_eq, linestyle='dashed', color='orange',
# label='Plano galáctico', linewidth=0.95)

ax.scatter(lon_eq, lat_eq, s=3, marker='o', alpha=0.7,
           color='steelblue', label='Ecliptic plane')
# ax.plot(lon_eq, lat_eq, linestyle='dotted', color='steelblue',
# label='Eclíptica', linewidth=0.95)

ax.scatter(np.radians(x), np.radians(DEC_fields), s=10,
           marker='o', c='purple', alpha=0.7,
           edgecolors='black', linewidth=0.3, zorder=1, label='TAOS-II fields')  # convert degrees to radians

ax.set_xticklabels(tick_labels)             # ESCALA DEL EJE X
#ax.set_title('Campos de TAOS-II')
ax.title.set_fontsize(10)
ax.set_xlabel("Right Ascension[°]")
ax.xaxis.label.set_fontsize(10)
ax.set_ylabel("Declination [°]")
ax.yaxis.label.set_fontsize(10)
ax.grid(True)
ax.legend(loc='best')
#ax.scatter(l_ecl_gal, b_ecl_gal, s=4, marker='^', label='Eclptic')
fig.savefig('TAOSII_FIELDS.png', dpi=300,rasterized=False)
