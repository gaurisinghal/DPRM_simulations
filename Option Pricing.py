# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 22:31:37 2021

@author: moodl
"""

#%%
""" Stock price = 250
    15% annualized volatility of log returns
    Stock pays an annualized 3% dividend. The dividend is paid continuously throughout the year 
    Annualized risk-free rate is 8% (at a continuously compounded rate)
    *We will value European put and call options
    Strike price = 260
    Expire at 1 year, 4 months
    Assume 360 days per year with 30 days per month
"""
# Binomial pricing
import math as m

def binomial_call(epoch, rf):
    price = []
    payout = []
    probability = []
    u = m.exp(0.15*m.sqrt((4/3)/epoch))
    #u = 1.1
    d = 1/u
    call_premium = 0
    for i in range(epoch, -1, -1):
        price.append(250*u**i*d**(epoch-i))
        
        prob = (m.factorial(epoch)/(m.factorial(epoch-i)*m.factorial(i)))*((m.exp(rf*(4/3)/epoch)-d)/(u-d))**i*((u-m.exp(rf*(4/3)/epoch))/(u-d))**(epoch-i)       
        probability.append(prob)
    for j in price:
        payout.append(max(j-260,0))
    
    for i in range(len(probability)):
        call_premium += payout[i]*probability[i]
        #print(call_premium)
    
    call_premium = call_premium*m.exp(-rf*4/3)

    return call_premium

print("biggest epoch call premium is:", binomial_call(1029, 0.05))
print("100 epoch call premium is:", binomial_call(100, 0.05))
print("500 epoch call premium is:", binomial_call(500, 0.05))
print("1000 epoch call premium is:", binomial_call(1000, 0.05))

#%%



