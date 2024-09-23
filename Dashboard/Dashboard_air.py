import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import folium
from streamlit_folium import st_folium
sns.set(style='dark')

# Judul Proyek
st.title("Proyek Analisis Data: Air Quality")

# Nama dan Info
st.markdown("""
**Nama:** Nurul Alam  
**Email:** iyungalam5@gmail.com  
**ID Dicoding:** [Link ke Profil](https://www.dicoding.com/users/iyungalam)
""")

# Pertanyaan Bisnis
st.header("Pertanyaan Bisnis")
st.markdown("""
1. Bagaimana perbedaan tingkat polutan di berbagai stasiun?  
2. Korelasi antara suhu, kecepatan angin pada tingkat polutan (SO2, NO2, CO2, O3)  
3. Tingkat curah hujan berdasarkan stasiun  
4. Pada stasiun mana suhu mencapai derajat terendah dan tertingginya?  
""")



# Upload Dataset
all_df = pd.read_csv("https://raw.githubusercontent.com/iyungalam/AirQuality_Analyst/refs/heads/main/Dashboard/all_clean.csv")

datetime_columns = ["Date"]
all_df.sort_values(by="Date", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])
    
    volume_mean = all_df.groupby(by="station").agg({
    "RAIN": ["max", "min"],
})
    temp_df = all_df.groupby(by="station").agg({
    "TEMP": ["max", "min"],
})
    pollutant_mean = all_df.groupby(by="station").agg({
    "SO2": ["mean"],
    "NO2": ["mean"],
    "CO": ["mean"],
    "O3": ["mean"]
})
    pollutant_mean['kadar_polusi'] = pollutant_mean.mean(axis=1)


    ## Pertanyaan 1: Bagaimana perbedaan tingkat polutan di berbagai stasiun?
    st.header("Pertanyaan 1: Perbedaan Tingkat Polutan di Berbagai Stasiun")
    # Data yang diperlukan
    stations = pollutant_mean.index
    mean_pollutant_levels = pollutant_mean['kadar_polusi']
    
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    
    # Membuat bar chart
    bars = ax1.bar(stations, mean_pollutant_levels, color='skyblue')
    
    # Menambahkan teks di atas setiap bar
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height,
            f'{height:.2f}', ha='center', va='bottom', fontsize=10)
    
    # Menambahkan label dan judul
    ax1.set_xlabel('Station Name')
    ax1.set_ylabel('Rata-rata tingkat polusi')
    ax1.set_title('Rata-rata tingkat polusi di berbagai stasiun')
    ax1.set_xticks(range(len(stations)))
    ax1.set_xticklabels(stations, rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig1)

    ## Pertanyaan 2: Korelasi antara suhu, kecepatan angin pada tingkat polutan (SO2, NO2, CO2, O3)
    st.header("Pertanyaan 2: Korelasi antara suhu, kecepatan angin pada tingkat polutan (SO2, NO2, CO2, O3)")
    pollutants = ['CO', 'NO2', 'O3','SO2']  # Adjust with actual pollutant names
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    corr_matrix = all_df[['TEMP', 'WSPM'] + pollutants].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax2)
    ax2.set_title('Korelasi antara suhu, kecepatan angin pada tingkat polutan (SO2, NO2, CO2, O3)')
    plt.tight_layout()
    st.pyplot(fig2)

    ## Pertanyaan 3: Tingkat curah hujan berdasarkan stasiun
    st.header("Pertanyaan 3: Tingkat Curah Hujan Berdasarkan Stasiun")
    # Mengelompokkan data untuk mendapatkan curah hujan maksimal dan minimal
    volume_mean = all_df.groupby(by="station").agg({
        "RAIN": ["max", "min"],
        })
    # Data yang diperlukan
    stations = volume_mean.index
    max_rain_levels = volume_mean['RAIN']['max']
    
    # Membuat figure dan axis untuk bar chart
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    
    # Membuat bar chart
    bars = ax3.bar(stations, max_rain_levels, color='skyblue', label='Max Rain')
    
    # Menambahkan teks di atas setiap bar
    
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width() / 2, height,
            f'{height:.2f}', ha='center', va='bottom', fontsize=10)
    
    # Menambahkan label dan judul (dilakukan sekali di luar perulangan)
    
    ax3.set_title('Curah Hujan per Stasiun (mm)', fontsize=14)
    ax3.set_ylabel('Curah Hujan (mm)', fontsize=12)
    ax3.set_xlabel('Stasiun', fontsize=12)
    ax3.set_xticks(range(len(stations)))
    ax3.set_xticklabels(stations, rotation=45, ha='right')
    
    # Mengatur layout
    plt.tight_layout()
    st.pyplot(fig3)

    ## Pertanyaan 4: Pada stasiun mana suhu mencapai derajat terendah dan tertingginya?
    st.header("Pertanyaan 4: Stasiun dengan Suhu Terendah dan Tertinggi")
    # Menghitung nilai maksimum dan minimum per stasiun
    Temparatur = all_df.groupby(by="station").agg({
        "TEMP": ["max", "min"],
        })
    
    # Data yang diperlukan
    stations_Temp = Temparatur.index
    max_temp_levels = Temparatur['TEMP']['max']
    min_temp_levels = Temparatur['TEMP']['min']
    
    # Membuat figure dan axis untuk bar chart
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    
    # Membuat plot batang untuk suhu maksimum dan minimum
    bars_max = ax4.bar(stations_Temp, max_temp_levels, color='skyblue', label='Max Temp')
    bars_min = ax4.bar(stations_Temp, min_temp_levels, color='red', label='Min Temp')
    
    # Menambahkan teks di atas masing-masing bar
    for bar in bars_max:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width() / 2, height,
            f'{height:.2f}', ha='center', va='bottom', fontsize=10, color='red')
    
    for bar in bars_min:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width() / 2, height,
            f'{height:.2f}', ha='center', va='bottom', fontsize=10, color='blue')
    
    # Menambahkan label dan judul (hanya dieksekusi sekali di luar loop)
    ax4.set_xlabel('Station Name')
    ax4.set_ylabel('Temperature Levels (°C)')
    ax4.set_title('Level Temperatur Per-Stasiun')
    ax4.set_xticks(range(len(stations_Temp)))
    ax4.set_xticklabels(stations_Temp, rotation=45, ha='right')
    ax4.legend()
    
    # Mengatur layout
    plt.tight_layout()
    st.pyplot(fig4)



    # Koordinat stasiun
    station_coords = {
        'Aotizhongxin': [39.9826, 116.3406],
        'Changping': [40.2186, 116.2339],
        'Dingling': [40.2875, 116.2375],
        'Dongsi': [39.9278, 116.4164],
        'Guanyuan': [39.9331, 116.3550],
        'Gucheng': [39.9147, 116.4039],
        'Huairou': [40.3167, 116.6333],
        'Nongzhanguan': [39.9375, 116.4806],
        'Shunyi': [40.1250, 116.6500],
        'Tiantan': [39.8864, 116.4061],
        'Wanliu': [39.9628, 116.2867],
        'Wanshouxigong': [39.8789, 116.3394],
        }
    
    pollutant_mean = all_df.groupby(by="station").agg({
    "SO2": ["mean"],
    "NO2": ["mean"],
    "CO": ["mean"],
    "O3": ["mean"]
    })
    
    pollutant_mean['kadar_polusi'] = pollutant_mean.mean(axis=1)
    
    # Hitung rata-rata lokasi untuk pusat peta
    mean_lat = sum(lat for lat, lon in station_coords.values()) / len(station_coords)
    mean_lon = sum(lon for lat, lon in station_coords.values()) / len(station_coords)
    
    # Buat peta dengan Folium
    m = folium.Map(location=[-7.9826, 112.6308], zoom_start=12)
    
    # Tambahkan marker untuk setiap stasiun
    for station, coords in station_coords.items():
        row = pollutant_mean.loc[station]
        popup_text = (
        f"Stasiun: {station}<br>"
        f"Kadar Polusi: {row['kadar_polusi'].iloc[0]:.2f}"
        )
        folium.Marker(
            location=coords,
            popup=popup_text,
            icon=folium.Icon(color='blue', icon='cloud')
            ).add_to(m)
        
    # Tambahkan TileLayer Stamen Terrain dengan atribusi
    folium.TileLayer(
        'Stamen Terrain', 
        attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
        ).add_to(m)
    
    # Tampilkan peta dengan Streamlit
    st.title("Peta Kualitas Udara")
    st_folium(m, width=500, height=300)

    # Menambahkan header untuk kesimpulan
    st.header("CONCLUSION")
    
    # Menambahkan kesimpulan dengan penjelasan yang lebih rapat
    st.markdown("""
    1. **Tingkat Polusi Tertinggi** Pada Stasiun Wanshouxigong dengan nilai rata-rata polusi sebesar 374.83
    2. **Korelasi antara Temp, WSPM, CO, SO2, NO2:**
        - Korelasi antara Temp dengan O3 sebesar 0.59
        - Korelasi antara wspm dengan O3 sebesar 0.29
        - Korelasi signifikan antara CO dengan NO2 sebesar 0.69 dan SO2 sebesar 0.53
        - Korelasi signifikan antara NO2 dengan CO sebesar 0.69 dan SO2 sebesar 0.49
        - Korelasi antara O3 dengan Temp sebesar 0.59 dan wspm 0.29
        - Korelasi antara SO2 dengan NO2 sebesar 0.49 dan CO sebesar 0.53
    3. **Tingkat Curah Hujan Tertinggi** berada pada stasiun Aotizhoungxin, Guanyuan, dan Wanliu
    4. **Suhu Tertinggi** Berada pada Stasiun Gucheng dengan suhu mencapai 41.60°C, dan **Suhu Terendah** berada pada stasiun Huairou dengan suhu -19.90°C
    """)
    
st.caption('Copyright (c) Nurul Alam -Chan 2024')
