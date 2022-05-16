#For Loop
# list_1=[1,2,3,4,5,6,7,8,9]
# even_count=0
# odd_count=0
# for num in list_1:
#     if num%2==0:
#         even_count= even_count+1
#     else:
#         odd_count = odd_count+1
# print("Count of Even number : ",even_count)
# print("Count of Odd number :",odd_count)

#While Loop

list_1=[1,2,3,4,5,6,7,8,9]
even_count=0
odd_count=0
num=0
while num<len(list_1):
    if list_1[num]%2==0:
        even_count= even_count+1
    else:
        odd_count = odd_count+1
        num=num+1
print("Count of Even number :",even_count)
print("Count of Odd number :",odd_count)
    