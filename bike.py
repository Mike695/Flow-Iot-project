# stdlib imports
import json
import streamlit as st
import time
from math import radians, sin, cos, asin,sqrt
import pandas as pd
# third-party imports (may need installing)
import requests
import csv

# Creating csv file
myfile = open('BikeStations.csv', 'w', newline='')
csvwriter = csv.writer(myfile) # 2. create a csvwriter object
csvwriter.writerow(['ID','totalSlotNumber','City','Street','Longitude','Latitude']) ## 4. write the header
    

info={}

#Looping on every dock station (57 known)
for i in range(1,60): 
    # Formating URL
    addedstr=str(i)
    if i < 9:
        addedstr = '0'+addedstr
    url='https://portail-api-data.montpellier3m.fr/bikestation?id=urn%3Angsi-ld%3Astation%3A0'+addedstr+'&limit=1'
    # Sending request
    response = requests.get(url)

    # Translating byte response to Python data structures
    response_json = response.json()
    if len(response_json)>0:
        ## Print Raw Data
        #print(response_json)

        # Extracting data from Json
        data=[response_json[0]['id'].replace(":","%3"),
            response_json[0]['totalSlotNumber']['value'],
            response_json[0]['address']['value']['addressLocality'],
            response_json[0]['address']['value']['streetAddress'],
            response_json[0]['location']['value']['coordinates'][0],
            response_json[0]['location']['value']['coordinates'][1]
            ]
        
        
        # Print Extracted data
        #print(data)

        # Wrinting Values in csv
        csvwriter.writerow(data) # 5. write the rest of the data
    info['lat']=data[4]

bikeData={}

bikeData['long']=[]
bikeData['lat']=[]

with open ('/home/michael.woods/BikeStations.csv','r') as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        if i[0] == 'ID':
            continue
        bikeData['lon'].append(float(i [4]))
        bikeData['lat'].append(float(i [5]))

 

#df=pd.DataFrame(,columns=['data'])    
with st.form("my_form"):
   st.write("Inside the form")
  
   lat1 = st.number_input('Insert a Lat',format='%f',step=0.000001)
   long1 = st.number_input('Insert a long',format='%f',step=0.000001)

  
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       s
       st.write('The current number is ', number)


def distance(lat1, long1,long2, lat2):
    lat1,long1,lat2,long2=map(radians,[lat1,long1,lat2,long2])
    dlon=long2-long1
    dlat=lat2-lat1
    a= sin(dlat/2)**2+ cos(lat1)*cos(lat2)*sin(dlon/2)
    c=2*asin(sqrt(a))
    km=-6371*c
    return km

#def nearest(num1,num2):
    
    
    


st.write("Outside the form")
st.map(bikeData)


st.write(time.asctime(time.localtime()))
myfile.close()