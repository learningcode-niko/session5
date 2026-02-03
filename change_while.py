import random
sum = 0
rolls = 100
while rolls > 0:
    result = random.randint(1, 6)
    sum += result
    rolls -= 1

print("I got", sum)

