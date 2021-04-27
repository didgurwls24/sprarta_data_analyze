import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

#Q1.4월의 유동인구 분석
pop_04 = pd.read_csv('C:/Users/user/Desktop/sparta_data/sparta_data/sparta_data/week02/data/population04.csv')

pop_04_loc = pop_04.groupby('군구')['유동인구수'].sum()

pop_04_loc = pop_04_loc.sort_values(ascending = False)

plt.figure(figsize=(15,10))
plt.bar(pop_04_loc.index,pop_04_loc)
plt.title('4월 구에 따른 유동인구 수의 합계')
plt.xlabel('군구')
plt.ylabel('유동인구 수(명)')
plt.xticks(rotation = -45)
plt.show()

#Q2. 4월과 7월의 강남구의 일별 유동인구 수 구하기

pop_04_kangnam = pop_04[pop_04['군구']=='강남구'].reset_index(drop=True)
pop_04_daily = pop_04_kangnam.groupby('일자')['유동인구수'].sum()

pop_07 = pd.read_csv('C:/Users/user/Desktop/sparta_data/sparta_data/sparta_data/week02/data/population07.csv')
pop_07_kangnam = pop_07[pop_07['군구']=='강남구'].reset_index(drop=True)
pop_07_daily = pop_07_kangnam.groupby('일자')['유동인구수'].sum()

new_04 = pd.DataFrame(pop_04_daily).reset_index()
new_07 = pd.DataFrame(pop_07_daily).reset_index()

result = pd.concat([new_04,new_07]).reset_index()

plt.figure(figsize=(30, 20))
date = []
for day in result['일자']:  # 날짜 담아주기(그냥 하면 그냥 인덱스 값으로 들어가서 날짜가 아닌것 처럼 보인다)
    date.append(str(day))

plt.plot(date, result['유동인구수'])
plt.xlabel('일자')
plt.ylabel('유동인구수')
plt.xticks(rotation=45)
plt.title('강남구 4월,7월 유동인구수')
plt.show()