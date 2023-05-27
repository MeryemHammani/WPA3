import hashlib
import random
import sys
import libnum

q = int(input("give the prime number"))
password = input("give the password")

a = random.randint(1, 1000)
A = random.randint(1, 1000)
b = random.randint(1, 1000)
B = random.randint(1, 1000)

sA = a + A
sB = b + B

PE = int(hashlib.md5(password.encode()).hexdigest()[:8], 16)

eletA = libnum.invmod(pow(PE, A), q)
eletB = libnum.invmod(pow(PE, B), q)

PEsA = pow(PE, sA, q)
PEsB = pow(PE, sB, q)

print("client generates two random values")
print("a:\t", a)
print("A:\t", A)
print("\n accesspoint generates two random values")
print("b:\t", b)
print("B:\t", B)

print("\nclient calculates element A")
print("Element A:", eletA)
print("\naccess point calculates element A")
print("Element B:", eletB)

pmk1 = pow(PEsA * eletA, b, q)
pmk2 = pow(PEsB * eletB, a, q)

print("\nThey exchange values and calculate a secret share")
print("\nclient share:\t", pmk1)
print("access share:\t", pmk2)
