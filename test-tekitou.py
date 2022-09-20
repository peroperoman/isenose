import random

class Player():
    def __init__(self, name):
        self.name = name
        self.finger = 2
        self.choise = 0
        self.order = False
        self.win = False
        self.lank = None

    def __repr__(self):
        return self.name

class IsenoSe():
    # def __init__(self, *args):
    def __init__(self, players):
        # self.players = list(args)
        self.players = players
        self.init_idx = random.randint(0, len(self.players)-1)
        self.players[self.init_idx].order = True
        self.farst_display()

    def farst_display(self):
        player_names = [i.name for i in self.players]
        print(f'参加メンバー : {player_names}')
        print(f'{self.players[self.init_idx].name} が親となりゲームスタート。\n')

    def run(self):
        def choise_finger():
            while True:
                choise = int(input(f'あなたの指の本数は残り {self.players[0].finger} です。\n次に出す本数を入力してください : '))
                # choise = 1
                if 0 <= choise <= self.players[0].finger:
                    self.players[0].choise = choise
                    break
                else:
                    continue
            
            for idx in range(1, len(self.players)):
                if self.players[idx].win:
                    continue
                cpu_choise = random.randint(0, self.players[idx].finger)
                self.players[idx].choise = cpu_choise
            choise_total = sum([i.choise for i in self.players])
            return choise_total
        
        def order_info():
            print('*'*30)
            print(f'プレイヤー数 : {len(player_names)}')
            print(f'指の合計 :  {finger_total} ')
            print(f'あなたは {self.players[order_idx[0]].choise} 本の指を出す予定。')
            print('*'*30)

        def order_choise():
            if self.players[order_idx[0]].name == 'You':
                while True:
                    order_info()
                    order_num = (int(input('宣言する合計本数を入力してください。 : ')))
                    # order_num = 1
                    if self.players[order_idx[0]].choise <= order_num <= finger_total:
                        break
                    else:
                        continue
            else:
                order_num = random.randint(self.players[order_idx[0]].choise, finger_total)  
            return order_num   

        def jedgement():
            print(f'\n{self.players[order_idx[0]].name} < いっせのーせ・・・\n\n{order_num} !\n')
            for i in self.players:
                print(f'{i.name} : {i.choise}')
            print(f'合計 : {choise_total}\n')
            if order_num == choise_total:
                print('-> 宣言と一致しました。\n')
                self.players[order_idx[0]].finger -= 1
                if self.players[order_idx[0]].finger == 0:
                    print(f'{self.players[order_idx[0]].name} 勝ち抜け!\n')
                    self.players[order_idx[0]].win = True
            else:
                print('-> 宣言と一致しませんでした。\n')

        def order_lotate():
            self.players[order_idx[0]].order = False
            if order_idx[0] == len(self.players)-1:
                order_idx[0] = 0
            else:
                order_idx[0] += 1
            while True:
                if self.players[order_idx[0]].win == False:
                    self.players[order_idx[0]].order = True
                    break
                if self.players[order_idx[0]].win == True and order_idx[0] != len(self.players)-1:
                    order_idx[0] += 1
                if self.players[order_idx[0]].win == True and order_idx[0] == len(self.players)-1:
                    order_idx[0] = 0
    
        while self.players[0].finger != 0 and len([i.name for i in self.players if not i.win]) != 1:
            order_idx = [i for i in range(len(self.players)) if self.players[i].order]
            print('-'*20, f'\n親 : {self.players[order_idx[0]].name}\n')
            player_names = [i.name for i in self.players if not i.win]
            finger_total = sum([i.finger for i in self.players])
            choise_total = choise_finger()
            order_num = order_choise()
            jedgement()
            order_lotate()
            for player in self.players:
                print(player.name, player.finger, player.win)

def main():
    cpu_num = int(input('あなた以外のプレイヤー数(CPU)を入力してください : '))
    players = [Player('You')] + [Player(f'CPU-{i}') for i in range(1, cpu_num + 1)]
    isenose = IsenoSe(players)
    isenose.run()

if __name__ == '__main__':
    main()
    