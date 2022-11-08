#練習一
#1. 請寫一個程式可以讓使用者連續輸入五個整數存入串列中，再從串列中找出最大值。
#list = [0 for i in range(5)]                                                  #看不懂?
#print('請輸入5個數字:')
#for i in range(5):
#    print('請輸入第{0}個整數:'.format(i+1),end=' ')
#    list[i] = int(input())                                                    #看不懂?
#print('串列為:',list)

#max = list[0]                                        #選取串列中的任何一位都可以
#for j in list:
#    if (j > max):
#        max = j
#print('最大值為:',max)






#2. 有一個串列為lst=[‘one’, ‘two’, ‘three’, ‘four’, ‘five’]，請將’three’由英文改成中文 ‘三’後再將整個串列列印出來。
 #list = ['one', 'two', 'three', 'four', 'five']
 #list[2] = '三'
 #print(list) 
 #for i in list:
 #    print(i,end=",")

#3. 有一個學生串列stu[]中有108名學生姓名，最後10名為轉學生。若要顯示不含轉學生的學生姓名，請問串列分割的表示法要如何寫？
 #stu[0:99]
 #stu[:-10]





#練習二
 #1. 有一個串列應該由0~9的數字所組成lst=[1, 8, 3, 6, 4, 7, 9, 2, 0]，但是發現其中少了5這個數字，請將它加入串列後並將數字依升冪排序後列印出來。
  #lst=[1, 8, 3, 6, 4, 7, 9, 2, 0]
  #lst.append(5)
  #list = sorted(lst)
  #for i in list:
  #    print(i,end=' ')
  #print('\n')
  #for i in range(len(list)):
  #    print(list[i], end=' ')

 #2. 下列程式碼，執行後輸出值為何？(不寫程式，用想的)
  #lst1 = [11, 22]
  #lst2 = [33, 44]
  #lst3 = lst1 + lst2
  #lst4 = lst3 * 2
  #print(lst4) [11,22,33,44,11,22,33,44]

#3. 假設班上有5個學生，請設計一個程式讓學生用座號簽到，一個人簽到後立即顯示尚未簽到的座號，待所有學生都簽到完畢後才結束程式。
  #解:
  #list = [1,2,3,4,5]
  #while (len(list)>0):                                   #迴圈結束在串列長度為0時
  #    print('尚未簽到座號:\t',end='')
  #    for n in list:
  #        print(n,end=' ')
  #    #print()                                            #換行 用法
  #    num = int(input('\n請輸入簽到座號:\t'))                  
  #    if(num<1 or num>5):
  #        print('輸入座號錯誤,請重新輸入')
  #        continue
  #    else:
  #        for index, i in enumerate(list):               #用 enumerat 將索引值與元素值分開
  #            if (num == i):
  #                del list[index]
                  #break
  #print('簽到完成')



  #老師解
  #stu = [1, 2, 3, 4, 5]
  #while (len(stu) > 0):
  #    print('未簽到座號: ', end='')
  #    for item1 in stu:
  #        print('{0}'.format(item1), end=' ')
  #    print()
  #    num = int(input('請輸入座號簽到: '))
  #    if (num < 1 or num > 5):
  #        print('座號不存在!')
  #        continue
  #    else:
  #        find = False
  #        for i, item2 in enumerate(stu):
  #            if (item2 == num):
  #                del stu[i]                         #為避免順序亂掉而刪錯元素值,因此從索引值去刪!!!
  #                find = True
  #                break
  #        if (find == False):                        #為避免重複顯示,使用布林值防止進入此迴圈,但是怎麼做到?
  #            print('{0} 已經簽到了!'.format(num))
  #print('簽到完畢!')




#練習三
#1. 有一個元組(Tuple)的資料為tuple1=(‘id’, ‘name’, ‘age’)，請加入’height’到元組內，並將’age’改成’weight’。
 #tuple1 = ('id','name','age')
 #list = list(tuple1)
 #list.append('height')
 #list[2] = 'weight'
 #tuple = tuple(list)
 #print(tuple)

#2. 有兩個字典資料如下：
 #dict1 = {'p':'Python', 'r':'Ruby', 'j':'Java'}
 #dict2 = {'Python':'易學', 'Ruby':'難學', 'Java':'中等'}
 #當使用者輸入p或r或j時，請輸出對應語言的學習難度。
 
 #解:
 #dict1 = {'p':'Python', 'r':'Ruby', 'j':'Java'}
 #dict2 = {'Python':'易學', 'Ruby':'難學', 'Java':'中等'}
 #print('請輸入代碼p/r/j: ', end=' ')
 #n = input()
 #print('{0},\t 語言難度為:\t{1}'.format(dict1[n] , dict2[dict1[n]]))

#3. 某校有兩個社團與成員資料如下：
 #group1 = ['A', 'B', 'C', 'D', 'A', 'C']
 #group2 = ['E', 'F', 'B', 'D', 'E', 'G', 'D’]
 #規則為不可重複報名或是同時參加兩個社團，請列出：
 #各社團的參加人數與正確人數
 #重複參加社團的名單
 #若是兩社團合併後的正確人數 

 #解:
 #group1 = ['A', 'B', 'C', 'D', 'A', 'C']
 #group2 = ['E', 'F', 'B', 'D', 'E', 'G', 'D']
 #gn11 = len(group1)
 #gn12 = len(set(group1))
 #print('社團一\t參加人數:{0}\t正確人數:{1}'.format(gn11,gn12))
 #gn21 = len(group2)
 #gn22 = len(set(group2))
 #print('社團二\t參加人數:{0}\t正確人數:{1}'.format(gn21,gn22))
 #set1 = set(group1)
 #set2 = set(group2)
 #print('重複參加社團的名單:{0}'.format(set1 & set2))
 #print('合併後的正確人數:{0}'.format(len(set1|set2))) 

 #老師解: 
 #group1 = ['A', 'B', 'C', 'D', 'A', 'C']
 #group2 = ['E', 'F', 'B', 'D', 'E', 'G', 'D']
 #set1 = set(group1)
 #print('社團一參加人數 {0} 人, 正確人數 {1} 人'.format(len(group1), len(set1)))
 #set2 = set(group2)
 #print('社團二參加人數 {0} 人, 正確人數 {1} 人'.format(len(group2), len(set2)))
 #set3 = set1.intersection(set2)
 #print('重複參加社團名單:', set3)
 #set4 = set1.union(set2)
 #print('合併後社團人數 {0} 人'.format(len(set4)))


#練習四
#1. 請寫一個程式可以讓使用者輸入資料，程式要把輸入值轉換成整數，如果輸入值無法轉換成整數則程式要做錯誤處理來印出錯誤訊息，並讓使用者可以重新輸入。
  #while(True):
  #    try:
  #        print('請輸入資料:')
  #        int(input())
  #        break
  #    except ValueError as e:          是ValueError!!!
  #        print(e)
  #        print('請重新輸入!')
          #continue

#2. 請寫一個程式讓使用者輸入密碼，長度為5~8個字元，若是長度不符規定就用例外處理的方式顯示錯誤訊息。 
  #try:
  #    password = input('請輸入密碼(5-8個字元): ')
  #    n = len(password)
  #    if (n<5 or n>8):
  #        raise Exception('密碼輸入長度超出範圍!')
  #except Exception as e:
  #        print(e)
        
