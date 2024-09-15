from combination import combination as c


# assume we shoot 3 pointers at a rate of 30%. what is the probability
def binomialDist(n,r,p):
    if r > n:
        return 0
    else:
       return (c(n,r)  * (p**r) * (1-p)**(n-r))





 






        
    
