import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('housing.csv')
df.head()

fiyatlar=df["price"]
bölge=df["area"]
yatak_odaları=df["bedrooms"]
hikayeler=df["stories"]


bin_sayisi = 7
df['area_bins'] = pd.cut(df['area'], bins=bin_sayisi)
plt.figure(figsize=(10, 6), dpi=100)
for bin_adi, grup in df.groupby('area_bins'):
    plt.hist(grup['price'], bins=15, alpha=0.5, label=str(bin_adi), edgecolor="black")


plt.title("Bölge - Fiyatlar Histogram")
plt.xlabel("Bölge")
plt.ylabel("Fiyatlar")
plt.legend(title="Alan Aralığı")
plt.show()


bin_sayisi = 5
df['bedrooms_bins']=pd.cut(df['bedrooms'],bins=bin_sayisi)
plt.figure(figsize=(10,6), dpi=100)
for bin_adi, grup in df.groupby('bedrooms_bins'):
    plt.hist(grup['price'], bins=10, alpha=0.5, label=str(bin_adi), edgecolor="black")
plt.title("Yatak Odaları - Fiyatlar Histogram")
plt.xlabel("Yatak Odaları")
plt.ylabel("Fiyatlar")
plt.legend(title="Yatak Odaları Aralıkları")
plt.show()

bin_sayisi = 4
df['stories_bins']=pd.cut(df['stories'],bins=bin_sayisi)
plt.figure(figsize=(10,6), dpi=100)
for bin_adi, grup in df.groupby('stories_bins'):
    plt.hist(grup['price'], bins=10, alpha=0.5, label=str(bin_adi), edgecolor="black")
plt.title("Hikayeler - Fiyatlar Histogram")
plt.xlabel("Hikayeler")
plt.ylabel("Fiyatlar")
plt.legend(title="Hikayeler Aralıkları")
plt.show()