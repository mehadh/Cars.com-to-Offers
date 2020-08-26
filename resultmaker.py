# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 02:34:11 2020

@author: PC
"""
import requests
import csv
from bs4 import BeautifulSoup
theheaders = {'Content-type': 'application/x-www-form-urlencoded'}
rawfile = "cars.csv"
cleanedfile = "offers.csv"
firsttime = True
with open(rawfile, encoding="utf8") as infile, open(cleanedfile, 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    headers = ['Year', 'Make', 'Model', 'Extras', 'Mileage', 'Price', 'Distance', 'Offer']
    writer.writerow(headers)
    print("he wnt here")
    for row in reader:
        year = row[0]
        make = row[1]
        model = row[2]
        miles = row[4]
        numeric_filter = filter(str.isdigit, miles)
        numeric_string = "".join(numeric_filter)
        mileage = numeric_string
        print (mileage)
        title = "clean"
        zipcode = "ENTERZIPHERE"
        cleandata = "pyear="+year+"&pmake="+make+"&pmodel="+model+"&ptrim=&ptitle="+title+"&getoffer=69510b42ce&pvin=&pzip="+zipcode+"&pwheelstires=1&pwheelssub%5B%5D=wheels_removed_driver_front&pwheelssub%5B%5D=wheels_removed_passenger_front&pwheelssub%5B%5D=wheels_removed_driver_rear&pwheelssub%5B%5D=wheels_removed_passenger_rear&pstartdrive=drive&pstartsub%5B%5D=engine_transmission&pstartsub%5B%5D=engine_transmission_notintact&pstartsub%5B%5D=engine_transmission_removed&pdrive=yes&pstart=no&pmileage="+mileage+"&pexterior=no&pexteriorsub%5B%5D=body_panels_driver_front&pexteriorsub%5B%5D=body_panels_passenger_front&pexteriorsub%5B%5D=body_panels_driver_rear&pexteriorsub%5B%5D=body_panels_passenger_rear&pmirror=no&pmirrorsub%5B%5D=mirrors_lights_glass_driver_front&pmirrorsub%5B%5D=mirrors_lights_glass_passenger_front&pmirrorsub%5B%5D=mirrors_lights_glass_driver_rear&pmirrorsub%5B%5D=mirrors_lights_glass_passenger_rear&pbody=no&pbodysub%5B%5D=body_damage_driver_front&pbodysub%5B%5D=body_damage_passenger_front&pbodysub%5B%5D=body_damage_driver_rear&pbodysub%5B%5D=body_damage_passenger_rear&pinterior=yes&pflood=yes&pvinlast=no&pvinfinal="
        data = {"action": "pulloffer", "nc": "69510b42ce", "data": str(cleandata)}
        durl = "https://www.cashautosalvage.com/wp-admin/admin-ajax.php"
        response = requests.post(durl, data, headers=theheaders, verify = False)
        if response.status_code == 200:
            #print(response.text)
            soup = BeautifulSoup(response.text, 'html.parser')
            balance2 = soup.find(class_='pedprice')
            if balance2 is None:
                print("aww")
                print(year+make+model+miles)
                if firsttime:
                    firsttime = False
                else:
                    oldmodel = model
                    extras = row[3]
                    split = extras.split()
                    new = oldmodel+"+"+split[0]
                    #print (new)
                    model = new
                    response2 = requests.post(durl, data, headers=theheaders, verify = False)
                    if response2.status_code == 200:
                        soup2 = BeautifulSoup(response.text, 'html.parser')
                        balance22 = soup.find(class_='pedprice')
                        if balance22 is None:
                            print(year+" "+make+" "+model+" "+mileage+"was unparseable")
                        else:
                            print("something didnt parse but now it did")
                            balance3 = balance22.contents[0]
                            row.append(balance3)
                            writer.writerow(row)
                    
            else:
                print(year+make+model+miles)
                balance = balance2.contents[0]
                print (balance)
                row.append(balance)
                writer.writerow(row)
        else:
            print (response.text)
            print(response.status_code)
    
