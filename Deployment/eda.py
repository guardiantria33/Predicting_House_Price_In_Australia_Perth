import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


def run():
    # Membuat Tittle
    st.title('House Pricing In Perth Australia')

    # Membuat Sub Headher
    st.subheader('EDA untuk analisa Dataset House Pricing In Perth')

    # Menambahkan gambar
    image = Image.open('House_Perth.jpg')
    st.image(image, caption='House in Perth')

    # Membuat Garis lurus
    st.markdown('---')

    # DataFrame
    data = pd.read_csv('all_perth_310121.csv')

    # Membuat histogram berdasarkan user
    st.write('#### Histogram berdasarkan Input User')
    pilihan = st.radio('Pilih column : ', ('PRICE', 'CBD_DIST', 'NEAREST_STN_DIST','NEAREST_SCH_DIST'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[pilihan], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Linechart Harga Rumah Berdasarkan Tahun
    st.write('#### LineChart Harga Rumah berdasarkan Tahun Pembangunan Rumah')
    fig = plt.figure(figsize=(20,6))
    sns.lineplot(x=data['BUILD_YEAR'], y=data['PRICE'])
    st.pyplot(fig)
    st.write('Terlihat pada line plot diatas bahwa harga rumah pada kawasan perth australia memiliki harga yang fluktuatif. Berdasarkan tahun pembuatan, harga rumah tertinggi dipegang oleh rumah yang di bangun pada tahun 1900an dan 1940an.')
    st.markdown('---')

    # Membuat Pie Chart Bedasarkan Bedrooms
    # Menghitung jumlah kamar
    df3 = data['BEDROOMS'].value_counts().reset_index()
    df3.columns = ['BEDROOMS', 'Value']
    # Mengatur sequence warna
    colors = px.colors.qualitative.Set3
    # Membuat pie chart dengan pengaturan visual yang diperindah
    st.write('#### Persentase Jumlah Kamar Pada Rumah')
    fig3 = px.pie(df3, 
                values='Value', 
                names='BEDROOMS', 
                color_discrete_sequence=colors,
                title='Jumlah Kamar')

    # Menambahkan layout yang lebih rapi
    fig3.update_traces(textposition='inside', textinfo='percent+label')
    fig3.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(title='BEDROOMS'),
        title_font=dict(size=20),
        title_x=0.5
    )
    st.plotly_chart(fig3)
    st.write('Dapat dilihat dari pie chart diatas, bahwa kebanyakan rumah pada kawasan perth memiliki jumlah kamar sebanyak 4 kamar dengan presentase 52.4%.Diikuti dengan jumlah kamar sebanyak 3 kamar sebanyak 34.5%')
    st.write('Hal ini mengindikasi bahwa kawasan pada rumah perth di isi dengan 3 - 4 orang yang bisa dibilang cocok bagi orang-orang yang baru membina rumah tangga yang terdiri dari ayah ibu dan anak.Selain itu hal ini juga mengindikasi bahwa perumahan pada kawasan perth diperuntukan bagi orang-orang yang ingin memiliki rumah yang tidak mau memiliki banyak kamar di dalam rumahnya.')
    st.markdown('---')

    # Menghitung jumlah kamar mandi
    df4 = data['BATHROOMS'].value_counts().reset_index()
    df4.columns = ['BATHROOMS', 'Value']

    # Mengatur sequence warna
    colors = px.colors.qualitative.Set3

    # Membuat pie chart dengan pengaturan visual yang diperindah
    fig4 = px.pie(df4, 
                values='Value', 
                names='BATHROOMS', 
                color_discrete_sequence=colors,
                title='Jumlah Kamar Mandi')

    # Menambahkan layout yang lebih rapi
    fig4.update_traces(textposition='inside', textinfo='percent+label')
    fig4.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(title='BATHROOMS'),
        title_font=dict(size=20),
        title_x=0.5
    )
    # Menampilkan pie chart
    st.plotly_chart(fig4)
    st.write('Dapat dilihat dari pie chart diatas, bahwa kebanyakan rumah pada kawasan perth memiliki jumlah kamar mandi sebanyak 2 kamar mandi dengan presentase 66.2%. Diikuti dengan jumlah kamar sebanyak 1 kamar sebanyak 26.3%')
    st.write('Hal ini bisa dikatakan normal, dikarenakan memang tidak hanya di perth australia, bahkan di indonesia pun kebanyakan rumah hanya memiliki kamar mandi dengan jumlah 1-2 kamar mandi.')
    st.markdown('---')

    # Melihat top 5 harga rumah bersarakan suburb
    top5_city_price = (data
                .groupby(['SUBURB'])
                .agg(mean_price=('PRICE','mean'))
                .reset_index()
                .sort_values('mean_price',ascending=False)
                .head(5)
                )
    fig = plt.figure(figsize=(8,6))
    top5_city_price['SUBURB'] = top5_city_price['SUBURB'].astype(str)
    sns.barplot(data=top5_city_price, x='SUBURB', y='mean_price')
    st.pyplot(fig)
    st.write('Terlihat pada barchart diatas, bahwa kawasan pada perth yang memiliki rata-rata harga rumah termahal terdapat pada :')
    st.write('Daiketh dengan rata-rata harga rumah sebesar 1,951,092 AUD')
    st.write('Peppermint Grove dengan rata-rata harga rumah sebsar 1.793.549 AUD')
    st.write('City Beach dengan rata-rata harga rumah sebesar	1,654,765 AUD')
    st.write('Nedlands dengan rata-rata harga rumah sebesar	1,647,442 AUD')
    st.write('Cottesloe dengan rata-rata harga rumah sebesar	1,646,283 AUD')
    st.markdown('---')


    # Melihat top data mean nearest sch dist berdasarkan harga dan suburb
    nearest_sch_price = (data
                .groupby(['SUBURB'])
                .agg(mean_price=('PRICE','mean'), mean_nearest_sch_dist=('NEAREST_SCH_DIST','mean'))
                .reset_index()
                .sort_values('mean_nearest_sch_dist',ascending=True))
    # Membuat scatter plot
    fig = plt.figure(figsize=(8,6))
    plt.scatter(x='mean_nearest_sch_dist', y='mean_price', data=nearest_sch_price, alpha=0.5)

    # Menambahkan label sumbu dan judul
    plt.xlabel('NEAREST_SCH_DIST')
    plt.ylabel('Harga Rumah')
    plt.title('Hubungan Price Dengan NEAREST_SCH_DIST')

    # Menampilkan plot
    st.pyplot(fig)
    st.write('Terlihat pada scatterplot diatas, bahwa jarak sekolah terdekat tidak selalu berpengaruh terhadap harga rumah. Dimana jika kita lihat pada tabel diatas, terdapat rumah-rumah yang memiliki harga yang bisa dibilang tinggi walaupun dekat dengan jarak sekolah. Hal ini memang bisa terjadi dikarenakan terdapat faktor-faktor lain yang bisa mempengaruhi harga rumah mulai dari luas lantai, jumlah kamar, jumlah kamar mandi, garasi, dll')

    # Melihat nearest stn dist berdasarkan harga dan suburb
    nearest_stn_price = (data
                .groupby(['SUBURB'])
                .agg(mean_price=('PRICE','mean'), mean_nearest_stn_dist=('NEAREST_STN_DIST','mean'))
                .reset_index()
                .sort_values('mean_nearest_stn_dist',ascending=True))
    # Membuat scatter plot
    fig = plt.figure(figsize=(8,6))
    plt.scatter(x='mean_nearest_stn_dist', y='mean_price', data=nearest_stn_price, alpha=0.5)

    # Menambahkan label sumbu dan judul
    plt.xlabel('Harga Rumah')
    plt.ylabel('NEAREST_STN_DIST')
    plt.title('Hubungan Price Dengan NEAREST_STN_DIST')

    # Menampilkan plot
    st.pyplot(fig)
    st.write('Terlihat pada scatterplot diatas, bahwa jarak stasiun terdekat tidak selalu berpengaruh terhadap harga rumah sama seperti dengan jarak sekolah. Dimana jika kita lihat pada tabel diatas, terdapat rumah-rumah yang memiliki harga yang bisa dibilang tinggi walaupun dekat dengan jarak statsiun. Hal ini memang bisa terjadi dikarenakan faktor dari stasiun itu sendiri, stasiun yang memiliki jurusan yang banyak atau sedikit atau stasiun yang biasanya dikujungi orang-orang atau tidak. Selain itu terdapat faktor-faktor lain yang bisa mempengaruhi harga rumah mulai dari luas lantai, jumlah kamar, jumlah kamar mandi, garasi, dll.')

    # Melihat rata-rata cbd dist berdasarkan harga dan sub urb
    cbd_dist_price = (data
                .groupby(['SUBURB'])
                .agg(mean_price=('PRICE','mean'), mean_cbd_dist=('CBD_DIST','mean'))
                .reset_index()
                .sort_values('mean_cbd_dist',ascending=True))
    # Membuat scatter plot
    fig = plt.figure(figsize=(8,6))
    plt.scatter(x='mean_cbd_dist', y='mean_price', data=cbd_dist_price, alpha=0.5)

    # Menambahkan label sumbu dan judul
    plt.xlabel('CBD_DIST')
    plt.ylabel('Harga Rumah')
    plt.title('Hubungan Price Dengan CBD_DIST')

    # Menampilkan plot
    st.pyplot(fig)
    st.write('Terlihat pada scatterplot diatas, bahwa jarak Kawasan Pusat Bisnis bisa dikatakan memiliki pengaruh, dimana semakin dekat rumah dengan kawasan bisnis maka harga rumah tersebut semakin tinggi. Selain itu, terdapat juga harga rumah yang tinggi walaupun jarak ke kawasan pusat bisnis tidak terlalu dekat. Hal ini bisa terjadi dikarenakan terdapat faktor-faktor lain yang mempengaruhi harga rumah tersebut. Seperti kawasannya, luas lantai rumah, jumlah kamar, jumlah kamar mandi, dan lain-lain.')




if __name__=='__main__':
    run()