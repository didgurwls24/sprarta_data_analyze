import pandas as pd
import matplotlib.pyplot as plt
import folium
import json
plt.rcParams['font.family'] = 'Malgun Gothic'

commercial = pd.read_csv('C:/Users/user/Desktop/sparta_data/sparta_data/sparta_data/week02/data/commercial.csv')

cat_range = set(commercial['상권업종소분류명'])

commercial[['시','구','상세주소']] = commercial['도로명'].str.split(' ',n = 2,expand=True)
0
seoul_commercial = commercial[commercial['시']=='서울특별시']
seoul_commercial = seoul_commercial.reset_index(drop = True)

seoul_chicken_commercial = seoul_commercial[seoul_commercial['상권업종소분류명']=='후라이드/양념치킨']

group = seoul_chicken_commercial.groupby('구')
groupby_cat = group['상권업종소분류명']
chicken_count_loc = groupby_cat.count()
sorted_chicken_loc = chicken_count_loc.sort_values(ascending = False)

plt.figure(figsize=(15,10))
plt.bar(sorted_chicken_loc.index,sorted_chicken_loc)
plt.title('구에 따른 치킨가게 수의 합계')
plt.xticks(rotation = 90)
plt.show()


seoul_state_geo = 'C:/Users/user/Desktop/sparta_data/sparta_data/sparta_data/week02/data/seoul_geo.json'
geo_data = json.load(open(seoul_state_geo,encoding = 'utf-8'))
map = folium.Map(location=[37.5502,126.982],zoom_start = 11)
folium.Choropleth(geo_data = geo_data,data=chicken_count_loc,columns = [chicken_count_loc.index,chicken_count_loc],fill_color='PuRd',key_on = 'properties.name').add_to(map)

#map.save('result.html')


population = pd.read_csv('C:/Users/user/Desktop/sparta_data/sparta_data/sparta_data/week02/data/population07.csv')
pop_loc = population.groupby('군구')['유동인구수'].sum()
pop_loc = pop_loc.sort_values(ascending = True)

plt.figure(figsize=(15,10))
plt.bar(pop_loc.index,pop_loc)
plt.title('7월 구에 따른 유동인구 수의 합계')
plt.xlabel('군구')
plt.ylabel('유동인구 수(명)')
plt.xticks(rotation = -45)
plt.show()

pop_kangnam = population[population['군구']=='강남구'].reset_index(drop=True)
pop_kangnam_daily = pop_kangnam.groupby('일자')['유동인구수'].sum()

plt.figure(figsize=(15, 10))
date = []
for day in pop_kangnam_daily.index:  # 날짜 담아주기(그냥 하면 그냥 인덱스 값으로 들어가서 날짜가 아닌것 처럼 보인다)
    date.append(str(day))

plt.plot(date, pop_kangnam_daily)
plt.title('7월 강남구의 날짜별 유동인구 수')
plt.xlabel('날짜')
plt.ylabel('유동인구 수(명)')
plt.xticks(rotation=-45)
plt.show()

map_2 = folium.Map(location=[37.5502,126.982],zoom_start = 11,tiles='stamentoner')

geo_data_2 = json.load(open(seoul_state_geo,encoding = 'utf-8'))
folium.Choropleth(geo_data=geo_data_2,data=pop_loc,columns=[pop_loc.index,pop_loc],fil_color='PuRd',key_on='properties.name').add_to(map_2)
map_2.save('result_2.html')

#새로운 데이터 프레임 생성(데이터 합쳐서 분석)
new_chicken_count_gu = pd.DataFrame(chicken_count_loc).reset_index()
new_pop_loc = pd.DataFrame(pop_loc).reset_index()
gu_chicken =new_chicken_count_gu.join(new_pop_loc.set_index('군구'),on = '구')
#치킨집 당 유동인구수 구하기
gu_chicken['유동인구 수/치킨집수']=gu_chicken['유동인구수']/gu_chicken['상권업종소분류명']

gu_chicken = gu_chicken.sort_values(by='유동인구 수/치킨집수')

plt.figure(figsize=(10,5))
plt.bar(gu_chicken['구'],gu_chicken['유동인구 수/치킨집수'])
plt.xlabel('구')
plt.ylabel('유동인구 수/치킨집수')
plt.xticks(rotation=90)
plt.title('치킨집 당 유동인구 수')
plt.show()