import pickle
import streamlit as st

#Membaca model
breastcancer_model = pickle.load(open('breastcancer_model.sav'))

#Judul web
st.title('Aplikasi Kanker Payudara')