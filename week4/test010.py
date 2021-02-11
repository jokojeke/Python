import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n 1.Open Notepad\n 2.Open Snapcamera\n 3.Exit ')
    choice = input('Select Menu :')

def opennotepad():
    filename = '%windir%\\system32\\notepad.exe'
    print('Memorandum Writing %s' %filename)
    os.system(filename)

def opensnapcamera():
    filename = 'C:\\Program Files\\Snap Inc\\Snap Camera\\Snap Camera.exe'
    print('Snap Camera %s' %filename)
    os.system(filename)

while True:
    menu() 
    if choice == '1' :
        opennotepad()
    elif choice == '2':
        opensnapcamera()
    else:
        break