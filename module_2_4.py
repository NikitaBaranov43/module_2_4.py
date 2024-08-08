numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
prime = 0

for i in numbers:
    if i == 1:
        continue
    for j in numbers:
        if i % j == 0:
            prime += 1
    if prime == 2:
        primes.append(i)
    else:
        not_primes.append(i)
    prime = 0
print(primes)
print(not_primes)



