import os
choice = 0
goods = [0,0,0,0,0]
pick = 0
def menu():
    global choice
    print('\tโปรแกรมร้านขายผักปลอดสารพิษ\n' ,'1.แสดงรายการผัก\n 2.หยิบสินค้าลงตะกร้า\n 3.แสดงจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม' )
    choice = input('กรุณาเลือกทำรายการ : ')
    screen_clear()

def menu1():
    print('\tรายการผักในร้าน')
    print('\t1.ผักสลัดแก้ว ราคา 50 บาท\n','\t2.หน่อไม้ฝรั่ง ราคา 45 บาท\n','\t3.กะหล่ำปลี ราคา 40 บาท\n','\t4.ขึ้นช่าย ราคา 25 บาท\n','\t5.ผักชี ราคา 10 บาท' )

def menu2():
   global pick
    print('\tรายการสินค้า\n 1.ผักสลัดแก้ว\n 2.หน่อไม่ฝรั่ง\n 3.กะหล่ำปลี\n 4.ขึ้นช่าย\n 5.ผักชี')
    pick = int(input('เลือกหยิบสินค้าตามหมายเลข : '))
    if pick == 1:
        goods[0] += 1
    elif pick == 2:
        goods[1] += 1
    elif pick == 3:
        goods[2] += 1
    elif pick == 4:
        goods[3] += 1
    elif pick == 5:
        goods[4] += 1
    screen_clear()

def menu3():
    list_score = ['ผักสลัดแก้ว','หน่อไม้ฝรั่ง','กะหล่ำปลี','ขึ้นช่าย','ผักชี']
    list_price = [50,45,40,25,10]
    print('{0:-<13}{1:-<13}{2:-<13}{3}'.format('สินค้า','ราคา','จำนวน','ราคาทั้งหมด'))
    for i in range(0,5);
        print('{0:-<13}{1:-<13}{2:-<13}{3}'.format(list_score[i],list_price[i],goods[i],goods[i]*list_price[i]))
    
def menu4():
    print('\t\nรายการสินค้า\n 1.ผักสลัดแก้ว\n 2.หน่อไม้ฝรั่ง\n 3.กะหล่ะปลี\n 4.ขึ้นช่าย\n 5.ผักชี')
    ggclear = int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก'))
    if ggclear == 1:
        goods[0] -= 1
    elif ggclear == 2:
        goods[1] -= 1
    elif ggclear == 3:
        goods[2] -= 1
    elif ggclear == 4:
        goods[3] -= 1
    elif ggclear == 5:
        goods[4] -= 1

def screen_clear():
    cleascreen = os.system('cls')


while True:
    menu()
    
    if  choice == '1':
        screen_clear()
        menu1()
    elif choice == '2':
        screen_clear()
        menu2()
    elif choice == '3':
        screen_clear()
        menu3()
    elif choice == '4':
        menu4()
        screen_clear()
    elif choice == '5':
        v =input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n: ')
        if v.lower == 'y':
            screen_clear()
        elif v.lower == 'n':
            screen_clear()
            break
            
   