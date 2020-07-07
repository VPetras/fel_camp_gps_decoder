#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
# GPS-decoder
# Title: This script decode gps data of the protocol NMEA 0183 (GPGGA)
# Author: Vojtěch Petrásek 
# Generated: 07/07/2020 17:31:28
##################################################


####
# input data
###

num_1 = '087C3E76'
num_2 = '1DD6CA43'

###
# hex to int decode
###

num_1 = int(num_1, 16)
num_2 = int(num_2, 16)

###
# parsing data into NMEA starndart
###

lat = str((num_2 // 10000000) + (num_2 % 10000000)/6000000)
lon = str((num_1 // 10000000) + (num_1 % 10000000)/6000000)

print('lat: ' + lat + ' lon: ' + lon)
#50.1026244N, 14.3933639E
