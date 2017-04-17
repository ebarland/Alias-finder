from numpy import *
from math import *

#Method that finds the alias, based on fm and fs.
def alias_finder(fm, fs):
    fN = float(0.5*fs) #Folding frequency
    k = float(fm/fN) #k used to determine ka
    ka = ka_finder(k)
    fa = ka*fN
    return fa

#Method that finds ka, based on input k.
def ka_finder(k):

    k_r = ceil(k) #rounding k up to the nearest integer, used to determine if k is odd or even
    
    if (k < 1): #k below 1, means it's on the baseline of the folding diagram and ka is equal to k
        ka = k

    elif (k_r % 2 == 0): #if the k rounded up is even it means k is an odd number, and the formula for ka is as follows
        ka = k_r - k
    
    elif (k_r % 2 != 0): #if k rounded up is odd it means k is even, and the formula for ka is as follows
        ka = 1 - (k_r - k)

    return ka

print 'The answer to a1): The alias frequency is %1f Hz' % alias_finder(100, 80)
print 'The answer to a2): The alias frequency is %1f Hz' % alias_finder(100, 60)
print 'The answer to a3): The alias frequency is %1f Hz' % alias_finder(100, 250)
