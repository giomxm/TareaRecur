
def fibonacci(n):
    print("fibonacci",n)
    if n<2:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def sumarlista(list):
    if len(list) == 0:
        return 0
    else:
        return list.pop() + sumarlista(list)


