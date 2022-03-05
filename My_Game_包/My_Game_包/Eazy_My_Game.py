from __future__ import print_function
import os

def Run(author, version, corporation, copyright=None):
    print(
        author + '''Windows 版本 [''' + version + ''']\n(''' + copyright + ''') ''' + corporation + ''' Corporation.all rights reserved.''')

def NewTempFile(NewTempFileName= 'TempFile'):
    NewTempFileName = open('C:\Windows\Temp' + NewTempFileName + '.Temp_MG', 'w')
    print('''记得关闭文件，释放内存哦！\n路径：C:\Windows\Temp\ ''' + NewTempFileName)
def Run_MyGame_FlappyBird():
    os.system(r"python MyGame_OK-Game_Flappy-Bird.py")
def Run_MyGame_snake():
    os.system(r"python MyGame_OK-Game_snake.py")
def Run_MyGame_translate():
    os.system(r"python MyGame_OK_translate.py")
def Run_MyGame_UAC():
    os.system(r"python MyGame_UAC.py")
def Run_When_bored():
    os.system(r"python When_bored.py")