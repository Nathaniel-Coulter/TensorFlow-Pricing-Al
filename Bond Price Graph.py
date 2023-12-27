%matplotlib inline

import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

import numpy as np



fig = plt.figure()

ax = plt.axes()



m = 2

T = 20

r = x

Face = 1000

cpr = 0.06



def bond_price(m,T,r,Face,cpr):

  return ((Face*cpr/m*(1-(1+r/m)**(-m*T)))/(r/m)) + Face*(1+(r/m))**(-m*T)



fig = plt.figure()

ax = plt.axes()



x = np.linspace(0.01, 0.14, 14)

ax.plot(x, bond_price(m,T,x,Face,cpr));



bond_price(m,T,x,Face,cpr), x