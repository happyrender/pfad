import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('daily_KP_EVAP_2024.csv', skiprows=2)

data = data.dropna()

data = data.rename(columns={'年/Year': 'Year', '月/Month': 'Month', '日/Day': 'Day'})

data['日期'] = pd.to_datetime(data[['Year', 'Month', 'Day']])

dates = data['日期']
values = data['數值/Value']

plt.figure(figsize=(10, 5))
plt.plot(dates, values, marker='o', linestyle='-')
plt.title('Daily Total Evaporation (mm) at King\'s Park, January 2024')
plt.xlabel('Date')
plt.ylabel('Evaporation (mm)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()