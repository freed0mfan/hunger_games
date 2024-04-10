import random

print('''Добрый день, уважаемые участники! Мы рады приветствовать вас на голодных играх за звание лучшего питониста НГУ!
      Правила игры просты:
      1. Каждый игровой час вы должны принимать решение о действиях на его протяжении. Всего вам доступно 5 вариантов,
      каждый из них влияет как на ваши ресурсы, так и на взаимодействие с другими игроками.
      2. Иногда на арене возникают случайные явления: они могут как навредить вам, так и помочь.
      3. Победитель - либо один, последний оставшийся в живых, либо никто :)
      4. Все из вас в равных условиях. Победе способствует только ваша стратегия и сила вселенского хаоса.
      
      Назовите свои имена, о воины прогерского легиона!
      ''')

players = []
for n in range(4):
    players.append(input(f'Игрок №{n + 1}: '))

HP = [100, 100, 100, 100]
weapons = [10, 10, 10, 10]
vulnerability = [2, 2, 2, 2]
medicine = [10, 10, 10, 10]


def stats():
    for player in range(4):
        if HP[player] <= 0:
            print(f'{player + 1}-й игрок мертв')
        else:
            print(f'''Показатели {player + 1}-го игрока: 
        HP: {HP[player]}
        Наносимый урон: {weapons[player]}
        Шанс получить урон: 1 к {vulnerability[player]}
        Может восстановить за ход: {medicine[player]} HP''')


def acid_rain():
    print('''
~~~Приближаются кислотные облака...
    ''')
    damage = random.randint(30, 50)
    if random.randint(1, 3) == 1:
        print(f'''Кислотный дождь ранит всех на {damage} HP~~~
        ''')
        for player in range(4):
            HP[player] -= damage
    else:
        print('''... и проходят мимо~~~
        ''')


def blessing():
    lucky = random.randint(0, 3)
    up = random.randint(20, 60)
    HP[lucky] += up
    print(f'''
    *** {players[lucky]}, вам везет! Вселенная  дает вам +{up} HP ***
    ''')


def move():
    return int(input('''
    Ваше действие:
    1. Атаковать соперника
    2. Улучшить оружие
    3. Подлечиться
    4. Снизить уязвимость
    5. Найти лекарства
    [1-5]: '''))


def attack():
    target = int(input('Атаковать игрока №: ')) - 1
    if random.randint(1, vulnerability[target]) == 1:
        HP[target] -= weapons[making_move]
        print(f'{players[target]} получает урон равный {weapons[making_move]} HP')
    else:
        print(f'{players[target]} уворачивается от атаки')


def upgrade_weapon():
    weapons[making_move] += 10
    print(f'{players[making_move]} теперь имеет оружие, наносящее на 10 HP больше урона')


def heal():
    HP[making_move] += medicine[making_move]
    print(f'{players[making_move]} восстанавливает {medicine[making_move]} HP')


def lower_vulnerability():
    vulnerability[making_move] += 1
    print(f'{players[making_move]} уменьшает свои шансы подвергнуться атаке до 1 к {vulnerability[making_move]}')


def upgrade_heal():
    medicine[making_move] += 10
    print(f'{players[making_move]} теперь может восстанавливать на 10 HP больше')


alive = players
hour = 1
making_move = 0
while len(alive) > 1:
    print(f'___________________________{hour}-й час противостояния___________________________')
    for making_move in 0, 1, 2, 3:
        if players[making_move] in alive:
            print(f'''
            Ходит {players[making_move]}.''')
            decision = move()
            match decision:
                case 1:
                    attack()
                case 2:
                    upgrade_weapon()
                case 3:
                    heal()
                case 4:
                    lower_vulnerability()
                case 5:
                    upgrade_heal()
            for player in range(4):
                if HP[player] <= 0:
                    alive.remove(players[player])
                    print(f'Из состязания выбыл/а: {players[player]}')
    blessing()
    acid_rain()
    stats()
    hour += 1
if len(alive) != 0:
    print(f'Поздравляем! {alive[0]} - лучший питонист НГУ!')
else:
    print(f'Все умерли! А это значит, хаос победил)')
