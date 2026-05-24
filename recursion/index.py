
# This is the iterative approch for the factorial

fact = 1
# n=3
# for i in range(1,n+1):
#     fact = fact * i

# print(fact)


# def factorial(num):
#     if num == 1 :
#         return 1
#     elif num == 0:
#         return 1
#     return num * factorial(num-1)

# print(factorial(6))

def fib(n):
    if n == 1:
        return 1
    elif n ==2 :
        return 1
    
    return fib(n-1)+fib(n-2)
    
print(fib(7))