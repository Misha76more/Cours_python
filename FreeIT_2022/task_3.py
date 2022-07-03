#3.1
print("Hello world")

#3.2
user = input()
print(f"Hello, {user}")

#3.3
mes = 'Hi, I am a string variable'
mes1 = 100
print(f"{mes} {mes1}")

#3.4
import math
print(math.factorial(100))

#3.5
tup = list(i for i in range(0,101,2))
tup = tuple(tup)
print(tup)

#3.6
tup = (0,4,16)
tup = [i**2 for i in list(tup)]
print(tup)

#3.7
tup_1 = 'sounds/lofi/chillstep.wav'
tup_1 = tup_1.replace('sounds', 'midi') 
print(tup_1[-4:])

#3.8
a = [1, 1, 2, 3, 5, 8, 10, 10]
print(set(a))

#3.9
print([i + 1 for i in list(a)])

#3.10
print('Python is the most popular programming language'.count('p'))

#3.11
a = [0,2,3,4]
b = [2,2,5]
print(set(a) - set(b))
