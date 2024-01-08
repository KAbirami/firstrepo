import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel('Olympic.xlsx')
# print(df.head())

# # gk=df.groupby('Athlete')
# # # print(gk.first())
# tuple_array=df['Year'].unique()
# print(tuple_array)
# np_array=np.array(tuple_array)
# print(np_array.sort())

# group data with multiple keys
# obj=df.groupby(['Athlete','Age'])
# for i in obj:
#     print(i)

# print(df.groupby(['Athlete']).sum())    
# grp=df.groupby('Country')
# # print(grp.first())
# print(grp.get_group('United States'))#  19 rows * 10 columns 

#aggregate functions
# grp=df.groupby('Country')
# print(grp['Gold Medals'].agg([np.sum,np.mean,np.max]))

# gk=df.groupby('Year')
# for each in gk:
#     print(each)
# print(gk.get_group('Russia'))
# # plt.plot(gk,)

# Python3 program to convert a 
# list into a tuple
# def convert(list1):
# 	return tuple(list1)
# list1=df['Year'].unique()
# print(convert(list1))
 
# sort_year = tuple(sorted(list1))  
# print('Sorted Tuple :', sort_year)  
# print(type(sorted_)) 

# Driver function
# list = [1, 2, 3, 4]
# print(convert(list1))


# list1=df['Year'].unique()
# print(list1)
# np_array=np.array(list1)
# print(np_array.sort())

#task2 bar graph in Grap_pic.py



# # task2
# #to read the data from excel to display it in the bar graph 
# india_df=df[df['Country']=='India']
# # print(india_df)

# yearly_total_medals_india=india_df.groupby('Year')['Total Medals'].sum().reset_index()
# print(yearly_total_medals_india)
# plt.figure(figsize=(10,6))
# plt.bar(yearly_total_medals_india['Year'],yearly_total_medals_india['Total Medals'])#bar graph as use the word 'bar' 
# plt.title("Fourth Graph ")
# plt.xlabel('Year')
# plt.ylabel('Total Medals')
# plt.grid(True)
# plt.show()




#Gold Medals
import seaborn as sns
india_df=df[df['Country']=='United States']
# print(india_df)

yearly_total_medals_india=india_df.groupby('Year')['Gold Medals'].sum().reset_index()
print(yearly_total_medals_india)
# ax1.bar(india_df,yearly_total_medals_india,color='orange',label='India')
# ax=sns.barplot(x='Year',y='Gold Medals',data=yearly_total_medals_india)
# ax.set(xlabel='Year',ylabel='Gold Medals')
# plt.title('Iran Total Gold medals Graph')
# plt.show()


# #united states
# states_df=df[df['Country']=='United States']
# yearly_total_medals_states=states_df.groupby('Year')['Gold Medals'].sum().reset_index()
# print(yearly_total_medals_states)



# #Italy
# italy_df=df[df['Country']=='Italy']
# yearly_total_medals_italy=italy_df.groupby('Year')['Gold Medals'].sum().reset_index()
# print(yearly_total_medals_italy)

# #Russia
# russia_df=df[df['Country']=='Russia']
# yearly_total_medals_russia=russia_df.groupby('Year')['Gold Medals'].sum().reset_index()
# print(yearly_total_medals_russia)


# #Japan
# japan_df=df[df['Country']=='Japan']
# yearly_total_medals_japan=japan_df.groupby('Year')['Gold Medals'].sum().reset_index()
# print(yearly_total_medals_japan)

# china_df=df[df['Country']=='China']
# yearly_total_medals_china=china_df.groupby('Year')['Gold Medals'].sum().reset_index()
# print(yearly_total_medals_china)



# fig,((ax1,ax2),(ax3,ax4),(ax5,ax6))= plt.subplots(3,2) 
# ax2.bar(yearly_total_medals_russia['Year'],yearly_total_medals_russia['Gold Medals'],color='SkyBlue')#bar graph as use the word 'bar' 
# ax2.set_title('Russia')
# ax1.bar(yearly_total_medals_india['Year'],yearly_total_medals_india['Gold Medals'],color='Orange')
# ax1.set_title('India')
# ax3.bar(yearly_total_medals_states['Year'],yearly_total_medals_states['Gold Medals'],color='Grey')
# ax3.set_title('United States')
# ax4.bar(yearly_total_medals_italy['Year'],yearly_total_medals_italy['Gold Medals'],color='pink')
# ax4.set_title('Italy')
# ax5.bar(yearly_total_medals_japan['Year'],yearly_total_medals_japan['Gold Medals'],color='black')
# ax5.set_title('Japan')
# ax6.bar(yearly_total_medals_china['Year'],yearly_total_medals_china['Gold Medals'],color='cyan')
# ax6.set_title('China')
# plt.title("Fourth Graph ")
# plt.xlabel('Year')
# plt.ylabel('Total Medals')
# plt.grid(True)
# plt.show()



