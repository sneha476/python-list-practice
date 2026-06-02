l=[10,20,30,40]
l.append(50)
print(l)
l3=(1,2,3)
l.append(l3)
print(l)
l2=(6,7)
l.extend(l2)
print(l)
l.insert(9,"hello")
print(l)
print(l.pop(4))
print(l.remove(40))
print(l.remove(10))
l=[10,10,20,30,60,20]
print(l.count(10))
l2=l.copy
print(l)
l.clear()
# print(l)

l=[10,20,30,40,50,60]
max=0
for i in l:
    if i>max:
        max=i
print(max)
min=l[0]
for i in range(len(l)):
    if l[i]<min:
        min=l[i]
print(min)
sum=0
for i in l:
    sum+=i
    print(sum)

product=1
for i in l:
    product*=i
print(product)


        
