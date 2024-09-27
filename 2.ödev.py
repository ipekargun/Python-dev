import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_csv('housing.csv')


ort_banyo = df.groupby('bathrooms')['price'].mean()
plt.figure(figsize=(10,6))
plt.bar(ort_banyo.index, ort_banyo.values, color='lightblue', edgecolor='black')
plt.title("Banyolar - Ort. Fiyatlar")
plt.xlabel("Banyo Sayısı")
plt.ylabel("Ortalama Fiyat")
plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x/1e6)}M'))
plt.xticks(ort_banyo.index) 
plt.grid(True, axis='y')
plt.show()


ort_mobilya = df.groupby('furnishingstatus')['price'].mean()
plt.figure(figsize=(10,6))
plt.bar(ort_mobilya.index, ort_mobilya.values, color='lightgreen', edgecolor='black')
plt.title("Mobilyalar - Ort. Fiyatlar")
plt.xlabel("Döşenmişlik Durumu")
plt.ylabel("Ortalama Fiyat")
plt.xticks(ort_mobilya.index) 
plt.grid(True, axis='y')
plt.show()
