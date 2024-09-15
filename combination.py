from factorial import factorial


def combination(n,r):
    if n < r:
        return 0
    
    else:
        return factorial(n) / (factorial(n-r) * factorial(r)) 
        







