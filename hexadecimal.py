import random

print(10)
print(hex(10))
print(int(0x0a))
print(int(0x0f))
print(int(0x10))

num = random.randint(0,100)
print("What decimal number is this hex value? ", hex(num))
answer = int(input())
if num == answer:
    print("Correct")
else:
    print("Try again")

  