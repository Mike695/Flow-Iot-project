import streamlit as st
import pandas as pd
import numpy as np

mpl_long = 3.876716 # Montpellier's long 
mpl_lat = 43.610767 # Montpellier latitude

df = pd.DataFrame(
    # generates 50 random points in Montpellier
    np.random.randn(50,2)/[50,50]+[mpl_lat, mpl_long], 
    columns=['lat', 'lon']
    )

st.map(df)
