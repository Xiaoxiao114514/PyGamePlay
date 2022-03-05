import Eazy_My_Game as G
import os
User_one = '''
         ________________        ___            ___        ________________        ________________        _________________________         ________________
        /               /\      /  /\          /  /\      /  _____________/\      /               /\      /                        /\       /               /\ 
       /      ___      / /     /  / /         /  / /     /  /\____________\/     /     ___       / /     /                        / /      /      _________/ /
      /      /\ /     / /     /  / /         /  / /     /  / /                  /     /\ /      / /     /                        / /      /      /_\_______\/
     /               / /     /  / /         /  / /     /  / /__________        /               / /     /    _____     _____     / /      /                /\ 
    /   ____________/ /     /  /_/_________/  / /     /  / //______   /\      /    ______     / /     /    /\___/    /\___/    / /      /      __________/ /
   /   /\___________\/     /______     ______/ /     /  / / \_____/  / /     /    /\____/    / /     /    / /  /    / /  /    / /      /      /\_________\/
  /   / /                  \_____/    /\_____\/     /  / /       /  / /     /    / /   /    / /     /    / /  /    / /  /    / /      /      /_/_______
 /   / /                        /    / /           /  /_/_______/  / /     /    / /   /    / /     /    / /  /    / /  /    / /      /                /\ 
/___/ /                        /____/ /           /_______________/ /     /____/ /   /____/ /     /____/ /  /____/ /  /____/ /      /________________/ /
\___\/                         \____\/            \_______________\/      \____\/    \____\/      \____\/   \____\/   \____\/       \________________\/

=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=

欢迎使用MyGame包。
[Welcome to the MyGame package.]

MyGame包有多种模式 （时间原因， 只开发了 Game 模式）。
可以键入【game】 进行尝试。
[The MyGame package has multiple modes (for time reasons, only the Game mode was developed).
You can type [game] to try.]

[Game 模式]可以尝试以下命令：
                      [flappy bird, snake, translatem, html-game]
[[Game Mode] Try the following commands:
                       [flappy bird, snake, translatem, html-game]]

作者：Mr.Python （Xiaoxiao）
Github：......
Microsoft Outlook ：Hello-Python@outlook.com
[Author: Mr.Python (Xiaoxiao)
Github: ......
Microsoft Outlook: Hello-Python@outlook.com]
'''
EE = '''



'''
print(User_one)
while 1:
    print(end= '')
    ui = input('''An instruction> ''')
    while 1:
        if ui == 'game':
            Gui = input('''Game> ''')
            if Gui == 'flappy bird':
                G.Run_MyGame_FlappyBird()
                break
            elif Gui == 'snake':
                G.Run_MyGame_snake()
                break
            elif Gui == 'translate':
                G.Run_MyGame_translate()
                break
            elif Gui == '123456':
                G.Run_When_bored()
                break
            elif Gui == 'html-game':
                os.system(r'//1080//__init__.py')
                break
            elif Gui == 'over':
                break
            print(EE)
            Gui = ''
        elif ui == 'Bilibili gameUP’s game' and '-Game':
            print('''我们有以下 UP 的游戏:
            
            宅宅萝卜:
                     PVZ__BT
            M木糖M:
                    Bug大战Bug:
                                1-1
                                BOOS
                    Flappy Bug
                    Bug逃亡
                    狂扁小Bug
                    supre马尿[1-1]
                    supre马尿[1-2]
                    Bug旷工
                    第五个Bug
                    魂Bug罗(魂爸罗[?])
            火山GieGie:
                    ......
            
            
            [先Ctrl+C UP的名字]
            [Ctrl+C你想玩的游戏名]
            [Ctrl+V 到  {Bilibili gameUP’s game> }  上]
            
            ''')
        BGui = input('''Bilibili gameUP’s game> ''')
        if BGui == '宅宅萝卜':
            zz_BGui = input('''Bilibili 宅宅萝卜’s game> ''')
            if zz_BGui == 'PVZ__BT':
                pass