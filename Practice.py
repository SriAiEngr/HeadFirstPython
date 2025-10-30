#print("First Module s Name: {}".format(__name__))

def main():
    print("First Module's Name: {}".format(__name__))

if __name__ == "__main__":
    print("Run Directly")
else:
    print("Run from Import")
    print(__name__)

#print(round(float(1223.4565),2))
"""
#type annotations"
age: int = 10
name: str = "Sri"

print ("Name:" +name,", Age:" +str(age))
print (f"Name:{name}, Age:{age}")


def calc(a: int, b: int, opr: str) -> int:
    if opr == '+':
        print(f"{a} {opr} {b}")
        return a + b
    elif opr == '-':
        print(f"{a} {opr} {b}")
        return a - b
    elif opr == '*':
        print(f"{a} {opr} {b}")
        return a * b
    elif opr == '/':
        print(f"{a} {opr} {b}")
        return a / b
    else:
        print("Invalid operation"+opr)        

print(calc(1, 2, '-*'))

for i in range(5):
    print(i)

while True:
    print("True")

i: int = 0
while i < 5:
    print(i)
    i += 1

try:
    print(1/0)
except ZeroDivisionError:
    print("Cannot divide by zero")

import math
print(math.sqrt(16))    

import math as m
print(m.sqrt(16))    
"""
