import streamlit as st
import pandas as pd
import numpy as np
import pickle
from feature_engine.outliers import Winsorizer
from klasifikasi_kota import klasifikasi_kota

# Load Model
with open('final_pipeline1.pkl', 'rb') as file_1:
  final_pipeline = pickle.load(file_1)

with open('klasifikasi_kota.pkl', 'rb') as file_2:
  cardinality = pickle.load(file_2)

#function run
def run() :
    data = pd.read_csv('all_perth_310121.csv')
    with st.form('House Pricing Prediction'):
        selected_suburb = st.selectbox('Pilih Suburb:', data['SUBURB'].unique())
        price = st.number_input('Price', min_value=0, max_value=2440000, value=0)
        bedroom = st.selectbox('Pilih Jumlah Bedroom:', data['BEDROOMS'].unique())
        bathroom = st.selectbox('Pilih Jumlah Bathroom:', data['BATHROOMS'].unique())
        landarea = st.number_input('Land Area', min_value=61, max_value=9999990, value=61, help ='Luas tanah dalam meter persegi')
        floorarea = st.number_input('Floor Area', min_value=1, max_value=870, value=1, help ='Luas lantai dalam meter persegi')
        cbddist = st.number_input('Central Business Distance', min_value=681, max_value=59800, value=681, help ='Menunjukkan Jarak ke Kawasan Pusat Bisnis (M)')
        stndist = st.number_input('Nearest Station Distance', min_value=46, max_value=35500, value=46, help ='Menunjukkan Jarak ke Stasiun Terdekat (M)')
        schdist = st.number_input('Nearest School Distance', min_value=0, max_value=23, value=0, help ='Menunjukkan Jarak ke Stasiun Terdekat (KM)')

        submitted = st.form_submit_button('Predict')

    data_inf = {
        'SUBURB': selected_suburb,
        'PRICE':price,
        'BEDROOMS':bedroom,
        'BATHROOMS' : bathroom,
        'LAND_AREA': landarea,
        'FLOOR_AREA': floorarea,
        'NEAREST_STN_DIST' : stndist,
        'NEAREST_SCH_DIST': schdist,
        'CBD_DIST': cbddist
    }
    
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
    # Melakukan klasifikasi kota
        data_inf['AREA'] = data_inf['SUBURB'].apply(klasifikasi_kota)

    # Memasukan Pipeline
        prediction_inf = final_pipeline.predict(data_inf)
        st.write('#Prediksi Harga Rumah Adalah Sebesar : AUD ', str(int(prediction_inf)))

if __name__ == '__main__':
    run()
