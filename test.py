import math

def fibo(index = 1):
    return ((1+math.sqrt(5))**index - (1-math.sqrt(5))**index) / (2**index * math.sqrt(5)) 

if __name__ == "__main__" :
    print(int(fibo(10)))
