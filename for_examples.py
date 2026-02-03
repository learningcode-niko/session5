i=0 # initialising
while i<10:
    print(i)
    i=i+1 # progressing
print()
for i in range(10): # the whole thing is done by range
    print(i)

for i in range(0, 100, 7):
    print(i)

for i in range(15):
    print(7*i)

for i in range(1,11):
    for j in range(i,11): # this can use variables
        print(f"{i} x {j} = {i*j}")
    print()
# done


