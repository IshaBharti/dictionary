list1=["one","two","three","four","five"]

list2=[1,2,3,4,5,] 
list=[]

i=0
while i<len(list1):
    res = {list1[i]: list2[i] }
    list.append(res)
    i=i+1
  

print (" dictionary is : " ,list) 