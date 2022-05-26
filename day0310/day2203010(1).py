from re import A
import numpy
"""
a = "py"
b = "thon"
print(a+b)
"""

"""
for i in range(-10,50,2):
  print(i)
"""

"""
a = ["changhyon","jiwon","iu","bts"]
print(a)
"""

"""
for i in range(2,10) :
  print(i)
  for j in range(2,i) :
    print("What is j =", j)
    if i%j==0:
      print("You get out")
      break
    else :
      print("Remainer is not zero")
  else :
    print(i, "is the  PrimeNumber")
"""
"""
def fib2(n) :

  result = []
  a,b =0,1
  while a<n :
    result.append(a)
    print(a, end=' ')
    a,b = b, a+b
  print()
  return result


fib2000 = fib2(2000)

"""

"""
def fib2(n) :
  a,b = 0,1
  while a<n :
    print(a)
    a,b = b,a+b

print(fib2(10))
print(fib2(100))
print(fib2(1000))
print(fib2(10000))
"""

"""
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue') :
  print("--This parrot wouldn't", action, end=' ')
  print("if you put", voltage, "volts through it.")
  print("--Lovely plumage, the", type)
  print("--It's", state,"!")

parrot()
parrot(voltage=5.0, 'dead')
parrot(110, voltage=220)
parrot(actior=)
"""

"""
def addone(n) :
  return lamda x:x+n

addone(1)#f(x)=x+1
addone(100)#f(x)=x+100
"""

