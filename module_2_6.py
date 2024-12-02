def draw_area():
    for i in area:
        print(*i)
print('Добро пожаловать в игру крестики нолики!')
area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}') # обращение к переменной turn
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = int(input('Введите номер строки: ')) - 1
    column = int(input('Введите номер столбца: ')) - 1
    if area[row][column] == '*':
        area[row][column] = turn_char
        draw_area()
        continue
    else:
        print('Ячейка занята, Вы пропускаете ход')
    if turn == 9:
        print('Игра окончена!')
    draw_area()
# print('Выберите число от 1 до 9')
