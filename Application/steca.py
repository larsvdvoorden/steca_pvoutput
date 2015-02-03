#!/usr/bin/python
# -*- coding: utf-8 -*-

_author_            =   "Lars van der Voorden"
_version_           =   "1.0"
_date_              =   "03/02/2015"                #dd/mm/yyyy

import urllib2                                      #urllib2 for downloading measurement table
from HTMLParser import HTMLParser                   #for parsing measurement table

class Steca():

    #The IP-adres of the Steca inverter (webserver)
    ip_adres = ""

    def __init__(self, ip_adres):
        self.ip_adres = ip_adres

  
    def getMeasurementTable(self):
        steca_webserver_request = urllib2.Request('http://%s/gen.measurements.table.js' 
                                    % self.ip_adres )
        steca_webserver_respone = urllib2.urlopen(steca_webserver_request)
        steca_webserver_html = steca_webserver_respone.read()[16:-3]        #cut off the Javascript
        
        #Create a new parser and feed it
        steca_parser = StecaParser()
        steca_parser.feed(steca_webserver_html)

        #Return the parsed dict
        return steca_parser.getParsedData()

    def getEnergyGenerated(self):
        steca_webserver_energy_request = urllib2.Request('http://%s/gen.yield.day.chart.js' 
                                            % self.ip_adres )
        steca_webserver_energy_respone = urllib2.urlopen(steca_webserver_energy_request)
        steca_webserver_energy_html = steca_webserver_energy_respone.read()

        kWhLocation = steca_webserver_energy_html.index('kWh')

        energy_generated = steca_webserver_energy_html[(kWhLocation-6):kWhLocation].replace(" ", "")

        return int(float(energy_generated)*1000)






#Class for parsing the Steca HTML-page to an dict
class StecaParser(HTMLParser):
    
    temp_steca_data     =   []

    def handle_data(self, data):
       self.temp_steca_data.append(data)


    def parseToDict(self):
        parsed_steca_data   =   {}
        
        if self.temp_steca_data:   

            #Start by 4. The first (0,1,2,3) items are headers, no data         
            i = 4

            #place all the data from the measurement table into an dict
            while i < len(self.temp_steca_data):
                parsed_steca_data[self.temp_steca_data[i]] = self.temp_steca_data[(i+1)]
                i += 3
        else:
            print "No data from Steca inverter"
        return parsed_steca_data


    def getParsedData(self):
        data_dict = self.parseToDict()
        return data_dict

