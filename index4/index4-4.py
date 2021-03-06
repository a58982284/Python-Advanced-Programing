# coding:utf8
'''
如何将多个小字符串拼接成一个大的字符串
在设计某网络程序时,我们自定义一个基于UDP的网络协议
按照固定次序向服务器传递一系列参数
hwDetect:      "<0112>"
gxDepthBits:   "<32>"
gxResolution:  "<1024x768>"
gxRefresh:     "<60>"
fullAlpha:     "<1>"
lodDist:       "<100.0>"
DistCull:      "<500.0>"

在程序中我们将各个参数按次序收集到列表中:
["<0112>","<32>","<1024x768>","<60>","<1>","<100.0>","<500.0>"]
最终我们要把各个参数拼接成一个数据报进行发送:
"<0112><32><1024x768><60><1><100.0><500.0>"
'''
L = ["<0112>", "<32>", "<1024x768>", "<60>", "<1>", "<100.0>", "<500.0>"]
S = ''
for x in L:
    S = S + x
print(S)
print(reduce(lambda x, y: x + y, L))
print(type(L))
# 以上两种方法会造成资源的浪费,推荐使用str.join(iterable) str为生成的字符串元素的分隔符
print(''.join(L))
# iterator

# 如果iterator内部组成不全是字符串
L = ["<0112>", "<32>", "<1024x768>", 60, "<1>", "<100.0>", "<500.0>"]
print(''.join(str(x) for x in L))