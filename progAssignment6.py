
#Number 6
h = input('Enter hex: ').lstrip('#')
print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

#Number 5
dec = 600

print("The decimal value of", dec, "is:")
print(bin(dec), "bin")
print(oct(dec), "oct")
print(hex(dec), "hex")

#Number 4
num = 13
if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")
    
    #Number 3
lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)