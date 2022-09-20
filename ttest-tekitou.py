import random


def create_player(name):
    return {
        'name': name,
        'finger': 2,
        'choise': 0,
        'order': False,
        'win': False,
        'lank': None,
    }

def init_order(players):
    init_idx = random.randint(0, len(players)-1)
    players[init_idx]["order"] = True
    player_names = [player["name"] for player in players]
    print(f'参加メンバー : {player_names}')
    print(f'{players[init_idx]["name"]} が親となりゲームスタート。\n')

def iseno_se(players):
    def choise_finger():
        while True:
            try:
                choise = int(input(f'あなたの指の残数 : {players[0]["finger"]}\n出す本数を入力してください : '))
            except ValueError:
                continue

            if 0 <= choise <= players[0]["finger"]:
                players[0]["choise"] = choise
                break
            else:
                continue
        
        for idx in range(1, len(players)):
            if players[idx]["win"]:
                continue
            cpu_choise = random.randint(0, players[idx]["finger"])
            players[idx]["choise"] = cpu_choise
        choise_total = sum([player["choise"] for player in players])
        return choise_total
    
    def order_info():
        print('-'*30)
        print(f'プレイヤー数 : {len(player_names)}')
        print(f'指の合計 :  {finger_total} ')
        print(f'あなたは {players[order_idx[0]]["choise"]} 本の指を出す予定。')
        print('-'*30)

    def order_choise():
        if players[order_idx[0]]["name"] == 'You':
            while True:
                order_info()
                try:
                    order_num = (int(input('宣言する合計本数を入力してください。 : ')))
                except ValueError:
                    continue

                if players[order_idx[0]]["choise"] <= order_num <= finger_total:
                    break
                else:
                    continue
        else:
            order_num = random.randint(players[order_idx[0]]["choise"], finger_total)  
        return order_num   

    def jedgement():
        print(f'\n{players[order_idx[0]]["name"]} < いっせのーせ・・・\n\n{order_num} !\n')
        _ = [print(f'{player["name"]} : {player["choise"]}') for player in players]            
        print(f'合計 : {choise_total}\n')
        if order_num == choise_total:
            print('-> 宣言と一致しました。\n')
            players[order_idx[0]]["finger"] -= 1
            if players[order_idx[0]]["finger"] == 0:
                print(f'{players[order_idx[0]]["name"]} 勝ち抜け!\n')
                players[order_idx[0]]["win"] = True
                players[order_idx[0]]["lank"] = lank
                return 1
        else:
            print('-> 宣言と一致しませんでした。\n')

    def order_lotate():
        players[order_idx[0]]["order"] = False
        if order_idx[0] == len(players)-1:
            order_idx[0] = 0
        else:
            order_idx[0] += 1
        while True:
            if players[order_idx[0]]["win"] == False:
                players[order_idx[0]]["order"] = True
                break
            if players[order_idx[0]]["win"] == True and order_idx[0] != len(players)-1:
                order_idx[0] += 1
            if players[order_idx[0]]["win"] == True and order_idx[0] == len(players)-1:
                order_idx[0] = 0

    lank = 1
    while len([player["name"] for player in players if not player["win"]]) != 1:
        order_idx = [idx for idx in range(len(players)) if players[idx]["order"]]
        print('-'*30, f'\n親 : {players[order_idx[0]]["name"]}')
        player_names = [player["name"] for player in players if not player["win"]]
        finger_total = sum([player["finger"] for player in players])
        choise_total = choise_finger()
        order_num = order_choise()
        r = jedgement()
        lank += 1 if r == 1 else 0
        order_lotate()
        _ = [print(f'{player["name"]} の残数: {player["finger"]}') for player in players]
    
    for player in players:
        if player["lank"] == None:
            player["lank"] = len(players)
    print('\n' + '*'*30)
    print('- ゲーム終了 -')
    _ = [print(f'{player["name"]} : {player["lank"]} 位') for player in players]
    print('*'*30)

def main():
    while True:
        try:
            cpu_num = int(input('あなた以外のプレイヤー数(CPU)を入力してください : '))
            break
        except ValueError:
            pass
    players = [create_player('You')] + [create_player(f'CPU-{i}') for i in range(1, cpu_num + 1)]
    init_order(players)
    iseno_se(players)    

if __name__ == '__main__':
    main()
