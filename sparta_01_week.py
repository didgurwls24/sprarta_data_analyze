import pandas as pd
import matplotlib.pyplot as plt

chicken07 = pd.read_csv('C:/Users/user/Desktop/sparta_data/sparta_data/sparta_data/week01/data/chicken_07.csv')
chicken08 = pd.read_csv('C:/Users/user/Desktop/sparta_data/sparta_data/sparta_data/week01/data/chicken_08.csv')
chicken09 = pd.read_csv('C:/Users/user/Desktop/sparta_data/sparta_data/sparta_data/week01/data/chicken_09.csv')

chicken = pd.concat([chicken07,chicken08,chicken09])
chicken = chicken.reset_index(drop = True)


sum_of_calls_by_week = chicken.groupby('요일')['통화건수'].sum()
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(8,5))
plt.bar(sum_of_calls_by_week.index,sum_of_calls_by_week)
plt.title('요일에 따른 치킨 주문량 합계')
plt.show()

# weeks = ['월','화','수','목','금','토','일']
# chicken_final_test = chicken.groupby('요일')['통화건수'].sum().reindex(weeks)

sum_of_calls_by_week_age = chicken.groupby('연령대')['통화건수'].sum()
plt.figure(figsize=(8,5))
plt.bar(sum_of_calls_by_week_age.index,sum_of_calls_by_week_age)
plt.xlabel('연령대')
plt.title('연령에 따른 치킨 주문량 합계')
plt.show()


sum_of_calls_by_week_city = chicken.groupby('시군구')['통화건수'].sum()
sum_of_calls_by_week_city

sorted_sum_of_calls_by_week_city = sum_of_calls_by_week_city.sort_values(ascending=False)


plt.figure(figsize=(20,15))
plt.bar(sorted_sum_of_calls_by_week_city.index,sorted_sum_of_calls_by_week_city)
plt.xlabel('지역')
plt.title('시군구에 따른 치킨 주문량 합계')
plt.xticks(rotation = 45)
plt.show()