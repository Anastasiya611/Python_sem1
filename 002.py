#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and
# ⋁ - or
# ¬ - not

X = int (input("Введите X:"))
Y  = int (input("Введите Y:"))
Z = int (input("Введите Z:"))
a = (not (X or Y or Z)) == (not (X) and not (Y) and not (Z))
print (f'{X},{Y},{Z} - ¬({X} ⋁ {Y} ⋁ {Z}) = ¬{X} ⋀ ¬{Y} ⋀ ¬{Z} - {a}')