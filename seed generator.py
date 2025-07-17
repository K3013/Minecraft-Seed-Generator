import random
input("--------Welcome to 'random seed generator'--------")
print("Your seed is : ", end="")
for i in range(10) :
    numcandidate = random.randint(1, 99)
    print(numcandidate, end="")
print()
int(input())
