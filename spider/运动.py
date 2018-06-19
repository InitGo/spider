import time

def sport1(weather,course,step_num):
    #各变量等级分数
    A = 100
    B = 75
    C = 50
    D = 25

    #步数等级
    if(step_num < 3000):
        step_num = A
    elif(3000 <= step_num < 6000):
        step_num = B
    elif(6000 <= step_num < 9000):
        step_num = C
    else:
        step_num = D

    #天气适宜指数等级
    if (weather < 25):
        weather = D
    elif(25 <= weather < 50):
        weather = C
    elif(50 <= weather < 75):
        weather = B
    else:
        weather = A

    #课程数等级
    if (course >= 4):
        course = D
    elif(2< course <= 3 ):
        course = C
    elif (1<=course <= 2):
        course = B
    else:
        course = A

    #时间等级
    hour =time.localtime().tm_hour
    if (0 < hour < 6):
        hour = D
    elif(6 <= hour <= 17):
        hour = B
    elif(17 < hour < 22):
        hour = A
    elif(22 <= hour <24):
        hour = C

    s = step_num*0.3 + (weather + course + hour)*(1-0.3)/3

    print('推荐运动指数：%.2f' % s)
'''
    print(weather)
    print(step_num)
    print(course)
'''


def sport2(x):
    ball = {'乒乓球运动训练','气排球','男子篮球','毽球','乒乓球（高级）','羽毛球（高级）','网球（高级）','足球（高级）','篮球（高级）','女子足球',
            '板球','足球','羽毛球','网球','软式排球','乒乓球','女子排球','男子排球','男子篮球',}
    outdoor = {'游泳','攀岩',}
    gongfu = {'太极拳、剑','跆拳道','武术','散打',}
    track = {'田径','器械健美',}  #田径
    dance ={'排舞','舞蹈啦啦操','形体','女子体育舞蹈','男子体育舞蹈','健美操',}

    if x in ball:
        print('推荐运动类型：球类运动')
    elif x in outdoor :
        print('推荐运动类型：户外运动')
    elif x in gongfu :
        print('推荐运动类型：武术运动')
    elif x in track :
        print('推荐运动类型：田径运动')
    elif x in dance :
        print('推荐运动类型：舞蹈运动')

if __name__  == '__main__':

    s = sport1(80,2,10000)

    x = sport2('游泳')

















