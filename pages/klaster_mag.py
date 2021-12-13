import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import re

def app():
    st.title('Klasterisasi Berdasarkan Magnitudo dan Kedalaman Gempa Bumi')

    st.write("""
    Klasterisasi berdasarkan magnitudo dan kedalaman gempa bumi di Indonesia dilakukan menggunakan algoritma **KNN**.

    """)

    data = pd.read_csv('data_clean.csv')

    df = data.drop(data[data['M'] < 4].index)
    df.reset_index(drop=True)

    data_cluster_mag = df.iloc[:, [2, 3]].values

    kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
    y_kmeans = kmeans.fit_predict(data_cluster_mag)

    
    
    plt.scatter(data_cluster_mag[y_kmeans == 0, 0], data_cluster_mag[y_kmeans == 0, 1], s = 10, c = 'blue', label = 'Cluster 1')
    plt.scatter(data_cluster_mag[y_kmeans == 1, 0], data_cluster_mag[y_kmeans == 1, 1], s = 10, c = 'red', label = 'Cluster 2')
    plt.scatter(data_cluster_mag[y_kmeans == 2, 0], data_cluster_mag[y_kmeans == 2, 1], s = 10, c = 'magenta', label = 'Cluster 3')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'yellow', label = 'Centroids')
    plt.title('Cluster gempa bumi di indonesia 2021 dengan KNN n=3')
    plt.xlabel('Kedalaman (Depth)')
    plt.ylabel('Magnitudo (M)')
    plt.legend()

    
    st.pyplot(plt)

    st.write("""
    Gambar diatas merupakan klasterisasi yang berhasil dibuat dengan menggunakan algoritma KNN dan n=3.
    Klaster yang terbentuk membagi data kedalam 3 bagian yang jika diperhatikan membentuk sebuah garis vertikal pada kedalaman tertentu.
    Ternyata klaster yang terbentuk memiliki kemiripan dengan pembagian kedalaman gempa (_Depth of Focus_)
    Menurut USGS[1] _Depth of Focus_ merujuk pada kedalaman terjadinya suatu gempa bumi.

    terdapat 3 _Depth of Focus_, yaitu :
        - Shallow (<70Km)
        - Intermediate (70Km < Depth < 300Km)
        - Deep (300Km < Depth < 700Km)  


    Adapun jumlah anggota dalam klaster dapat dilihat pada piechart berikut



    """)
    st.text("\n")


    df['cluster'] = y_kmeans

    klaster_count = df['cluster'].value_counts()
    plt.figure(figsize=(2,2))
    plt.pie(klaster_count,
            labels = ['dangkal','sedang','dalam'],
            autopct = '%1.1f%%',
            colors = ['#D53032','#E67F0D','#93C572'],
            explode = [0.2,0,0],
            shadow = True)
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')
    plt.show()

    st.pyplot(plt)

    st.text("""

    Sumber :
    
    [1] USGS. Determining the Depth of an Earthquake. https://www.usgs.gov/programs/earthquake-hazards/determining-depth-earthquake
    
    """)
