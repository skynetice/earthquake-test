import streamlit as st
from multiapp import MultiApp
from pages import page1, klaster_lokasi, klaster_mag, view_data, home



app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data Gempa", view_data.app)
app.add_app("Titik gempa", page1.app)
app.add_app("Klaster Lokasi", klaster_lokasi.app)
app.add_app("Klaster Magnitudo", klaster_mag.app)


# The main app
app.run()
