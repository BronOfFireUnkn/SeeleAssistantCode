#可动变量声明区域开始#

"adb地址，更改为你自己模拟器的adb地址，不会开adb找不到adb就百度，百度也找不着就默认,adb调用airtest核心与根目录的adb，不是你自己的adb，无需单独配置adb环境变量"
ADB_SERVER_IP = '127.0.0.1'
ADB_SERVER_PORT = 5555

"模拟器地址/游戏地址，蓝叠模拟器就是在C盘，不是你的安装位置，蓝叠模拟器不用改，其他根据实际情况改"
Game_Path = 'C:\Program Files\BlueStacks_nxt\HD-Player.exe'

"1=官服 2=B服"
var1 = 1

"不推荐开，除非你真的特别懒"
var2 = 0

"开启会大幅延长脚本运行时间，不过既然这是模拟器的话也无所谓的对吧"
var3 = 1

"需要代打万象虚境吗，不过暂时只支持第二关哦，var4调整成0为不打，需要自己调整队伍"
"通用模版请将var5调成0，暂时只支持人律特殊模版"
var4 = 1
var5 = 1

"商店金币购买，开启将var6调成1，关闭为0"
"普通晶体核心为变量var7，调整同上"
var6 = 1
var7 = 1

"远征次数，默认为3，测试期间为了体力安全建议不要动"
var8 = 3

"家园派遣次数，默认为4，测试期间为了体力安全建议不要动"
var9 = 4
#可动变量声明区域结束#

#不可动变量声明区域开始#
A = 1
B = 2
C = 1
D = 1
E = 1
F = 1
G = 1
H = 1
I = 1
J = 1
K = 1
I = 1
#不可动变量声明区域结束#
