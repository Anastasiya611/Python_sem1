# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).



x = int (input("Введите номер четвети:"))
if ( x == 1 ):
    print ("x > 0 and y > 0")
if ( x == 2 ):
    print ("x < 0 and y > 0")
if ( x == 3 ):
    print (" x < 0 and y < 0")
if ( x == 4 ):
    print ("x > 0 and y < 0")   