import math
# A python function that calculates the value of a futures contract

def FuturePrice(spotPrice, benefit, cost, r, t):

    return (spotPrice - benefit + cost)*math.pow(1 + r, t);

   

spotPrice       = 100;         

benefit         = 0;            # No dividend expected

miscCharges     = 1;

t               = 30;      

r               = 0.07;

ratePerday      = r/365;

 

contractPrice   = FuturePrice(spotPrice, benefit, miscCharges, r, t);

 

print("Spot price of the equity futures contract:%3.2f"%spotPrice);

print("Expected benefits like dividend:%3.2f"%benefit);

print("Expected costs to be incurred:%3.2f"%miscCharges);

print("Time to expiry of the futures contract in days:%d"%t);

print("Interest Rate in percent:%2.2f"%(r*100));

 

print("Price of the futures contract:%3.2f"%contractPrice)