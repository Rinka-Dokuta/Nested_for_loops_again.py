for i in range(2):
    for j in range(3):
        print("*", end = " ")
    print()
    
print()

for i in range(5):
    for j in range(5):
        print(j, end = " ")
    print()
    
print()

for i in range(5): #rows
    for j in range(i): #columns
        print("*", end = " ")
    print()
