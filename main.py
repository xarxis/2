a=[3,4,7]
print(type(a))
b=[1,2,3,4,5,6]
#b.append(7)
#b.extend(a)
b.insert(3,7)
#b.remove(7)
b.sort()
#b.reverse()
#print(b[3])
#c=[]
#for i in range (10):
   # c.append(i)
#print(c)


#Словари
d={}
e={"BMW":50000,"TOYOTA":30000,"LADA":"priora"}
#print(e.keys())
#print(e.items())
#print(e.values())
#print(e["BMW"])
#print(e.pop("BMW"))
#print(e.fromkeys("BMW"))

#регулярные выражения
import re
string="My,name,is,Valera"
res=string.split(",")
#res= re.search("n",string)
res=string.find("is")
print(res)