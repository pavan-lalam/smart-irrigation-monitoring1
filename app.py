import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(layout="wide")

API_URL = "https://smart-irrigation-monitoring1.onrender.com"

data_store = []

st.title("🌱 Smart Irrigation Dashboard")

placeholder = st.empty()

while True:
    try:
        res = requests.get(API_URL)
        data = res.json()

        if data:
            data_store.append(data)

            df = pd.DataFrame(data_store)

            with placeholder.container():

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Moisture")
                    st.line_chart(df[["moistureA","moistureB","moistureC"]])

                with col2:
                    st.subheader("Temp & Humidity")
                    st.line_chart(df[["temp","humidity"]])

                st.write(df.tail(1))

    except:
        st.warning("Waiting for data...")

    time.sleep(2)
