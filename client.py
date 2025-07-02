import math
from stockdex import Ticker


def fibonacci (index) :
    if index <= 2 :
        return 1
    else:
        return (fibonacci(index-1) + fibonacci(index-2))
    
def fibLin (index):
    if index < 3:
        return 1
    currSum = 1
    prevSum = 1
    currIndex = 2
    while currIndex < index:
        currSum += prevSum
        prevSum = currSum - prevSum
        currIndex +=1
    return currSum

def fibConst (index):
    return ((1+math.sqrt(5))**index - (1-math.sqrt(5))**index) / (2**index * math.sqrt(5))
    
etf = Ticker(isin="IE00B4L5Y983", security_type="etf")

etf_general_info = etf.justetf_general_info


#print(fibLin(10))
#print(fibConst(10))