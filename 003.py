#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
#Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3
x = int (input("Введите X:"))
y  = int (input("Введите Y:"))
if ( x > 0 and y > 0 ):
    print ("I")
if ( x < 0 and y > 0 ):
    print ("II")
if ( x < 0 and y < 0 ):
    print ("III")
if ( x > 0 and y < 0 ):
    print ("IV")   

