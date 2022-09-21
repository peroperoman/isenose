import random

def create_player(name, is_auto=True):
    return {
        'name': name,
        'finger': 2,
        'choise': 0,
        'order': False,
        'win': False,
        'lank': None,
        'is_auto': is_auto,
    }

def init_order(players):
    init_i = random.randint(0, len(players)-1)
    players[init_i]["order"] = True
    player_names = [player["name"] for player in players]
    print(f'参加メンバー : {player_names}')
    print(f'{players[init_i]["name"]} が親となりゲームスタート。\n')

def iseno_se(players):
    def choise_finger():
        for player in players:
            if player["win"]:
                continue
            if player["is_auto"]:
                r_choise = random.randint(0, player["finger"])
                player["choise"] = r_choise
            else:
                while True:
                    try:
                        choise = int(input('-> 出す本数を入力してください : '))
                    except ValueError:
                        continue
                    if 0 <= choise <= player["finger"]:
                        player["choise"] = choise
                        break
                    else:
                        continue
        choise_total = sum([player["choise"] for player in players])
        return choise_total
    
    def order_choise():
        if not players[order_i]["is_auto"]:
            print(f'-> 全プレイヤーの指の合計数は {finger_total} です。')
            while True:
                try:
                    order_num = (int(input('-> 宣言する合計数を入力してください。 : ')))
                except ValueError:
                    continue
                if players[order_i]["choise"] <= order_num <= finger_total:
                    break
                else:
                    continue
        else:
            order_num = random.randint(players[order_i]["choise"], finger_total)
        return order_num   

    def jedgement():
        print(f'\n{players[order_i]["name"]} < いっせのーせ・・・{order_num} !\n')
        _ = ([print(f'{player["name"]} < {player["choise"]}') 
            for player in players if not player["win"]])
        print(f'\n-> 合計 : {choise_total}')
        if order_num == choise_total:
            print('-> 宣言と一致しました。\n')
            players[order_i]["finger"] -= 1
            if players[order_i]["finger"] == 0:
                print(f'{players[order_i]["name"]} 勝ち抜け!\n')
                players[order_i]["win"] = True
                players[order_i]["choise"] = 0
                players[order_i]["lank"] = lank
                return 1
        else:
            print('-> 宣言と一致しませんでした。\n')

    def order_lotate(order_i):
        players[order_i]["order"] = False
        order_i += -(len(players)-1)  if order_i == len(players)-1 else 1
        while True:
            if not players[order_i]["win"]:
                players[order_i]["order"] = True
                break
            order_i += (1 if players[order_i]["win"] 
                        and order_i != len(players)-1 else 0)
            order_i += (-(len(players)-1) if players[order_i]["win"] 
                        and order_i == len(players)-1 else 0)

    def end_display():
        for player in players:
            if player["lank"] == None: player["lank"] = len(players)
        print('\n' + '*'*30)
        print(f'- {turn}ターンでゲームが終了しました -\n[順位]')
        lanks = {player["name"]: player["lank"] for player in players}
        s_lanks = dict(sorted(lanks.items(), key=lambda x: x[1]))
        _ = [print(f'{v}位\t: {k}') for k, v in s_lanks.items()]
        print('*'*30)

    lank, turn = 1, 1
    while len([player["name"] for player in players if not player["win"]]) != 1:
        order_i = (int(''.join([str(i) for i in range(len(players)) 
                    if players[i]["order"]]))) 
        print('*'*10, f'{turn}ターン目 -> 親={players[order_i]["name"]}', '*'*10)
        _ = ([print(f'{player["name"]}\t: 指の残数 -> {player["finger"]}') 
            for player in players if not player["win"]])
        finger_total = sum([player["finger"] for player in players])
        choise_total = choise_finger()
        order_num = order_choise()
        r = jedgement()
        lank += 1 if r == 1 else 0
        order_lotate(order_i)
        turn += 1
    end_display()
    
def main():
    while True:
        try:
            cpu_num = int(input('あなた以外のプレイヤー数(CPU)を入力してください : '))
            break
        except ValueError:
            pass    
    players = ([create_player('You', is_auto=False)] 
            + [create_player(f'CPU-{i}') for i in range(1, cpu_num + 1)])
    # players = ([create_player('You')] 
    #         + [create_player(f'CPU-{i}') for i in range(1, cpu_num + 1)])
    init_order(players)
    iseno_se(players)    

if __name__ == '__main__':
    main()
