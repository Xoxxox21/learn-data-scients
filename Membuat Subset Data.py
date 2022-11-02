import datetime
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

# visualisasi dalam bentuk pie chart
dataset_dki_q4 = dataset[(dataset['province']=='DKI Jakarta') & (dataset['order_month']>='2019-10')]
gmv_per_city_dki_q4 = dataset_dki_q4.groupby('city')['gmv'].sum().reset_index()
plt.figure(figsize=(6,6))
plt.pie(gmv_per_city_dki_q4['gmv'], labels= gmv_per_city_dki_q4['city'],autopct='%1.2f%%')  # type: ignore
plt.title('GMV Contribution Per City - DKI Jakarta in Q4 2019', loc='center',pad=30, fontsize=15, color='blue')
plt.show()

# visualisasi dalam bentuk bar chart
dataset_dki_q4.groupby('city')['gmv'].sum().sort_values(ascending=False).plot(kind='bar', color='green')
plt.title('GMV Per City - DKI Jakarta in Q4 2019',loc='center',pad=30,fontsize=15,color='blue')
plt.xlabel('city', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))  # type: ignore
plt.xticks(rotation=0)
plt.show()