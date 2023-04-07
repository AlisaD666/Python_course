e = int(input('Введите год: '))
if e%4==0 and e%100!=0 or e%400==0: 
    print('Високосный')
else :
    print('Год не високосный')