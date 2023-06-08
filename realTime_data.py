#
# Launched from terminal with: streamlit run realTime_data.py
# ça lance un serveur web sur la machine qui sert une page web qui s'ouvre
# et détecte quand y a un changement dans le code / peut recharger page si nécessaire


import streamlit as st
import numpy as np
import pandas as pd
import time # to simulate real time data
import plotly.express as px # interactive charts

# read static csv from an online place
dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"
#age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome,deposit
#159,admin.,married,secondary,no,2343,yes,no,unknown,5,may,1042,1,-1,0,unknown,yes
#56,admin.,married,secondary,no,45,no,no,unknown,5,may,1467,1,-1,0,unknown,yes

st.set_page_config(
    page_title = 'Real-Time Data Science Dashboard',  # important pour le référencement sur Google quand on hébergera l'app
    page_icon = '✅',
    layout = 'wide'
)

# read csv from a URL just at start of the app
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()
st.title("Real-Time / Live Data Science Dashboard")

# top-level filters
# défini un widget graphique pour choisir un métier parmi ceux listés dans le jeu de données
job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

# on filtre le dataframe en fonction de ce qui est choisi dans le widget job_filter
df = df[df["job"] == job_filter]

# affiche le dataframe filtre
#st.dataframe(df[0:5]) # n'affiche que les 5 premières lignes
# fait maintenant plus bas

# creating a single-element container
placeholder = st.empty()
# Insert a single-element container.
# Inserts a container into your app that can be used to hold a single element. This allows you to, for example, remove elements at any point, 
# or replace several elements at once (using a child multi-element container).
# To insert/replace/clear an element on the returned container, you can use "with" notation or just call methods directly on the returned object. 


# near real-time / live feed simulation
for seconds in range(200):

    df["age_new"] = df["age"] * np.random.choice(range(1, 5))
    df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

    # creating KPIs
    avg_age = np.mean(df["age_new"])

    count_married = int(
        df[(df["marital"] == "married")]["marital"].count()
        + np.random.choice(range(1, 30))
    )

    balance = np.mean(df["balance_new"])

    with placeholder.container():
	    # la fonction container insère un conteneur multi-elements.
    	#Inserts an invisible container into your app that can be used to hold multiple elements. 
    	#This allows you to, for example, insert multiple elements into your app out of order.
    	# Et comme ils sont dans un st.empty() ca permettra de remplacer tous ces éléments d'un seul coup.

        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="Age ⏳",
            value=round(avg_age),
            delta=round(avg_age) - 10,
        )
        
        kpi2.metric(
            label="Married Count 💍",
            value=int(count_married),
            delta=-10 + count_married,
        )
        
        kpi3.metric(
            label="A/C Balance ＄",
            value=f"$ {round(balance,2)} ",
            delta=-round(balance / count_married) * 100,
        )

        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(
                data_frame=df, y="age_new", x="marital"
            )
            st.write(fig)
            
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="age_new")
            st.write(fig2)

        # 3D scatter plot grâce à plotly.express :
        threeDplot = px.scatter_3d(df, x='campaign', y='day', z='age',
              color='marital')
        st.write(threeDplot)

        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)


