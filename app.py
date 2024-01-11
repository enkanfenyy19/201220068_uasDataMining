import pickle
import streamlit as st

#Membaca model
breastcancer_model = pickle.load(open('breastcancer_model.sav', 'rb'))

#Judul web
st.title('Aplikasi Kanker Payudara')

Id = st.text_input ('Input nilai Id')

Radius_mean = st.text_input ('Input nilai Radius Mean')

Texture_mean = st.text_input ('Input nilai Texture Mean')

Perimeter_mean = st.text_input ('Input nilai Perimeter Mean')

Area_mean = st.text_input ('Input nilai Area Mean')

Smoothness_mean = st.text_input ('Input nilai Smoothness Mean')

Compactness_mean = st.text_input ('Input nilai Compactness Mean')

Concavity_mean = st.text_input ('Input nilai Concavity Mean')

Concave_points_mean = st.text_input ('Input nilai Concave Points Mean')

Symmetry_mean = st.text_input ('Input nilai Symmetry Mean')

Fractal_dimension_mean = st.text_input ('Input nilai Fractal Dimension Mean')

Radius_se = st.text_input ('Input nilai Radius Se')

Texture_se = st.text_input ('Input nilai Texture Se')

Perimeter_se = st.text_input ('Input nilai Perimeter Se')

Area_se = st.text_input ('Input nilai Area Se')

Smoothness_se = st.text_input ('Input nilai Smoothness Se')

Compactness_se = st.text_input ('Input nilai Compactness Se')

Concavity_se = st.text_input ('Input nilai Concavity Se')

Concave_points_se = st.text_input ('Input nilai Concave Points Se')

Symmetry_se = st.text_input ('Input nilai Symmetry Se')

Fractal_dimension_se = st.text_input ('Input nilai Fractal Dimension Se')

Radius_worst = st.text_input ('Input nilai Radius Worst')

Texture_worst = st.text_input ('Input nilai Texture Worst')

Perimeter_worst = st.text_input ('Input nilai Perimeter Worst')

Area_worst = st.text_input ('Input nilai Area Worst')

Smoothness_worst = st.text_input ('Input nilai Smoothness Worst')

Compactness_worst = st.text_input ('Input nilai Compactness Worst')

Concavity_worst = st.text_input ('Input nilai Concavity Worst')

Concave_points_worst = st.text_input ('Input nilai Concave Worst')

Symmetry_worst = st.text_input ('Input nilai Symmetry Worst')

Fractal_dimension_worst = st.text_input ('Input nilai Fractal Dimension Worst')

#Code untuk diagnosis
kanker_diagnosis = ''

#Membuat tombol untuk diagnosis
if st.button('Test Diagnosis Kanker Payudara'):
    kanker_diagnosis = breastcancer_model.predict([[Id, Radius_mean, Texture_mean, Perimeter_mean, Area_mean, Smoothness_mean, Compactness_mean, Concavity_mean, Concave_points_mean, Symmetry_mean, Fractal_dimension_mean, Radius_se, Texture_se, Perimeter_se, Area_se, Smoothness_se, Compactness_se, Concavity_se, Concave_points_se, Symmetry_se, Fractal_dimension_se, Radius_worst, Texture_worst, Perimeter_worst, Area_worst, Smoothness_worst, Compactness_worst, Concavity_worst, Concave_points_worst, Symmetry_worst, Fractal_dimension_worst]])

if 'diagnosis' in ("M", "B") :
    print("Pasien terkena Kanker Payudara Ganas.")
else :
    print("Pasien terkena Kanker Payudara Jinak.")

st.success(kanker_diagnosis)
