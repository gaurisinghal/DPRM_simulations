import math as m
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_call(iterations, stock = 250, strike = 260, rf= 0.08, q = 0.03, T= 4/3, vol= 0.15):
    stock_price = []
    call_payout = []
    mean = (rf-q-(0.5*m.pow(vol,2)))*T #of the normal distribution
    stdv = vol*m.sqrt(T)

    for i in range(iterations):
        stock_price.append(stock*m.exp(np.random.normal(mean, stdv))) #drawing random variable from normal dostribution
        call_payout.append(max(0,stock_price[i]-strike)) 
        #print(call_payout[i])
    
    expected_call = sum(call_payout)/iterations
    discounted_call = expected_call*m.exp(-rf*T)

    #storing expected call payouts to create histogram
    '''
    with open("expected_call_100000.txt", "a") as filehandle:
        filehandle.write(str(expected_call)+"\n")
    '''

    return discounted_call

def monte_carlo_put(iterations, stock = 250, strike = 260, rf= 0.08, q = 0.03, T= 4/3, vol= 0.15):
    stock_price = []
    put_payout = []
    mean = (rf-q-(0.5*m.pow(vol,2)))*T #of the normal distribution
    stdv = vol*m.sqrt(T)

    for i in range(iterations):
        stock_price.append(stock*m.exp(np.random.normal(mean, stdv))) #drawing random variable from normal dostribution
        put_payout.append(max(0, strike - stock_price[i])) 
    
    expected_put = sum(put_payout)/iterations
    discounted_put = expected_put*m.exp(-rf*T) #discounting back to the present

    #storing expected put payouts to create histogram
    '''
    with open("Monte Carlo Data/expected_put_10000.txt", "a") as filehandle:
        filehandle.write(str(expected_put)+"\n")
    '''


    return discounted_put

print("call price for 1000 iterations is: "+ str(round(monte_carlo_put(1000),2)))
print("call price for 10,000 iterations is: "+ str(round(monte_carlo_call(10000),2)))
print("call price for 100,000 iterations is: "+ str(round(monte_carlo_call(100000),2)))
print("\n")
print("put price for 1,000 iterations is: "+ str(round(monte_carlo_put(1000),2)))
print("put price for 10,000 iterations is: "+ str(round(monte_carlo_put(10000),2)))
print("put price for 100,000 iterations is: "+ str(round(monte_carlo_put(100000),2)))




