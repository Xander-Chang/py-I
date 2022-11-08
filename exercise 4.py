#練習一
 #1. 請將'We like Python!’這個字串反向列印出來變成’!nohtyP ekil eW'
  #text = 'We like Python!'
  #print(text[::-1])        # !nohtyP ekil eW

 #2. 請使用跳脫序列將'蘋果30元愛文芒果15元奇異果20元'列印成
  #print('蘋果\t30元\n愛文芒果15元\n奇異果\t20元')           #為何印出來格式不對? 芒果中間

 #3. 請寫一個程式可以計算下列字串中指定字母的數量：
  #字串為'Python is my favorite language.'
  #方式1:
  # text = 'Python is my favorite language.'
  #abc = input('輸入要計算的字母:')
  #t = 0
  #for x in text:
  #   if (abc in x ):                                # in 的用法
  #       t += 1
  #print(abc+'總共有',t,'個') 

  #方式2:
  #text = 'Python is my favorite language.'
  #abc = input('輸入要計算的字母:')
  #t = 0
  #for x in text:
  #   if (abc == x ):                                # ==  這樣可以嗎?
  #       t += 1
  #print(str(abc) + '總共有'+ str(t) + '個')   

#練習二
 #1. 請設計一個程式可以接受使用者輸入學生姓名及分數，然後依照下列格式用format方法列印出來：
 #姓名前後要用雙引號括住
 #分數直接顯示不用引號或其他字元括住
 #姓名和分數之間用逗號隔開
 #name = input('請輸入姓名:')
 #score = int(input('請輸入分數:'))
 #print('"{}",{}'.format(name,score))   #資料型態可以不管?


 #2. 有一個商品紀錄有三項資料以及列印格式分別是：
 #品名：遙控車 (佔10個空格，靠左對齊)
 #成本：10.255 (佔7個空格，靠右對齊，小數點兩位)
 #售價：17.54 (佔6個空格，靠右對齊，小數點一位)
 #請用format方法列印出來。
 #item = "遙控車"
 #cost = float(10.255)
 #price = float(17.54)
 #print('品名:{0:10s}\n成本:{1:7.2f}\n售價:{2:6.1f}'.format(item,cost,price))

#練習三
 #1. 請將'Simple is better than complex'這句話的每個單字都改成第一個字母大寫，將空白字元改成’-’後列印出來。
 #解一
 #s = 'Simple is better than complex'.title().replace(' ','-')
 #print(s)

 #解二
 #s = 'Simple is better than complex'
 #s2 = s.title()
 #print(s.replace(' ','-'))

 #2. 請寫一個程式讓使用者輸入一個英文字串，然後將該字串的每個字元所對應的Unicode碼分別列印出來，並將每個Unicode碼的值加總後也列印出來。
 #ord(s)
 #t = input('請輸入一個英文字串:')
 #sum = 0
 #for x in t :
 #   u = ord(x)
 #   print(u)
 #   sum += u
 #print(sum)

 #老師解
 #t = input('請輸入字串:')
 #sum = 0
 #for x in t:
 #   u = ord(x)
 #   print('\'{0}\'的Unicode碼是\'{1}\''.format(x,u))       #print("'%s'的Unicode碼是'%d'"%(x,u))
 #   sum += u
 #print('Unicode碼的總和是\'{0}\''.format(sum))             #print('Unicode碼的總和是"%d"'% (sum))


 #3. 有一個字串內容為'   PythoN IS ThE BesT LanguagE.   '，字串左右各有三個空白。請寫一個程式做以下處理：
 #將字串的左右空白去掉
 #只有第一個字的第一個字母要大寫，其他字母都小寫
 #s = '   PythoN IS ThE BesT LanguagE.   '.capitalize().strip()   ####用法學起來
 #print('結果:\'{}\''.format(s))                                  #四種不同print
 #print("結果:'%s'"% (s))
 #print('結果:',s)
 #print('結果:',str(s))


#練習四
 #1. 請寫一個程式整數乘法測驗程式，需求如下：
  #隨機亂數產生整數被乘數介於11~20之間
  #隨機亂數產生整數乘數介於1~10之間
  #答題結束時要顯示是否答對以及所花費時間秒數到小數第二位
  
  #循環問題解
  #import random
  #import time
  #n1 = random.randint(11,20)
  #n2 = random.randint(1,10)
  #ans = n1*n2
  #a = True
  #while(True):
  #   q = print('{0} x {1} = ?'.format(n1,n2),end=' ')                        #用end來改變格式
  #   t1 = time.time()
  #   quest = eval(input(q))                                                  #'eval'把input的字串變成數值。 為何用上變數會跑出 None?
  #   t2 = time.time()
  #   if(ans == quest):
  #       print('你答對了，正確答案為%d,總共花費%s秒' % (ans , (t2-t1)))
  #       break
  #   else:
  #       print('你答錯了，正確答案為%d,總共花費%s秒' % (ans , (t2-t1)))


  #老師解:
  #import random
  #import time
  #num1 = random.randint(11, 20)
  #num2 = random.randint(1, 10)
  #answer = num1 * num2
  #print('請輸入 {0} x {1} = '.format(num1, num2), end='')
  #t1 = time.time()
  #user_input = eval(input())
  #t2 = time.time()
  #if (user_input == answer):
  #   print('你答對了, 花費時間 {0:.2f} 秒'.format(t2 - t1))
  #else:
  #   print('你答錯了, 正確答案為 {0:d}, 花費時間 {1:.2f} 秒'.format(answer, (t2 - t1)))  



#2. 請設計一個模擬大樂透開獎的程式，規則如下：
 #從1~49數字中隨機抽出7個數字，數字不可重複，第七個數字為特別號
 #顯示前六個數字時請從小到大排序，最後顯示特別號 

 #
 #from random import sample
 #scope = range(1,50)
 #list = sample(scope,7)
 #print('開獎號碼為:', list[:6], list[6],sep=',')
 #print('開獎號碼為:',end=' ')
 #for i in list[:6]:
 #    print(i,end=',')    
 #print(list[6])                                              #調整格式的方式
 #
 #order = sorted(list[:6])                                    #記住sorted 用法(排列大小,輸出串列)
 #print('\n排序號碼為:',end=' ')
 #for j in order[:5]:
 #    print(j,end=',')
 #print(list[5],end='')
 #print('\t特別號為:',list[6])

#老師解:
 #import random
 #random.seed(0)
 #numlist = random.sample(range(1, 50), 7)
 #print('開獎號碼為 ', end='')
 #for i in numlist[:6]:
 #    print(i, end=',')
 #print(numlist[6])
 #print('\n排序後號碼為 ', end='')
 #alist = numlist[:6]
 #while (len(alist) > 0):
 #    min = 99
 #    idx = 0
 #    for i in range(len(alist)):
 #        if (min > alist[i]):
 #            min = alist[i]
 #            idx = i
 #    del alist[idx]                                     #del alist[i] 為什麼不行?
 #    print(min, end=',')
 #print(numlist[6])
                                                       #看不懂?
