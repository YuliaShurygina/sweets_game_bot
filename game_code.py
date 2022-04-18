from random import randint

def game_with_bot_hard(sweets, maximum_sweets, queue):
    i = 0
    while sweets > maximum_sweets:
        if queue == 1:
            a = input(f'ход игрока:\n введите количество забираемых конфет от 1 до {maximum_sweets}: ')
            if not a.isdigit():
                print("Неверно введено число")
                continue
            a = int(a)
            if a < 1 or a > maximum_sweets:
                print("Неверно введено число")
                continue
            queue = 2
        else:
            a = sweets%(maximum_sweets+1)
            if a == 0:
                a = 1
            print(f"ход компьютера {a}")
            queue = 1
        sweets -= a
        print(f"Осталось {sweets} конфет")
        i += 1
        
    if queue == 1: return f'Выиграл игрок'
    else: return 'Выиграл компьютер'   
 
def game_with_bot_middle(sweets, maximum_sweets, queue):
    i = 0
    while sweets > maximum_sweets:
        if queue == 1:
            a = input(f'ход игрока:\n введите количество забираемых конфет от 1 до {maximum_sweets}: ')
            if not a.isdigit():
                print("Неверно введено число")
                continue
            a = int(a)
            if a < 1 or a > maximum_sweets:
                print("Неверно введено число")
                continue
            queue = 2
        else:
            if i ==0 or i == 1:
                a = randint(1, maximum_sweets)
            else:
                a = sweets%(maximum_sweets+1)
                if a == 0:
                    a = randint(1, maximum_sweets)
            print(f"ход компьютера {a}")
            queue = 1
        sweets -= a
        print(f"Осталось {sweets} конфет")
        i += 1
    if queue == 1: return f'Выиграл игрок'
    else: return 'Выиграл компьютер'

def game_with_bot_easy(sweets, maximum_sweets, queue):
    i = 0
    while sweets > maximum_sweets:
        if queue == 1:
            a = input(f'ход игрока:\n введите количество забираемых конфет от 1 до {maximum_sweets}: ')
            if not a.isdigit():
                print("Неверно введено число")
                continue
            a = int(a)
            if a < 1 or a > maximum_sweets:
                print("Неверно введено число")
                continue
            queue = 2
        else: 
            a = randint(1, maximum_sweets)
            print(f"ход компьютера {a}")
            queue = 1
        sweets -= a
        print(f"Осталось {sweets} конфет")
        i += 1
    if queue == 1: return f'Выиграл игрок'
    else: return 'Выиграл компьютер'

player = randint(1,2)
level = int(input("Выберите уровень сложности: "))
if level == 1: print(game_with_bot_easy(10,3, player))
elif level == 2: print(game_with_bot_middle(10,3, player))
else: print(game_with_bot_hard(10, 3, player))