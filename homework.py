# 1.)
# Q1: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# n=0
# for i in xrange(1,10):
# 	if not i % 3 or not i % 5:
# 		n = n + i

# print n


# 2.)
# Q3 The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

n = 600851475143
i = 2
while i * i < n:
	while n % i == 0:
		n = n / i
		i = i + 1

print n

# 3.)
# Q6: The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

r = xrange(1, 101)
a = sum(r)
print a * a - sum(i*i for i in r)

# 4.)
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import prime
print prime.prime(10000)