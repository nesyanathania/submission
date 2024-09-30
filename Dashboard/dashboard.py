import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari CSV
data1 = pd.read_csv('data1_project.csv')  # Data untuk analisis pertama
data2 = pd.read_csv('data2_project.csv')  # Data untuk analisis kedua

# Fungsi untuk analisis pertama (korelasi antara jumlah foto dan rating ulasan)
def plot_correlation(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='product_photos_qty', y='review_score', data=data)
    plt.title('Korelasi antara Jumlah Foto Produk dan Rating Ulasan')
    plt.xlabel('Jumlah Foto Produk')
    plt.ylabel('Rating Ulasan')
    st.pyplot(plt)

# Fungsi untuk analisis kedua (total penjualan dan pendapatan berdasarkan kategori)
def plot_sales_revenue(data):
    st.write('### Produk Kategori Terlaris dan Berpendapatan Tertinggi')

    # Menghitung total penjualan dan total pendapatan per kategori
    category_sales = data.groupby('product_category_name').agg(
        total_terjual=('order_id', 'count'),
        total_pendapatan=('price', 'sum')
    ).reset_index()

    # Mengambil 5 kategori dengan pendapatan tertinggi
    top5_categories = category_sales.nlargest(5, 'total_pendapatan')

    # Membuat figure dan dua subplot
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Membuat bar plot untuk total pendapatan pada 5 kategori dengan pendapatan tertinggi
    sns.barplot(x='product_category_name', y='total_pendapatan', data=top5_categories, ax=ax1, color='b', label='Total Revenue')

    # Menggunakan twinx untuk membuat sumbu kedua untuk total sold
    ax2 = ax1.twinx()
    sns.lineplot(x='product_category_name', y='total_terjual', data=top5_categories, ax=ax2, color='r', marker='o', label='Total Sold')

    # Menambah label dan judul
    ax1.set_xlabel('Product Category')
    ax1.set_ylabel('Total Pendapatan', color='b')
    ax2.set_ylabel('Total Terjual', color='r')
    plt.title('Top 5 Kategori Produk berdasarkan Total Pendapatan')

    # Menambahkan legenda
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Menampilkan plot
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

# Layout dashboard
st.title('Dashboard Analisis E-Commerce')

# Tab untuk Korelasi
st.header('Analisis Korelasi antara Jumlah Foto Produk dan Rating Ulasan')
plot_correlation(data1)

# Tab untuk Penjualan dan Pendapatan
st.header('Analisis Penjualan dan Pendapatan Berdasarkan Kategori')
plot_sales_revenue(data2)