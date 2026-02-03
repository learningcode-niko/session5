import random
money = random.randint(1, 10000000000)
print("Netowrh is", money)
if money > 10**9:
    print("Welcome to Forbes List")
elif money > 10**8:
    print("Welcome to Forbes Up and Coming")
elif money > 10**7:
    print("Do you like your Ferraris")
elif money> 10**6:
    print("Multimillionaire, still pretty good")
elif money > 10**5:
    print("^ Figure Worth, Decent")
elif money > 10**4:
    print("Technically not poor")
else:
    print("I'm sorry")

