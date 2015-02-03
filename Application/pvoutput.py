#!/usr/bin/python
# -*- coding: utf-8 -*-

_author_            =   "Lars van der Voorden"
_version_           =   "1.0"
_date_              =   "03/02/2015"                #dd/mm/yyyy

import datetime 
import urllib
import urllib2

class PVoutput():

    api_key         =   ""
    sid             =   ""

    pvouturl        =   "http://pvoutput.org/service/r2/addstatus.jsp"

    now = datetime.datetime.now()

    def __init__(self, api_key, sid):
        self.api_key = api_key
        self.sid = sid

    def uploadMeasurements(self, energie_today, current_measurements):

        pvoutput_data = {   'key'   :   self.api_key,                   #API Key
                            'sid'   :   self.sid,                       #(PV-)System ID
                            'd'     :   self.now.strftime('%Y%m%d'),    #date
                            't'     :   self.now.strftime('%H:%M'),     #time (now)
                            'v1'    :   energie_today,                  #total kWh generation today 
                            'v2'    :   current_measurements['P AC'],   #current output power
                            'v6'    :   current_measurements['U DC'] }  #current PV voltage
        
        encoded_pvoutput_data = urllib.urlencode(pvoutput_data)

        request_obj = urllib2.Request(self.pvouturl + '?' + encoded_pvoutput_data)
        response_pvoutput = urllib2.urlopen(request_obj)

        return response_pvoutput.read()
