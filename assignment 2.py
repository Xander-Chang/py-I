#回家功課
# 1. 請設計一個程式讓使用者可以輸入存款金額(整數)、年利率(浮點數)和存款年數(整數)，然後計算出單利和複利的本利和(字寬12格，顯示到小數一位)。
# 單利：本利和 = 本金 + 本金 x 年利率 x 年數
# 複利：本利和 = 本金 x (1 + 年利率) ^ 年數

deposit = int(input('type amount:'))
rate = float(input('type the interests:'))
years = int(input('type how many years:'))
simple_interests = deposit + deposit * rate * years
compound_interests = deposit * (1+rate) ** years
print('單利本利和: %12.1f 元' % simple_interests)
print('複利本利和: %12.1f 元' % compound_interests)


# 2. 請設計一個程式，輸入距離(單位公尺)和秒數後，會算出運動員跑步的速度(每分鐘可以跑幾百公尺，顯示到小數第二位)，使用Python內建函式使輸出結果盡可能精準。
# 例如：
# 請輸入距離(單位公尺):246
# 請輸入秒數(單位秒):32.5
# 速度為:4.54百公尺/分鐘

distance = float(input('請輸入距離:'))
seconds = float(input('請輸入秒數:'))
meter_min = distance / seconds * 60 / 100
print('速度為:%.2f\t百公尺/分鐘' % meter_min)

