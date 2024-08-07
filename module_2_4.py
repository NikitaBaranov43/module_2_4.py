numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_primes = False
    count = 0
    for j in numbers:
        deli = i % j
        if deli == 0:
            count += 1
        elif count == 2:
            is_primes = True
            continue
        elif count == 3:
            is_primes = False
            break
        if is_primes:
            primes.append(i)
        elif i > 1:
            not_primes.append(i)
print(primes)
print(not_primes)



