#練習一
#1. 請設計一個函式可以計算兩個整數相除，並傳回計算結果，若是除數為零則傳回None。   #違反規則用 '例外處理'
 #我解:
 # divident = int(input('請輸入被除數:\t'))                                  #如何使用自定義的例外處理??
 #divisor = int(input('請輸入除數:\t'))
 #def division (divident, divisor):
 #    try:
 #        remainder = divident / divisor  
 #        print('計算結果為:\t',remainder)
 #    except ZeroDivisionError:
 #        print('除數不可為0!')
 #division (divident, divisor)

 #老師解:
 #def divide(num1, num2):
 #    try:
 #       ans = num1 / num2
 #   except ZeroDivisionError:
 #       return None
 #   else:
 #       return ans
 #   
 #num1 = int(input('請輸入被除數:'))
 #num2 = int(input('請輸入除數:'))
 #ans = divide(num1, num2)
 #if (ans != None):
 #   print('計算結果:', ans)
 #else:
 #   print('除數不可為0!')

#2. 請設計一個函式可以產生n個隨機整數的串列，亂數範圍介於-100~100之間，最後回傳此串列。
 #再設計另外一個函式可以傳入一個整數串列並將此串列內的數值取絕對值，沒有傳回值。
"""
 from random import randint
 def random_list(n):
     list = [0 for i in range(n)]
     for x in range(len(list)):
         list[x] = randint(-100,100)                      #不懂??
     return list

 def absolute_value(list):
     for j in range(len(list)):
         list[j] = abs(list[j])                           #不懂??
        
 list1 = random_list(10)
 print(list1)
 absolute_value(list1)
 print(list1)
"""


#練習二
#1. 給定一個數值串列，請設計一個遞迴函式來計算串列中各元素的數值總和。 
'''
看不懂?
'''
#2. 有一個函式如右：(不寫程式，用算的)    請問func(13)的傳回值為何？
'''
def func(n):
    if(n > 1):
        return func(n-2) + 3
    return n
 f(13)                   f(11) + 3 = 19
 f(11)                   f(9)  + 3 = 16
 f(9)                    f(7)  + 3 = 13
 f(7)                    f(5)  + 3 = 10
 f(5)                    f(3)  + 3 = 7
 f(3)                    f(1)  + 3 = 4
 f(1)     1  開始遞迴計算
'''
#3. 讓使用者輸入等差數列的首項a、公差d與項數n，設計一個遞迴函式來求得等差數列的總和。
'''
看不懂?
'''


#練習三
#1. 請設計一個商品類別Product，其初始化方法可以設定商品名稱name及商品價格price兩個屬性的值。
# 請讓使用者輸入商品名稱與價格，然後用這些資料建立一個Product物件，並將物件屬性列印出來。
'''
 class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

 name = input('請輸入商品名稱:\t')
 price = input('請輸入商品價格:\t')
 p =  Product(name, price)
 print('商品名稱:', name, '價格:', price)
 '''

#2. 請設計一個Point類別，其初始化方法可以設定座標的x與y值。
# 請為它設計一個可以計算自己到另一個Point的距離的方法。建立兩個Point物件，p1的座標為(1, 1)，p2的座標為(2, 2)，試列印出此兩點的距離。

'''
 import math               #記住!!!!! 計算函式的輸入
 class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, point):
        d = math.sqrt(math.pow(self.x - point.x, 2) + math.pow(self.y - point.y, 2))
        print('距離為',d)
        
 #解1:
 p1 = Point(1, 1)
 p2 = Point(2, 2)
 distance = p1.distance(p2)

 #解2
 dis = Point(1,1)
 dis.distance(p2)
 '''


#練習四
 #1. 請設計一個倒數計時器類別Countdown，其有一個私有屬性counter，使用者可以用初始化方法來設定其數值。
 #設計一個run方法來啟動倒數功能，並設計一個顯示時間的方法show來顯示目前的counter值。(提示：使用import time的sleep(1))
'''
 import time
 class Counter:
    def __init__(self, sec):
        self.__counter = sec
    def show(self):
        print()
 #      print('', end='\r')
 #      print('目前剩餘{}秒'.format(self.__counter), end='\r')   #\r 浮標會退回始點
        print('目前剩餘{}秒'.format(self.__counter))
    def run(self):
        while (self.__counter >0):
            self.show()
            time.sleep(1)                             #停一秒
            self.__counter -= 1
        print('倒數結束')

 countdown = Counter(3)
 countdown.run()
'''

#練習五
#1. 請使用P.23的Student類別建立三個學生物件並以{座號:Student}存放在字典中，使用者可以輸入學生座號來顯示學生屬性資料。
#老師解
'''
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

stu1 = Student('John', 20, 90)            
stu2 = Student('Mary', 19, 95)
stu3 = Student('Tom', 18, 80)
stuDict = {1:stu1, 2:stu2, 3:stu3}        
num = int(input('請輸入學生座號:\t'))
if(num in stuDict):
    
    print('座號為:\t', num)
    print('姓名為:\t', stuDict[num].name)  
    print('年齡為:\t', stuDict[num].age)
    print('成績為:\t', stuDict[num].grade)
else:
    print('查無此號')
'''
#我解
'''
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
stu1 = Student('sam',18,100)                  #建立三個物件
stu2 = Student('xander',18,99)
stu3 = Student('sally',18,98)
dict = {1:stu1 , 2:stu2 , 3:stu3}             #三個物件存放在字典中
num = int(input('請輸入座號:\t'))
if (num in dict):
    #print(stuDict[num])                       # 不行! 原因???解釋?
                                            #字典套用方法
    print('座號:\t',num,'\n姓名:\t',dict[num].name,'\n年紀:\t',dict[num].age,'\n成績:\t',dict[num].grade,sep='')
else:
    print('錯誤座號')
'''