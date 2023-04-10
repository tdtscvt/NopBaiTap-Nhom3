
def isPrime(a: int)-> bool:
    if a < 2:
        return False
    if a == 2:
        return True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

def PrimeNumbers(n):
    prime_numbers= []
    for i in range (2,n+1):
        if isPrime(i) :
            prime_numbers.append(i)
    return prime_numbers
