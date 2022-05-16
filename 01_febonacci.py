number = int(input("Enter the number"))
no_1,no_2=0,1
i=0

while i<number:
    print(no_1)
    no_3=no_1+no_2
    no_1=no_2
    no_2=no_3
    i=i+1

# print(i)

