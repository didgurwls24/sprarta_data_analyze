import pandas as pd
import matplotlib.pyplot as plt
pizza = pd.read_csv('C:/Users/user/Desktop/sparta_data/sparta_data/sparta_data/week01/data/pizza_09.csv')


pizza_day = pizza.groupby('요일')['통화건수'].sum()

weeks = ['월','화','수','목','금','토','일']
pizza_day = pizza.groupby('요일')['통화건수'].sum().reindex(weeks)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(8,5))
plt.bar(pizza_day.index,pizza_day)
plt.title('요일에 따른 피자 주문량 합계')
plt.show()

pizza_loc = pizza.groupby('발신지_구')['통화건수'].sum()
pizza_loc = pizza_loc.sort_values(ascending=False)
plt.figure(figsize=(8,5))
plt.bar(pizza_loc.index,pizza_loc)
plt.title('지역구에 따른 피자 주문량 합계')
plt.xticks(rotation = 45)
plt.show()