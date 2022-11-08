#練習一
# 1. 請問以下資料應該使用何種資料型別？
#(A)name(姓名,’李連城’):str		(B)age(年齡,21):int
#(C)title(職稱,’經理’):str		(D)weight(體重,53.8):float
#(E)years(年資,12):int			(F)married(已婚,True):boolean
#(G)zip(郵遞區號,’301’):str

#2. 寫一個程式，宣告兩個變數分別為三角形的底25.6與高10.84
#請計算三角形的面積並將面積輸出。
height = 10.84
bottom = 25.6
dimension = bottom*height/2
#print("三角形面積:", dimension)

#3. 請列印出下列數值的2進位、8進位及16進位的值
#     (a)199   (b)55   (c)255
a = 199
b = 55
c = 255
#print(bin(a), oct(a), hex(a)) #0b11000111 0o307 0xc7 
#print(bin(b), oct(b), hex(b)) #0b110111 0o67 0x37       
#print(bin(c), oct(c), hex(c)) #0b11111111 0o377 0xff

#4. 請將下列數值轉成10進位
#     (a)0b11110010   (b)0o666   (c)0xabcdef
#print(0b11110010 ,0o666,0xabcdef ) #242 438 11259375

#5. 請問0x12與0b0010相加結果以10進位顯示為何?
#     (a)22   (b)20   (c)18   (d)5
#print(int(0x12) + int(0b0010)) #print(0x12 + 0b0010)= (b)20




#練習二(不需要寫程式，用心算)
#1. 下列程式碼執行後輸出結果為何？
#a, b = 2, 3
#c, d = 4, 5
#val = b // a + c // b + d // b
#print(val) 3

#2. 假設x、y、z皆為boolean變數，且x=True、y=True、z=False，請問下列運算式的結果為何？
#(A)not(y or z) or x         true
#(B)not y or (z or not x)    false
#(C)z or (x and (y or z))    true
#(D)(x or x) and z           false

#3. 若要邏輯判斷式not(x or y)計算結果為True，則x和y的值分別應該為何？
#(x or y) = false 皆為false

#4. 請問以下的執行結果：                                                               看不懂
0 or 6 
3 and 'a'
5 or 'b' 

#5. 下列程式碼執行後，a、b及c的資料型態為何？
x1 = '5'
y1 = 4
a = x1 * y1
x2, y2 = 6, 3
b = x2 / y2
x3, y3 = 1.0, 2
c = x3 + y3
#print(type(a), type(b), type(c))



#練習三
#1. 請設計一個程式可以輸入攝氏溫度，然後輸出華氏溫度(小數點一位)。
#華氏溫度 = 攝氏溫度 * (9 / 5) + 32
#celsius = float(input('請輸入攝氏溫度:'))  #需要有float才能計算
#fahrenheit = celsius * (9 / 5) + 32
#print('華氏溫度:%.1F度'% (fahrenheit))

#2. 請設計一個程式可以輸入學生的名字、英文分數與數學分數，接著計算總分與平均分數(小數點一位)，最後列印出如下格式：
student = input('type ur name:')
english = float(input('type ur english score:'))
math = float(input('type ur math score:'))
total = float(english + math)
average = float(total / 2)
#print('|姓名:\t',str(student),'|'\n,'|英文成績:\t',float(english),'|'\n,'數學成績:\t',float(math),'|'\n,'總分:\t',float(total),'|'\n,'平均:\t',float(average),'|')
#print('|姓名:\t',str(student),'|')
#print('|英文成績:\t',float(english),'|')
#print('|數學成績:\t',float(math),'|')
#print('|總分:\t',float(total),'|')
#print('|平均:\t',float(average),'|')
print('|姓名:     %10s|' % (student))
print('|英文成績: %10d|' % (english))
print('|數學成績: %10d|' % (math))
print('|總分:     %10d|' % (total))                   #用%d 整數顯示
print('|平均:     %10.1f|' % (average))               #用% 空格會變長