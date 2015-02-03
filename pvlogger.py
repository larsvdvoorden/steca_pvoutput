#!/usr/bin/python
# -*- coding: utf-8 -*-

_author_            =   "Lars van der Voorden"
_version_           =   "1.0"
_date_              =   "03/02/2015"                #dd/mm/yyyy

from Application.steca      import Steca
from Application.pvoutput   import PVoutput

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

#Replace with the IP-adres of the Steca inverter 
steca_ip            =   "192.168.x.x"

#Replace with the API-key from PVoutput.org
pvoutput_api_key    =   "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#Replace with the 'System Id' of your Steca inverter from PVoutput.org
pvoutput_sid        =   "xxxxx"

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

# 
# DO NOT CHANGE ANYTHING BELOW
#

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


#Create new Steca-object
steca                =  Steca(steca_ip)

#Create new PVoutput-object
pvOutput             =  PVoutput(pvoutput_api_key, pvoutput_sid);

current_measurements =  ""
energy_generated_day =  ""

#Get the data from the Steca inverter
try:
    current_measurements =  steca.getMeasurementTable()
except:
    print 'Not possible to get the Measurement table'

try:
    energy_generated_day =  steca.getEnergyGenerated()
except:
    print 'Not possible to get the generated energy'

if (energy_generated_day != "" and current_measurements != ""):
    print pvOutput.uploadMeasurements(energy_generated_day, current_measurements)
else:
    print 'Not uploaded to PVOutput'
