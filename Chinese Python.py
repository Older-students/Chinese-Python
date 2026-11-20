#---------导入(Import)----------
from code import interact as 保持控制台
import os
import sys
import time
import pygame
import tkinter as 图形界面导入
import ctypes
#----------真和假(True and False)----------
真 = True
假 = False
#----------图形界面(Graphical User Interface)----------
图形界面 = 图形界面导入.Tk()
标题 = 图形界面.title
标题("提示")
窗口大小 = 图形界面.geometry
窗口大小("200x100")
是否允许用户调整窗口大小 = 图形界面.resizable
是否允许用户调整窗口大小(假,假)
文本 = 图形界面导入.Label
文本(图形界面, text = "翻译可能不完全,请见谅", font = ("微软雅黑", 12)).pack(pady = 5)
按钮 = 图形界面导入.Button
按钮(图形界面, text="确认", command = lambda:退出图形界面()).pack(pady = 5)
def 退出图形界面():
    退出 = 图形界面.destroy()
    退出
#----------普通指令(Instruction)----------
打印 = print
整数 = int
字符串 = str
浮点数 = float
退出 = sys.exit

#----------函数(Function)----------
def 帮助():
    打印('''    ----------显示帮助----------
    ----------基本指令----------
    真 = True
    假 = False
    打印 = print
    整数 = int
    字符串 = str
    浮点数 = float
    退出 = sys.exit
    ----------函数----------
    帮助() = 显示帮助
    当以下条件达成时重复执行(条件,事情) = 当条件为真时重复执行事情
    重复执行(事情) = 无限循环执行事情
    重复_次执行(次数,事情) = 执行事情指定次数
    版本() = 显示版本信息
    ''')
def 当以下条件达成时重复执行(条件,事情):
    while 条件:
        事情()
def 重复执行(事情):
    while True:
        事情()
def 重复_次执行(次数,事情):
    for _ in range(整数(次数)):
        事情()
def 版本():
    打印("作者不知道这是第几个版本")

#----------控制台(Console)----------
保持控制台(local=globals())