L = 100000 # Mortgage amount in dollars
r = 0.04 # yearly interest rate of 4%
c = r/12
n = 360 # duration of mortgage
P = L*(c*(1+c)**n/((1+c)**n-1)
print(P)
