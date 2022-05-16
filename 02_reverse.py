# x=input("Enter a string")
# a=x.split()
# a.reverse()
# print("".join(a))

word= input("Enter the word :")
for char in range(len(word)-1,-1,-1):
    print(word[char],end="")
print("\n")