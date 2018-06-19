import time

t = time.localtime()
a=time.asctime(t)
print(t)
print(a)
print(a[0])
print(t.tm_hour)
print(isinstance(t.tm_hour,int))#判断数据类型

print('你好')


def ai(c):
    item_ball = ('乒乓球运动训练'，'气排球'，'男子篮球')
    item_outdoor = ('跑步')
    c = c.decode('gbk').encode('utf-8')


    if c in item_ball:
        print('推荐运动类型：球类运动')
    elif c in item_outdoor :

if __name__ == '__main__':
    a =ai('跑步')
