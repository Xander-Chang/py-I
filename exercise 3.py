#練習一   (單向流程控制)
 #1. 請設計一個程式可以輸入任意整數，然後輸出絕對值。
  #x = int(input('請輸入任意數:'))
  #if x < 0 :
  #    x = -x
  #print('絕對值:', x)

 #2. 請設計一個程式可以輸入學生成績，成績在>=55且未達60分者，以60分計分。
  #grade = float(input('請輸入學生成績:'))
  #if grade >= 55 and grade < 60:
  #   print('成績為60分')
  #else:
  #   print('成績為',grade)

 #老師解
  #grade = int(input('輸入學生成績:'))
  #if ((grade >= 55) and (grade < 60)):
  #   grade = 60
  #print('最終成績=', grade)

#練習二   (雙向流程控制)
 #1. 請設計一個程式可以輸入任意整數，輸出奇偶數的判斷。
  #x = int(input('請輸入任意數:'))
  #y = x % 2
  #if y == 0 :
  #   print(x, '是偶數')
  #else:
  #   print(x, '是奇數')

 #2. 假設電影票原價300元，請設計一個程式可以輸入年齡，若年齡低於10歲或大於等於65歲時則半價優惠。
  #ticket = 300
  #age = int(input('請輸入年齡:'))
  #解一
   # if age < 10 or age >= 65:
   # print('票價為' + str(ticket * 0.5) + '元')
   #else:
   # ticket = 300
   # print('票價為:' + str(ticket) + '元')
 
  #解二
   # if age < 10 or age >= 65:
   #   ticket /= 2
   #else:
   #   ticket /= 1
   #print('票價為\t%.1f元' % ticket)
   
#練習三   (巢狀流程控制)
 #請設計一個程式可以輸入西元年份數字，然後判斷其是否為潤年並輸出結果。潤年的條件是可以被4整除，並且必須符合除以100時餘數不為0或是除以400時餘數為0。
 #year = int(input('請輸入西元年:'))
 #leapyear = True
 #if year % 4 == 0:
 #   if (year % 100 != 0) or (year % 400 ==0):
 #       leapyear = True
 #       print('%d為閏年' % year)
 #   else:
 #       leapyear = False
 #       print(year, '並非閏年,請重新輸入')
 #else:
 #   print(year, '並非閏年,請重新輸入')

#練習四   (多向流程控制)
 #1. 有一個戲院的票價一張票賣100元，但是如果觀眾年齡小於等於6歲或是年齡大於等於80歲，則收費是打二折；
 # 但若觀眾的年齡是7~12歲或是60~79歲則收費是打五折。請設計一個程式，輸入觀眾的年齡，然後可以自動計算票價輸出。
 #t = 100
 #age = int(input('請輸入年齡:'))
 #if (age <= 6) or (age >= 80):
 #   t *= 0.2
 #elif (age <= 12) or (age >= 60):
 #   t *= 0.5
 #else:
 #   t *= 1
 #print('您的票價為:%d元' % t)



 #2. 設計一個程式有中文的選項，輸入號碼會顯示對應的英文單字，畫面如下：
 #num = int(input('請輸入數字1~3,其中的任一數'))
 #if num == 1:
 #   print('英文單字: apple')
 #elif   num == 2:
 #   print('英文單字: banana')
 #elif   num == 3:
 #   print('英文單字: mango')
 #else:
 #   print('輸入錯誤,請重新輸入')

#練習五   (for迴圈)
 #請設計一個程式可以輸入兩個不同的正整數，然後計算兩個整數間所有數字的總和並輸出結果。
 #例如：
 #請輸入第一個數字：1
 #請數入第二個數字：10
 #總和：55
 
 #firnum = int(input('請輸入第一個數字:'))
 #secnum = int(input('請輸入第二個數字:'))
 #sum = 0
 #if firnum != secnum:
 #   if firnum > secnum:
 #       firnum, secnum = secnum, firnum                                              
 #   for x in range (firnum, secnum+1) :
 #       sum += x 
 #   print('總合為%d'% sum)
 #else:
 #   print('兩正整數不能相同,請重新輸入:')

#練習六   (for ... else迴圈)
 #請設計一個程式可以輸入三個整數，然後加總後計算平均值並輸出結果到小數點2位。

 #sum = 0
 #for x in range (3):
 #   fig = '請輸入第' + str(x + 1) + '個整數:'             # str('加引號會直接變成字串直接顯示,而不是數值,無法做運算')
 #   num = int(input(fig))
 #   sum += num
 #average = sum / 3
 #print('平均值為%.2f' % average)

#練習七   (while迴圈)
 #請設計一個程式可以一直輸入文字，並輸出相同的文字，直到輸入q才結束。
 #text = ''                                                                            # ''表達某物?
 #while (text != 'q'):
 #   text = input('請輸入文字:')
 #  print(text)
 #print('結束程式')

#練習八   (while ... else迴圈)
 #請設計一個程式可以讓使用者輸入成績，然後程式自動判斷成績等級並輸出，直到使用者輸入q才結束。成績等級定義如下：
 #A: 成績>=90
 #B: 成績>=80 且 <90
 #C: 成績>=70 且 <80
 #D: 成績>=60 且 <70
 #E: 成績<60
 
 #grade = ''
 #while (grade != 'q'):
 #   grade = input('請輸入成績:')                             # 'q'為字串,成績為數值，因此要分成兩個變數區分
 #   if (grade != 'q'):                                      # 不能理解這個if的作用?
 #    score = int(grade)
 #    if score >= 90:
 #       print("成績等級為A")
 #    elif score >= 80:
 #       print("成績等級為B")
 #    elif score >= 70:
 #       print("成績等級為C")
 #    elif score >= 60:
 #       print("成績等級為D")
 #    else:
 #       print("成績等級為E")
 #    else:
 #     print('結束程式')                                        #此else 是給 第一個if 還是 while? 怎麼解釋不同
 #else:
 #    print('結束程式')    

#練習九   (continue指令)
 #請設計一個程式可以產生10個隨機整數，數值要介於1~100之間，每產生一個隨機數就將它輸出，並將隨機值加總，可是小於60的數值就不加，最後印出總和結果。
 #import  random
 #sum = 0
 #for x in range(10):
 #   num = random.randint(1,100)        # 終值的位置要注意
 #   print('第%d次: %d' % (x+1,num))
 #   if (num < 60) :
 #       continue                       #是否需要加上 del 刪掉60以下的num? 如何使用?
 #   else:
 #       sum += num
 #print('總合為:%d' % sum) 

#練習十   (break指令)
 #1. 請設計一個程式產生一個介於0~9的隨機數字讓使用者猜，使用者只有三次輸入的機會，前兩次猜錯的話要提示下一次要多或少，如果最後沒猜中就要將答案輸出。
 #import random
 #num = random.randint(0, 9)
 #x = 1
 #while(x <= 3):
 #   guess = int(input('請輸入0-9的一整數:'))
 #   if guess == num:
 #       print('恭喜答對!')
 #       break
 #   elif (x == 2):
 #       if(guess > num):
 #           print('低一點')
 #       else:
 #           print('高一點')
 #   x += 1
 #else:
 #   print('答案是' , num)


 #2. 請設計一個擲筊的程式，程式會產生兩個亂數，0代表反面，1代表正面，當亂數值為0與1或1與0時程式結束執行，否則程式會一直執行。
 #解1
 #import random
 #while(True):
 #   num1 = random.randint(0,1)
 #   num2 = random.randint(0,1)
 #   print('num1 = %d, num2 = %d' % (num1, num2))
 #   if(num1 + num2 == 1):
 #       print('done')
 #       break
 #解2
 #from random import randint
 #x = 0
 #while(True):
 #   n1 = randint(0,1)
 #   n2 = randint(0,1)
 #   print(n1,n2)
 #   x += 1
 #   if(n1 + n2 == 1):
 #     print(n1,n2,'第%s次'% x)
 #     break  

 #老師解
 #from random import randint
 #counter = 0
 #while (True):
 #   num1 = randint(0, 1)
 #   num2 = randint(0, 1)
 #   print('num1 = %d, num2 = %d' % (num1, num2))
 #   if (num1 + num2 == 1):
 #       print('totol %d times' % (counter + 1))
 #       break
 #   counter += 1                                     # 放在最下似乎不是最佳?

#練習十一   (巢狀迴圈)
 #1. 請設計一個程式可以輸出九九乘法表，並請將輸出排列整齊。


 #for n1 in range(1, 10):
 #   for n2 in range(1, 10):
 #       n3 = n1*n2
 #       print('%d*%d=%02d'% (n1,n2,n3),end=' ')
 #   print('')                                           ##看不懂?


 #2. 下列程式碼中，哪個片段不會被執行？

 #n = 0
 #while (1):              # while(1)永遠不會等於0,循環會一直執行,除非有設置break
 #    n += 1
 #    if (n > 10):
 #        break
 #    print(n)
 #else:
 #    print('迴圈結束!')   #用不到
 #print('程式結束!')

