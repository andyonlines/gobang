#! /usr/bin/env python3
"""
# *_* codeing : UTF-8 *_*
# @Author    :  Andy.Gan
# @Project   :  gobang
# @Time      :  2019/7/21 15:24
# @FileName  :  gobang.py
# @IDE       :  PyCharm
# @Contact   :  andy.freedoms@gmail.com
# @Blog      :  https://blog.csdn.net/andyonlines
# @License   :  (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# Desc       :
"""
# import lib

finish = False
flagNum = 1
flagch = '*'
x = 0
y = 0

#棋盘初始化
checkerboard = []
for i in range(10):
    checkerboard.append([])
    for j in range(10):
        checkerboard[i].append('-')

def msg():
    """


    :return: None
    """
    print("\033[1;37;44m----------------------------------------------------------")
    print("  1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkerboard)):
        print(chr(i + ord('A')) + "" ,end = ' ')
    print()
    print("------------------------------------------------------------------------\033[0m")
    if flagNum == 1:
        print('\033[32m*棋胜利！***\033[0m')
    else:
        print('\033[32mo棋胜利！***\033[0m')

while not finish:
    print('\033[1;30;46m----------------------------------------------------------------')
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkerboard)):
        print(chr(i + ord('A')) + " ",end=' ')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + ' ',end=' ')
        print()
    print("--------------------------------------------------------------------------\033[0m")
    if flagNum == 1:
        flagch = '*'
        print('\033[1;37;40m请*输入棋子的坐标（如A1）：\033[0m',end=' ')
    else:
        flagch='o'
        print('\033[1;37;40m请o输入棋子的坐标（如A1）：\033[0m', end=' ')
    str = input()
    ch = str[0]
    x = ord(ch) - 65
    y = int(str[1]) - 1
    if (x < 0 or x > 9 or y < 0 or y > 9):
        print('\033[31m***您输入的坐标有误请重新输入！***\033[0m')
        continue
    if (checkerboard[x][y] == '-'):
        if flagNum == 1:
            checkerboard[x][y] = '*'
        else:
            checkerboard[x][y] = 'o'
    else:
        print('\033[31m***您输入的坐标已经有其他的棋子请重新输入！***\033[0m')
        continue

    if y - 4 >= 0:
        if (checkerboard[x][y-1] == flagch
        and checkerboard[x][y-2] == flagch
        and checkerboard[x][y-3] == flagch
        and checkerboard[x][y-4] == flagch):
            finish = True
            msg()

    if y + 4 <= 9:
        if (checkerboard[x][y+1] == flagch
        and checkerboard[x][y+2] == flagch
        and checkerboard[x][y+3] == flagch
        and checkerboard[x][y+4] == flagch):
            finish = True
            msg()

    if x - 4 >= 0:
        if (checkerboard[x - 1][y] == flagch
        and checkerboard[x - 2][y] == flagch
        and checkerboard[x - 3][y] == flagch
        and checkerboard[x - 4][y] == flagch):
            finish = True
            msg()

    if x + 4 <= 9:
        if (checkerboard[x + 1][y] == flagch
        and checkerboard[x + 2][y] == flagch
        and checkerboard[x + 3][y] == flagch
        and checkerboard[x + 4][y] == flagch):
            finish = True
            msg()

    if (x - 4 <= 0 and y + 4 <= 9):
        if (checkerboard[x - 1][y + 1] == flagch
        and checkerboard[x - 2][y + 2] == flagch
        and checkerboard[x - 3][y + 3] == flagch
        and checkerboard[x - 4][y + 4] == flagch):
            finish = True
            msg()

    if (x + 4 <= 9 and y + 4 <= 9):
        if (checkerboard[x + 1][y + 1] == flagch
        and checkerboard[x + 2][y + 2] == flagch
        and checkerboard[x + 3][y + 3] == flagch
        and checkerboard[x + 4][y + 4] == flagch):
            finish = True
            msg()

    if (x - 4 >= 0 and y + 4 <= 9) :
        if (checkerboard[x - 1][y + 1] == flagch
        and checkerboard[x - 2][y + 2] == flagch
        and checkerboard[x - 3][y + 3] == flagch
        and checkerboard[x - 4][y + 4] == flagch):
            finish = True
            msg()
    if (x - 4 >= 0 and y - 4 >= 0):
        if (checkerboard[x - 1][y - 1] == flagch
        and checkerboard[x - 2][y - 2] == flagch
        and checkerboard[x - 3][y - 3] == flagch
        and checkerboard[x - 4][y - 4] == flagch):
            finish = True
            msg()

    flagNum *= -1
