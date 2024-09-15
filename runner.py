from binomialcalculator import binomialDist
from permutation import permutation
from combination import combination
from geometriccalculator import geometric



pval = float(input("enter a probability of success between 0 and 1"))
x = int(input("enter a number of trials"))

res = geometric(pval, x)
print(res, "this is the probability of wainting ", x, "times for the 1st success")

