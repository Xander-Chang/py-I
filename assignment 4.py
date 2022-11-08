#回家作業(本次作業要記得上傳)
 
 #1.請撰寫一程式，輸入四個分別含有小數1到4位的浮點數，然後將這四個浮點數以欄寬為7、每列印兩個的方式，
 # 先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。
 #(23.12),(395.30),(100.46),(564.33)
 #a = 23.12
 #b = 395.30
 #c = 100.46
 #d = 564.33
 #print('|%7.2f %7.2f|'% (a, b))
 #print('|%7.2f %7.2f|'% (c, d))
 #print('|%-7.2f %-7.2f|'% (a, b))
 #print('|%-7.2f %-7.2f|'% (c, d))




#2.請設計一個行動電話號碼檢查程式，電話號碼要符合下面的條件：
 #格式必須為0000-000-000，只由數字與-組成
 #若格式正確就顯示’行動電話號碼格式正確’，反之就顯示’行動電話號碼格式錯誤‘
 #可以連續輸入並檢查，當使用者輸入q後結束程式

 #解一:
  #while(True):
  #    n1 = input('請輸入號碼或按q離開:')
  #    n2 = n1.split('-')
  #    if(n1 == 'q'):
  #        print('程式結束')
  #        break
  #    elif(len(n2) == 3):
  #        if(len(n2[0]) == 4 and len(n2[1]) == 3 and len(n2[2]) == 3):
  #             if(n2[0].isdigit and n2[1].isdigit and n2[2].isdigit):
  #               print('行動電話號碼格式正確')
  #   else:
  #       print('行動電話號碼格式錯誤')

 #同學解:
  #while(True):
  #  F = False
  #  num = input('請輸入電話號碼或按q結束程式:')
  #  if (num == 'q'):
  #      break
  #  num2 = num.split('-')
  #  if(len(num2) == 3):
  #      if(len(num2[0]) == 4 and len(num2[1]) == 3 and len(num2[2]) == 3):
  #          if(num2[0].isdigit() and num2[1].isdigit() and num2[2].isdigit()):
  #              F = True
  #  if(F):
  #      print('輸入格式正確!')
  #  else:
  #      print('格式錯誤，請從新輸入:')
  #print('程式結束')
      
