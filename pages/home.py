import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def app():
    st.write("""
    # Klasterisasi Gempa Bumi di Indonesia Selama 2021

    Proyek ini dibuat sebagai tugas akhir proyek pada pelatihan Microcredential Certification Associate Data Scientist tahun 2021. Daftar Nama Kelompok yang mengerjakan tugas akhir ini adalah: 

    - Achmad Rafif Nst
    - Arnold Prajna
    - Muhammad Rhayhan Akbar

    #### Kelompok 8 ITS05

    Github : [indonesia-earthquake2021-cluster](https://github.com/skynetice/indonesia-earthquake2021-cluster)
    
    """)

  