
import csv
import streamlit as st
import json
import streamlit as st
import time
from math import radians, sin, cos, asin,sqrt
import pandas as pd
# third-party imports (may need installing)
import requests
import csv


bikeData={}
bikeData['stops']=[]
bikeData['lon']=[]
bikeData['lat']=[]

with open ('BikeStations.csv','r') as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        if i[0] == 'ID':
            continue
        bikeData['stops'].append(i[3])
        bikeData['lon'].append(float(i [4]))
        bikeData['lat'].append(float(i [5]))

print(bikeData)
st.map(bikeData)
with st.form("my_form"):
   st.write("Inside the form")
  
   latInput = float(st.number_input('Insert a Lat',format='%f',step=0.000001))
   longInput = float(st.number_input('Insert a long',format='%f',step=0.000001))

  
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   #if submitted:
df=pd.DataFrame.from_dict(bikeData)
print(df)
      
def distance(lat1, long1,lat2, long2):
    #print(lat1,long1,lat2,long2)
    lat1,long1,lat2,long2=map(radians,[lat1,long1,lat2,long2])
    dlon=long2-long1
    dlat=lat2-lat1
    a= sin(dlat/2)**2+ cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*asin(sqrt(a))
    km=6371*c
    return km
rows=[]
def nearest(df):
    dist=[]
    stop=df['stops']
    lats=df['lat']
    lons=df['lon']
    for i in range(0,df.shape[0]):
       
    
        test=distance( latInput ,longInput  ,float(lats[i]),float(lons[i]))
        row=(stop[i],lats[i],lons[i],test)
        rows.append(row)
    min=100
    closest=rows[i]
    for i in range(0,len(rows)):
        if rows[i][3]<min:
            min=rows[i][3]
            closest=rows[i]

    print(min)
    maplat=[closest[1],latInput ]
    maplon=[closest[2],longInput ]
    mapdf={"lat":maplat,"lon":maplon}
    points=pd.DataFrame(data=mapdf)
    st.map(points)
temp=get_weather('43.605366','3.881346')
kelvin_to_F(temp)
   
        
nearest(df)
#print(rows)

    
