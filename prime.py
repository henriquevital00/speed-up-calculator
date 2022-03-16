import sympy
import concurrent.futures
import psutil

def check_prime(data):
    prime = 0
    for i in range(len(data)):
        if sympy.isprime(data[i]):
            prime += 1
    return prime


def coef(n, c):
    c[0] = 1
    for i in range(n):
        c[1 + i] = 1
        for j in range(i, 0, -1):
            c[j] = c[j - 1] - c[j]
        c[0] = -c[0]

# function to check whether
# the number is prime or not
def isPrime_aks(n):
    c = [0] * 250000
    coef(n, c)

    c[0] = c[0] + 1
    c[n] = c[n] - 1

    i = n
    while (i > -1 and c[i] % n == 0):
        i = i - 1

    return True if i < 0 else False



def is_prime(data, func=sympy.isprime):
    tamanholista = len(data)
    primos = 0
    for i in range(tamanholista):
        if func(data[i]):
            primos += 1
    return primos

def is_prime_thread(data, number_of_threads):
    ThreadsQtdd = number_of_threads
    tamanholista = len(data)
    index = range(0, tamanholista+(tamanholista//ThreadsQtdd), tamanholista//ThreadsQtdd)
    primos = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(ThreadsQtdd):
            futures.append(executor.submit(check_prime, data=data[index[i]:index[i+1]]))
        for future in concurrent.futures.as_completed(futures):
            primos += future.result()
    return primos