#回家功課
#1. 請設計一個程式讓使用者可以輸入一個正整數，程式會顯示從2到該數之間的所有質數。
p = 2
num = int(input('請輸入一個正整數:'))
while (p <= num):
    flag = True #預設為質數
    for i in range(2, p):
        if (p % i == 0):
            flag = False
            break
    if (flag == True):
        print(p, end=' ')
    p += 1





#2. 請設計一個猜拳遊戲，使用者玩到贏才能結束。
 #from random import randint
 #x = 1
 #while(True):
 #   gamer = int(input('請輸入剪刀(0)石頭(1)布(2)的代表數字:'))
 #   ai = randint(0,2)
 #   if gamer == ai :
 #       print('平手!請再輸入剪刀(0)石頭(1)布(2)的代表數字:')
 #   elif gamer == 0:
 #       if ai == 1:
 #           print('請再輸入剪刀(0)石頭(1)布(2)的代表數字:')
 #       else:
 #           break
 #   elif gamer == 1:
 #       if ai == 2:
 #           print('請再輸入剪刀(0)石頭(1)布(2)的代表數字:')
 #       else:
 #           break
 #   elif gamer == 2:
 #       if ai == 0:
 #           print('請再輸入剪刀(0)石頭(1)布(2)的代表數字:')
 #       else:
 #           break
 #   else:
 #       print('輸入錯誤')        
 #   x += 1
 #print('恭喜在第%x次獲勝' % (x))

 #老師解
 #A2.
 #import random
 #0代表剪刀, 1代表石頭, 2代表布
 #while (True):
 #   player = int(input('請輸入剪刀(0);石頭(1);布(2):'))
 #   computer = random.randint(0, 2)
 #   if (player == 0):
 #       pp = '剪刀'
 #   elif (player == 1):
 #       pp = '石頭'
 #   elif (player == 2):
 #       pp = '布'
 #   else:
 #       print('輸入錯誤!')
 #       continue
 #   if (computer == 0):
 #       cc = '剪刀'
 #   elif (computer == 1):
 #       cc = '石頭'
 #   else:
 #       cc = '布'
 #   if player == computer:
 #       print('電腦出 %s, 你出 %s, 結果平手，再來!' % (cc, pp))
 #   elif (player == 1 and computer == 0) or (player == 0 and computer == 2) or (player == 2 and computer == 1):
 #       print('電腦出 %s, 你出 %s, 結果你贏了!' % (cc, pp))
 #       break
 #   else:
 #       print('電腦出 %s, 你出 %s, 結果你輸了!' % (cc, pp))


#3. 請寫一個程式有一個主功能表選項，若輸入1~3就顯示對應的作業名稱，若輸入0就顯示’程式結束’並結束程式，若輸入不是介於0~3的數值，則顯示’輸入不正確’。
 #print('==主功能表==')
 #print('1.新增作業')
 #print('2.修改作業')
 #print('3.查詢作業')
 #print('0.結束程式')
 #while(True):
 #   c = input('請輸入選項(0-3):')
 #   if c =='1':
 #       print('1.新增作業')
 #   elif c == '2':
 #       print('2.修改作業')
 #   elif c == '3' :
 #       print('3.查詢作業')
 #   elif c =='0':
 #       break
 #   else:
 #       print('輸入錯誤')
 #print('0.結束程式')
