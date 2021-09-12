def soma_h(n):
    divisor = 1
    h = 1
    while divisor < n:
        divisor += 1
        print(divisor)
        h += 1/divisor
        
    return round(h,2)

print(soma_h(2))