def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

def calc(n1, n2, func): #High order function while passing a function as an argument
    return func(n1, n2)


result = calc(10, 5, multiply)
print(result)
