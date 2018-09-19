import random


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def find_coprime(a,z):
      if gcd(a,z) == 1:
        return z
      end
      find_coprime(a, z + 1)



m = 19 #123


p = 7 #2861 #any prime
q = 17 #2039 #any prime

n = p*q
phi=(p-1)*(q-1)

rand = random.randint(1,phi-1)
e = find_coprime(phi,1) #coprimee

d=e**(phi-1)

print("public key: ", e,n)
print("private key:", d,n)

print("_____\noriginal:", m)

x = (m**e)%n
print("encrypt ",x)
y = (x**d)%n
print("decrypt ",y)

print(y)
# Are p, q and e (coprime) given?
