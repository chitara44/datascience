# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 00:30:09 2020

@author: Ricardo
"""

from geopy.geocoders import Nominatim
geolocalizador=Nominatim()
ubicacion=geolocalizador.reverse('4.6621712,-74.0881987')
print(ubicacion.address)