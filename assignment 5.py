#1. 下表為四位學生的成績，請寫一個程式完成空白部分的數據並完整列印出來。(平均分數到小數點一位)

 #我解:
 #num = [1,2,3,4]
 #g1 = [85,83,90]
 #g2 = [95,60,82]
 #g3 = [76,77,80]
 #g4 = [63,98,75]
 #g = [[85,83,90], [95,60,82], [76,77,80], [63,98,75]]
 #g100 = [g1,g2,g3,g4] 

 #print('座號\t英文\t數學\t國語\t總分')

 #for i in range(len(num)):                                 #記住用法!!!!!!
 #    print('%d' % num[i],end='\t')
 #    sum = 0
 #    for j in range(len(g100[i])):        
 #        sum += g100[i][j]                                 #串列必須用 二維,  用g100[i]而非g100, 不然座標不對
 #        print('%d\t' % (g100[i][j]),end='')
 #    print('%d' % (sum))   
 
 #print('平均',end='\t')    
 #for x in range(3):
 #    sum = 0
 #    average = 0
 #    for y in range(4):
 #        sum += g100[y][x]                      
 #        average = sum / len(num)                            #也可以用作號去除
 #    print('%.1f' % (average),end='\t') 



 #老師解:
 #no = [1, 2, 3, 4]
 #score = [[85, 83, 90], [95, 60, 82], [76, 77, 80], [63, 98, 75]]
 #print('座號    英文    數學    國語    總分')
 #print('===================================')
 #for i in range(len(no)):
 #   print('%2d' % no[i], end='    ')
 #   hSum = 0
 #   for j in range(len(score[i])):
 #       print('%3d' % score[i][j], end='     ')
 #       hSum += score[i][j]
 #   print('%3d' % hSum)
 #print('%s' % '平均', end='    ')
 #for i in range(3):
 #   vSum = 0
 #   for j in range(len(no)):
 #       vSum += score[j][i]
 #   print('%4.1f' % (vSum / len(no)), end='    ')


#2. 請設計一個程式可以新增、刪除及查詢的英漢字典，畫面如圖：
 #功能需求：
 #選項1：若英文單字不存在字典中，就新增到字典內，
 #否則修改中文解釋
 #選項2：若英文單字存在字典中，就刪除此單字，
 #否則提示不存在此單字
 #選項3：若英文單字存在字典中，就顯示其中文解釋，
 #否則提示不存在此單字 

 #我解:
 #print('===電腦字典===\n1.新增/修改單字\n2.刪除單字\n3.查詢單字\n4.結束程式\n')
 #dic = {}
 #while(True):
 #    print('請輸入操作選項(1~4):',end='\t')
 #    option = input()
 #    if(option == '1'):
 #        word = input('請輸入英文單字:')
 #        if(word in dic):
 #            explicate = input('請修改中文解釋:')
 #            dic[word] = explicate
 #            print('已修改單字:\t',word)
 #        else:
 #            explicate = input('請輸入中文解釋:')
 #            dic[word] = explicate
 #            print('已修改單字"{0}" 中文解釋:\t'.format(word))
 #    elif(option == '2'):
 #        word = input('請輸入英文單字:')
 #        if (word in dic):
 #            del dic[word]
 #            print('已刪除單字:\t',word)
 #        else:
 #            print('不存在此單字!')
 #    elif(option == '3'):
 #        word = input('請輸入英文單字:')
 #        if(word in dic):
 #            print('單字:{0}\t中文解釋:\t{1}'.format(word, dic[word]))
 #        else:
 #            print('不存在此單字')
 #    elif(option == '4'):
 #        print('88')
 #        break
 #    else:
 #        print('無此選項,請重新輸入')
         


 #老師解:
 #table = '''                                   #函式table表格用法!!!  用三個引號包起來
 #===電腦字典===
 #1.新增/修改單字
 #2.刪除單字
 #3.查詢單字
 #4.結束程式
 #請輸入選項(1~4):
 #'''
 #dict1 = {}
 #while (True):
 #    print(table)
 #    function = input()
 #    if (function == '1'):
 #        eng = input('請輸入英文單字:')
 #        chi = input('請輸入中文解釋:')
 #        dict1[eng] = chi
 #        print('已新增/修改 {0}!'.format(eng))
 #    elif (function == '2'):
 #        eng = input('請輸入英文單字:')
 #        if (eng in dict1):
 #            del dict1[eng]
 #            print('{0} 已刪除!'.format(eng))
 #        else:
 #            print('單字不存在!')
 #    elif (function == '3'):
 #        eng = input('請輸入英文單字:')
 #        if (eng in dict1):
 #            print('{0} 的中文解釋: {1}'.format(eng, dict1[eng]))
 #        else:
 #            print('單字不存在!')
 #    elif (function == '4'):
 #        print('Bye!')
 #        break
 #    else:
 #        print('輸入選項錯誤!')
 



