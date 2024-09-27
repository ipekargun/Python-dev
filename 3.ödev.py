import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('housing.csv')


label_encoder = LabelEncoder()
df['mainroad_encoded'] = label_encoder.fit_transform(df['mainroad'])
df['guestroom_encoded'] = label_encoder.fit_transform(df['guestroom'])
df['basement_encoded'] = label_encoder.fit_transform(df['basement'])
df['hotwaterheating_encoded'] = label_encoder.fit_transform(df['hotwaterheating'])
df['airconditioning_encoded'] = label_encoder.fit_transform(df['airconditioning'])
df['prefarea_encoded'] = label_encoder.fit_transform(df['prefarea'])
df['furnishingstatus_encoded'] = label_encoder.fit_transform(df['furnishingstatus'])
df['furnishingstatus_encoded'] = df['furnishingstatus_encoded'].max() - df['furnishingstatus_encoded']
encoded_df = df[['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'parking',
                 'mainroad_encoded', 'guestroom_encoded', 'basement_encoded', 
                 'hotwaterheating_encoded', 'airconditioning_encoded', 'prefarea_encoded', 
                 'furnishingstatus_encoded']]
correlation_matrix = encoded_df.corr()
correlation_matrix = correlation_matrix.rename(columns={'furnishingstatus_encoded': 'mobilyalar'},
                                               index={'furnishingstatus_encoded': 'furnishingstatus'})
correlation_matrix = correlation_matrix.rename(columns={'prefarea_encoded': 'bölge tercihi'},
                                               index={'prefarea_encoded_encoded': 'prefarea'})
correlation_matrix = correlation_matrix.rename(columns={'airconditioning_encoded': 'havalandırma'},
                                               index={'airconditioning_encoded': 'airconditioning'})
correlation_matrix = correlation_matrix.rename(columns={'hotwaterheating_encoded': 'sıcak su'},
                                               index={'hotwaterheating_encoded': 'hotwaterheating'})
correlation_matrix = correlation_matrix.rename(columns={'basement_encoded': 'bodrum'},
                                               index={'basement_encoded': 'basement'})
correlation_matrix = correlation_matrix.rename(columns={'guestroom_encoded': 'misafir odası'},
                                               index={'guestroom_encoded': 'guestroom'})
correlation_matrix = correlation_matrix.rename(columns={'mainroad_encoded': 'anayol'},
                                               index={'mainroad_encoded': 'mainroad'})

plt.figure(figsize=(10,7))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Korelasyon Matrisi')
plt.tight_layout()
plt.show()
