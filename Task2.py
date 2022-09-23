# Задача 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# (¬ отрицание, ∧ и, ∨ или)

x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
z = int(input('Введите значение z: '))

p = [x, y, z] 

def checkPredicate(p):
    left = not (p[0] or p[1] or p[2])
    right = not p[0] and not p[1] and not p[2]
    result = left == right
    return result
    
if checkPredicate(p) == True:
    print(f'Утверждение истинно')
else:
    print(f'Утверждение ложно')

