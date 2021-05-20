# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:40:49 2019

@author: jereme pineda
Price and profit estimation
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

param_1 = st.sidebar.number_input("Annualized Technology cost:",10000)
param_2 = st.sidebar.number_input("Annualized R&D Personnel costs:",10000)
param_3 = st.sidebar.number_input("Connectivity fee:",2)


  
list_1 = [5,10,15,20,25]
list_2 = [50,70,100,150,200,250,300,500,1000,2000,2500]
list_3 = [5,10,20,50,100]

list_4 = [20,30,40,50,60,70,80,90,100]
list_5 = [50,60,70,80,90,100,120]
list_6 = [4,9,14,19,24]
list_7 = [1,2,3,5,10,15]


param_4 = st.sidebar.slider('Starting Min and Max Customers',5, 150, (5, 50))
param_7 = st.sidebar.slider('Select price per report',0,150,(20,100))
param_9 = st.sidebar.selectbox('Number of price points to create', list_6)

param_10 = st.sidebar.selectbox('Number of reports per customer',list_7)


cost = param_1 + param_2
connectivity_fee = param_3

number_of_customers_start = min(param_4)
number_of_customers_stop = max(param_4)
number_of_customers_step = 5


X = np.linspace(number_of_customers_start, number_of_customers_stop, number_of_customers_step) # number of customers
Y = param_10

initial_price = min(param_7)
maximum_price = max(param_7)
number_of_pricepoints = param_9


price = np.linspace(initial_price, maximum_price, number_of_pricepoints) # price options

pr = np.zeros((len(price), len(X))) # profit
index = 0
for i in price:
    
    
    pr[index, :] = (i * Y * X * 12) - cost + (connectivity_fee * X * 12) 
    # cost = cost + cost * 0.10 ##percent cost increase per price point
    print(i)
    index += 1


st.write("Yearly Profitability calculation of a per Report subscription pricing")


plt.figure()

plt.xlabel('Number of customers')
# plt.ylabel("Profit (logarithmic scale)")
plt.ylabel("Profit")

for i in range(len(pr)):
    #print(i)
    # plt.plot(X, np.log(pr[i, : ]),  linewidth = 1)
    plt.plot(X, (pr[i, : ]), linewidth = 1)

# plt.figure(figsize=(180,760))
plt.legend(price)
plt.grid()
# plt.savefig('profit_log_scale.png')
plt.show()

st.pyplot()

st.write("Profit is calculated as: " 
+ "(Price per Report x Reports per Customer x Number of Customer x 12) + (Connectivity fee x Number of Customers x 12) - (Annualized Tech Cost + Annualised R&D Cost) "

)


# st.write("""We assume there are __2__ reports per customer and up to __70__ customers in total. 
# The connectivity is pegged at __50__ customers.""")

st.write("We assume there are "+str(Y)+ " reports per customer and up to "+str(number_of_customers_stop )+
" customers in total. The connectivity is pegged at "+str(connectivity_fee)+" per customers.")
