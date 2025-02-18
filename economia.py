import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Tasa de cambio Representativa del Mercado (TRM).csv', sep=';', decimal=',', skiprows=1, names=['Fecha', 'TRM'])
data['Fecha'] = pd.to_datetime(data['Fecha'], format='%Y/%m/%d')
data['Growth Rate'] = data['TRM'].pct_change() * 100
plt.figure(figsize=(14, 7))
plt.subplot(2, 1, 1)
plt.plot(data['Fecha'], data['TRM'], label='TRM', color='blue')
plt.title('Tasa Representativa del Mercado (TRM)')
plt.xlabel('Fecha')
plt.ylabel('TRM')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(data['Fecha'], data['Growth Rate'], label='Tasa de Crecimiento', color='red')
plt.title('Tasa de Crecimiento Diaria')
plt.xlabel('Fecha')
plt.ylabel('Tasa de Crecimiento (%)')
plt.legend()
plt.tight_layout()
plt.show()

def calculoDias(data):
    max_growth_day = data[data['Growth Rate'] == data['Growth Rate'].max()]
    min_growth_day = data[data['Growth Rate'] == data['Growth Rate'].min()]
    print("Mayor Crecimiento:")
    print(max_growth_day[['Fecha', 'TRM', 'Growth Rate']])
    print("\nMenor Crecimiento:")
    print(min_growth_day[['Fecha', 'TRM', 'Growth Rate']])


    print('mayor precio')
    
calculoDias(data)
