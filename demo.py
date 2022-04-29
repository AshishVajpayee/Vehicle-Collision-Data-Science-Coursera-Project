import streamlit as st
import pandas as pd


st.write("Hello World")

st.map()

DATA_URL = (
    "Motor_Vehicle_Collisions_-_Crashes.csv"
)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    data.head()
data = load_data(100000)