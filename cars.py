# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:50:37 2020

@author: PC
"""

import requests
from bs4 import BeautifulSoup
from csv import writer

durl = "https://www.cars.com/for-sale/searchresults.action/?page=1&perPage=20&prMx=1000&rd=100&searchSource=GN_REFINEMENT&sort=relevance&zc=ENTERZIPHERE"
response = requests.get(durl, verify = False)
if response.status_code == 200:
    #print(response.text)
    #print("good")
    soup = BeautifulSoup(response.text, 'html.parser')
    #balance2 = soup.find(class_='pedprice')
    #balance = balance2.contents[0]
    #print (balance)
    cars = soup.findAll(class_='listing-row__title')
    #print (cars)
    mileage = soup.findAll(class_='listing-row__mileage')
    price = soup.findAll(class_='listing-row__price ')
    distance = soup.findAll(class_='listing-row__distance ')
    wontwork = soup.findAll(class_='listing-row__details')
    #print (wontwork)
    with open('cars.csv', 'w', newline='') as csv_file:
        write = writer(csv_file)
        headers = ['Year', 'Make', 'Model', 'Extras', 'Mileage', 'Price', 'Distance']
        write.writerow(headers)
        #for car in cars:
            #name = (car.get_text('listing-row__title'))
            #miles = (car.get_text('listing-row__mileage'))
            #price = (car.get_text('listing-row__price '))
            #distance = (car.get_text('listing-row__distance '))
            #write.writerow([name, miles, price, distance])
            ##print (name)
            ##print (mileage[0].get_text('listing-row__mileage'))
            #for car2 in mileage:
            #    miles = (car2.get_text('listing-row__mileage'))
            #    print (miles)
        for i in range(18):
            name =  (cars[i].get_text('listing-row__title'))
            split = name.split()
            year = split[0]
            make = split[1]
            model = split[2]
            #extras = split[3]
            #print (split)
            #print (year)
            #print (make)
            #print (model)
            #print ("done")
            extravar = ""
            number = len(split)
            for x in range(3, number):
                #print (split[x])
                extravar += split[x] + ' '
            #print (extras)
            #print (extravar)
            miles = (mileage[i].get_text('listing-row__milesage'))
            prices = (price[i].get_text('listing-row__price '))
            far = (distance[i].get_text('listing-row__distance '))
#            print (name)
 #           print (miles)
  #          print (prices)
   #         print (far)
            write.writerow([year, make, model, extravar, miles, prices, far])
            
else:
    print (response.text)
    print(response.status_code)
    
