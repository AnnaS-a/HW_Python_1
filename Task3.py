# Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0, и выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример: x=34; y=-30 -> 4      x=2; y=4-> 1           x=-34; y=-30 -> 3

x = int(input('Введите значение x отличное от нуля: '))
y = int(input('Введите значение y отличное от нуля: '))

if x > 0 and y > 0:
    print(f'точка с координатами ({x}; {y}) находится в 1 четверти плоскости')
elif x < 0 and y > 0:
    print(f'точка с координатами ({x}; {y}) находится во 2 четверти плоскости')
elif x < 0 and y < 0:
    print(f'точка с координатами ({x}; {y}) находится в 3 четверти плоскости')
elif x > 0 and y < 0:
    print(f'точка с координатами ({x}; {y}) находится в 4 четверти плоскости')   
elif x == 0 or y == 0:
    print('точка лежит на одной из осей координат')
else:
    print('Введены некорректные значения')
