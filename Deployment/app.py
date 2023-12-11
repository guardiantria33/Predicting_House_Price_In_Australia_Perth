import streamlit as st
import eda
import prediction

halaman = st.sidebar.selectbox('Choice Page : ', ('eda', 'prediction'))

if halaman == 'eda' :
    eda.run()
else :
    prediction.run()