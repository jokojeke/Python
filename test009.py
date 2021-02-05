print('#'*50)
a =int(input('Please Enter Your Number Of Students : '))
print('#'*50)
point =[0,0,0,0,0,0]
score =['0-49:','50-59:','60-69:','70-79:','80-89:','90-100:']
b = 1
while b <= a :
    c = int(input('[%d] Please Enter Students Score : '%b))
    b += 1
    if c >= 0 and c <=49:
        point[0] +=1
    elif c >= 50 and c <= 59:
        point[1] +=1
    elif c >= 60 and c <= 69:
        point[2] +=1
    elif c >= 70 and c <= 79:
        point[3] +=1
    elif c >= 80 and c <= 89:
        point[4] +=1
    elif c >= 90 and c <= 100:
        point[5] +=1
print('-'*50)
for x in range(0,6):
    print(score[x],'*'*point[x])