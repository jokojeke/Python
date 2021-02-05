print("\t ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
print('#'*70)
num=1
a=[]
b=""
c=1
while b !='exit' :
    b=input("อาหารโปรดอันดับที่ "+str(num)+" คือ\t")
    a.append(b)    
    num+=1
a.pop()

print('อาหารสุดโปรดของคุณมีดังนี้',end='')
for i in a : 
    print(str(c)+"."+i+" ",end='')
    c+=1