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
    st.title('Klasterisasi Berdasarkan Lokasi Terjadinya Gempa Bumi')

    st.write("""
    Klasterisasi lokasi terjadinya gempa bumi di Indonesia dilakukan menggunakan algoritma **DBScan**.

    Algoritma ini dipilih karena menghasilkan dapat menghasilkan klaster yang cukup baik.
    """)
    st.text("\n")

    data = pd.read_csv('data_clean.csv')

    df = data.drop(data[data['M'] < 4].index)
    df.reset_index(drop=True)

    data_cluster = df.iloc[:, [1, 0]].values

    X = data_cluster

    db = DBSCAN(eps=2.5, min_samples=55).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    clusters = labels

    colors = ['royalblue', 'maroon', 'forestgreen', 'mediumorchid', 'tan', 'deeppink', 'olive', 'goldenrod', 'lightcyan', 'navy', 'black']
    vectorizer = np.vectorize(lambda x: colors[x % len(colors)])

    plt.figure(figsize=(12,6))
    plt.scatter(X[:,0], X[:,1], c=vectorizer(clusters))

    
    st.pyplot(plt)

    st.write("""
    Gambar diatas merupakan klasterisasi yang berhasil dibuat dengan menggunakan algoritma DBScan dengan nilai eps=2.5 dan min_sample=55 klasterisasi dengan DBScan dan parameter tersebut menghasilkan 4 klaster.
    
    Adapun titik hitam pada beberapa sudut klaster merupakan titik yang dianggap sebagai noise sehingga tidak termasuk kedalam klaster
    """)
