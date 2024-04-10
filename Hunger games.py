import random
import ru_local as ru

print(ru.INTRODUCTION)

players = []
for n in range(4):
    players.append(input(f'{ru.PLAYER_N}{n + 1}: '))

HP = [100, 100, 100, 100]
weapons = [10, 10, 10, 10]
vulnerability = [2, 2, 2, 2]
medicine = [10, 10, 10, 10]


def stats():
    for player in range(4):
        if HP[player] <= 0:
            print(f'{player + 1}{ru.PLAYER_DEAD}')
        else:
            print(f'''{ru.STATS} {player + 1}{ru.FOR}: 
        HP: {HP[player]}
        {ru.DAMAGE}: {weapons[player]}
        {ru.CHANCE}{vulnerability[player]}
        {ru.REGENERATION}: {medicine[player]} HP''')


def acid_rain():
    print(ru.ACID_CLOUDS)
    damage = random.randint(30, 50)
    if random.randint(1, 3) == 1:
        print(f'''{ru.ACID_DAMAGE}{damage} HP~~~
        ''')
        for player in range(4):
            HP[player] -= damage
    else:
        print(f'''{ru.PASS_BY}
        ''')


def blessing():
    lucky = random.randint(0, 3)
    up = random.randint(20, 60)
    HP[lucky] += up
    print(f'''
    *** {players[lucky]}, {ru.LUCKY} +{up} HP ***
    ''')


def move():
    return int(input(ru.MOVE))


def attack():
    target = int(input(ru.ATTACK)) - 1
    if random.randint(1, vulnerability[target]) == 1:
        HP[target] -= weapons[making_move]
        print(f'{players[target]} {ru.IS_DAMAGED} {weapons[making_move]} HP')
    else:
        print(f'{players[target]} {ru.DODGE}')


def upgrade_weapon():
    weapons[making_move] += 10
    print(f'{players[making_move]} {ru.WEAPON_UP}')


def heal():
    HP[making_move] += medicine[making_move]
    print(f'{players[making_move]} {ru.HEAL} {medicine[making_move]} HP')


def lower_vulnerability():
    vulnerability[making_move] += 1
    print(f'{players[making_move]} {ru.DEFENCE} {vulnerability[making_move]}')


def upgrade_heal():
    medicine[making_move] += 10
    print(f'{players[making_move]} {ru.MEDICINE}')


alive = players
hour = 1
making_move = 0
while len(alive) > 1:
    print(f'___________________________{hour}{ru.HOUR}___________________________')
    for making_move in 0, 1, 2, 3:
        if players[making_move] in alive:
            print(f'''
            {ru.MOVING} {players[making_move]}.''')
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
                    print(f'{ru.IS_OUT}: {players[player]}')
    blessing()
    acid_rain()
    stats()
    hour += 1
if len(alive) != 0:
    print(f'{ru.CONGRATULATIONS} {alive[0]} - {ru.BEST}')
else:
    print(ru.ALL_DEAD)
