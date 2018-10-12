import sys


def recursive_prime_finder(func_num, divisor):

    if func_num == divisor:
        prime_factors.add(func_num)
        return

    if func_num % divisor == 0:
        prime_factors.add(divisor)
        recursive_prime_finder(int(func_num / divisor), 2)
    else:
        divisor += 1
        recursive_prime_finder(func_num, divisor)


type_ = sys.argv[1]
num = int(sys.argv[2])
prime_factors = set()
divisor = 2

if type_ == 'recursive':
    recursive_prime_finder(num, divisor)
elif type_ == 'iterative':
    while True:
        if num == divisor:
            prime_factors.add(num)
            break
        if num % divisor == 0:
            prime_factors.add(divisor)
            num = int(num / divisor)
        else:
            divisor += 1

print(prime_factors)