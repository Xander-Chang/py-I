#練習一
#1. 有一個二維串列內容為[[1,‘John’,85], [2,‘Mary’,90], [3,‘Tom’,75], [4,‘Steve’, 60]]，
# 請使用with open() ... as的方式將這些資料寫入data1.txt檔案中，若用記事本軟體開啟檔案來看應該為下圖格式。
'''
data_list = [[1,'John',85], [2,'Mary',90], [3,'Tom',75], [4,'Steve', 60]]
fn = 'data1.txt'
with open(fn , 'a') as fn1:
    for i in data_list:
        print(i)
        j = str(i) + '\n'
        fn1.write(j)             #write()只能寫str,因此要先把list轉成str,所以不能直接寫 write(i)

'''

#2. 承上題，請先檢查data1.txt是否存在，若存在則將data1.txt檔案讀入二維串列之中，資料型態需要與原來的二維串列內容相同，然後將此串列印出來。
'''
import os 
if (os.path.exists('data1.txt') == True):                               #不懂....?
    list = []
    with open(fn, 'a+') as fn2:
        fn2.readlines()
        for i in fn2:
            list += i.strip() 
            list1 = []
            print(list)
else:
    print('檔案不存在')
'''

