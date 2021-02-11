print("\t เลือกเมนูเพื่อทำรายการ")
print("#"*50)
print("\t กด 1 เลือกเหมาจ่าย")
print("\t กด 2 เลือกจ่ายเพิ่ม")
c = int(input(""))
km = int(input(" Enter your distance : \n"))
if c == 1:
    if km <=25 :
        print("จ่ายทั้งหมด 25 บาท")
    elif km > 25 :
        print("จ่ายทั้งหมด 55 บาท")
if c == 2:
    if km <= 25:
        print("จ่ายทั้งหมด 25 บาท")
    elif km > 25:
        print("จ่ายทั้งหมด 80 บาท")


