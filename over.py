list=[]
list=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    list.append(int(input()))
print("list is:",list)
for i in list:
    if i > 100:
      list.append("over")
    else:
          list.append(i)
          print("result list is:",list)
