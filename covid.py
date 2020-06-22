# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:51:17 2020

@author: Harshal
"""


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
date_wise = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise_daily.csv')
state_data = data[['State',"Confirmed",'Recovered',"Deaths",'Active','Last_Updated_Time']]
#state_data = state_data[state_data['State']!='Total']


confirmed = date_wise[date_wise['Status']=='Confirmed'] 
recovered = date_wise[date_wise['Status']=='Recovered']
dead = date_wise[date_wise['Status']=='Deceased']


def covid_status(name):
    name1 = state_dict.get(name)

    x = state_data[state_data['State'] == name1 ]
    print("\nHERE IS THE STATUS OF THE QUERY:")
    print()
    print("STATE NAME:  " + state_dict.get(name))
    print("CONFIRMED : " , int(x["Confirmed"]))
    print("ACTIVE    : " , int(x["Active"]))
    print("RECOVERED : " , int(x["Recovered"]))
    print("DECEASED  : " , int(x["Deaths"]))
    
    x='TT'
    plt.plot(confirmed.Date,confirmed[name],'b-',label='Confirmed')
    plt.plot(recovered.Date,recovered[name],'g-',label='Recovered')
    plt.plot(dead.Date,dead[name],'r-',label='Deceased')
    plt.xticks(dead.Date[::30])
    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.title(name1 + " COVID STATUS TILL DATE(per day)",fontdict={'fontweight':'bold','fontsize':14})
    
    


state_list = ['Total','Andhra Pradesh',"Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala",'Ladakh',"Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli and Daman and Diu","Laakshadweep","Delhi","Puducherry" ]
state_dict = {'TT':'Total','AP':'Andhra Pradesh','AN':'Arunachal Pradesh','AS':'Assam','BR':'Bihar','CT':'Chhattisgarh','GA':'Goa','GJ':'Gujarat','HR':'Haryana','HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand','KA':'Karnataka','KL':'Kerala','LA':'Ladakh','MP':'Madhya Pradesh','MH':'Maharashtra','MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','NL':'Nagaland','OR':'Odisha','PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim','TN':'Tamil Nadu','TG':'Telangana','TR':'Tripura','UP':'Uttar Pradesh','UT':'Uttarakhand','WT':'West Bengal','AR':'Andaman and Nicobar Islands','CH':'Chandigarh','DN':'Dadra and Nagar Haveli and Daman and Diu','LD':'Lakshadweep','DL':'Delhi','PY':'Puducherry'}
state_code = ['TT','AP','AN','AS','BR','CT','GA','GJ','HR','HP','JK','JH','KA','KL','LA','MP','MH','MN','ML','MZ','NL','OR','PB','RJ','SK','TN','TG','TR','UP','UT','WT','AR','CH','DN','LD','DL','PY']

for i in range (len(state_list)):
    print(state_list[i] + "("+ state_code[i]+ ")")
print()
state = str(input('Please Enter the code of the state: '))
covid_status(state)



