def factorial(n):

    if n < 0:
        return "Cant take negative number factorial"
    if not isinstance(n, int):
        return "Can't take factorial of something that's not an integer"
    dictOfNumToFactorial = {}
            
    def factorialOf(n):
        if n == 1:
            return 1
        if n in list(dictOfNumToFactorial.keys()):
            return dictOfNumToFactorial[n]
        else:
            answer = n * factorialOf(n - 1) 
            dictOfNumToFactorial[n] = answer
            return answer 
    result = factorialOf(n)
    return result


