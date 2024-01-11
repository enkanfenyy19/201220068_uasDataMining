import pickle
import streamlit as st

#Membaca model
import pickle

try:
    with open('breastcancer_model.sav', 'rb') as model_file:
        breastcancer_model = pickle.load(model_file)
    print("Model berhasil dimuat.")
except FileNotFoundError:
    print("File 'breastcancer_model.sav' tidak ditemukan.")
except Exception as e:
    print(f"Terjadi kesalahan saat memuat model: {e}")

#Judul web
st.title('Aplikasi Kanker Payudara')

#Membagi kolom
col1, col2, col3 = st.columns(3)

with col1 :
    Id = st.text_input ('Input nilai Id')

with col2 :
    Radius_mean = st.text_input ('Input nilai Radius Mean')

with col3 : 
    Texture_mean = st.text_input ('Input nilai Texture Mean')

with col1 :
    Perimeter_mean = st.text_input ('Input nilai Perimeter Mean')

with col2 :
    Area_mean = st.text_input ('Input nilai Area Mean')

with col3 :
    Smoothness_mean = st.text_input ('Input nilai Smoothness Mean')

with col1 :
    Compactness_mean = st.text_input ('Input nilai Compactness Mean')

with col2 :
    Concavity_mean = st.text_input ('Input nilai Concavity Mean')

with col3 :
    Concave_points_mean = st.text_input ('Input nilai Concave Points Mean')

with col1 :
    Symmetry_mean = st.text_input ('Input nilai Symmetry Mean')

with col2 :
    Fractal_dimension_mean = st.text_input ('Input nilai Fractal Dimension Mean')

with col3 :
    Radius_se = st.text_input ('Input nilai Radius Se')

with col1 :
    Texture_se = st.text_input ('Input nilai Texture Se')

with col2 :
    Perimeter_se = st.text_input ('Input nilai Perimeter Se')

with col3 :
    Area_se = st.text_input ('Input nilai Area Se')

with col1 :
    Smoothness_se = st.text_input ('Input nilai Smoothness Se')

with col2 :
    Compactness_se = st.text_input ('Input nilai Compactness Se')

with col3 :
    Concavity_se = st.text_input ('Input nilai Concavity Se')

with col1 :
    Concave_points_se = st.text_input ('Input nilai Concave Points Se')

with col2 :
    Symmetry_se = st.text_input ('Input nilai Symmetry Se')

with col3 :
    Fractal_dimension_se = st.text_input ('Input nilai Fractal Dimension Se')

with col1 :
    Radius_worst = st.text_input ('Input nilai Radius Worst')

with col2 :
    Texture_worst = st.text_input ('Input nilai Texture Worst')

with col3 :
    Perimeter_worst = st.text_input ('Input nilai Perimeter Worst')

with col1 :
    Area_worst = st.text_input ('Input nilai Area Worst')

with col2 :
    Smoothness_worst = st.text_input ('Input nilai Smoothness Worst')

with col3 :
    Compactness_worst = st.text_input ('Input nilai Compactness Worst')

with col1 :
    Concavity_worst = st.text_input ('Input nilai Concavity Worst')

with col2 :
    Concave_points_worst = st.text_input ('Input nilai Concave Worst')

with col3 :
    Symmetry_worst = st.text_input ('Input nilai Symmetry Worst')

with col1 :
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
