import streamlit as st
import pandas as pd

file = st.file_uploader("Upload a file", type=["csv", "txt"])

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())
    
        
        