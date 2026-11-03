# def fib(n):
#     if n<=2:
#         return 1 
#     return fib(n-1)+fib(n-2) 
# n=int(input("Enter the Number: "))
# print(fib(n))
a=0
b=1 
for i in range(10):
    c=a+b
    a=b
    b=c 
    print(c, end=" ")